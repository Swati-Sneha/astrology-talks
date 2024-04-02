from fastapi import FastAPI, Request, Response, status, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import datetime
import jwt as pyjwt

# from openai import models as openAI_models
from app.enums import openAI_models
from openai import OpenAI
from app.settings import settings

horoscope_router = APIRouter(prefix="/horoscope", tags=["horoscope"])

open_ai_client = OpenAI(api_key=settings.OPEN_AI_KEY)

async def decode_jwt(jwt_token: str) -> dict:
    if jwt_token and jwt_token.startswith("Bearer "):
        jwt_token = jwt_token[len("Bearer ") :]
    
    secret_key = settings.JWT_SECRET.encode()
    payload = pyjwt.decode(jwt_token, secret_key, algorithms=["HS256"])
    
    return payload

@horoscope_router.get("/", status_code=status.HTTP_200_OK)
async def get_horoscope(request: Request, response: Response) -> JSONResponse:
    payload = {}
    jwt_token = request.headers.get("Authorization")
    if jwt_token:
        payload = await decode_jwt(jwt_token)
    
    name = request.query_params.get("name") or (payload.get("firstName") or "") + " " + (payload.get("lastName") or "")
    zodiac_sign = request.query_params.get("zodiac_sign")
    dob = (payload.get("dob") or "") if hasattr(payload, 'dob') else None

    if not name and not zodiac_sign:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": "Name and Zodiac Sign is required"}
    try:
        openAi_response = open_ai_client.chat.completions.create(
            model=openAI_models.GPT_35_TURBO_1106[0],
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": f"On {datetime.date.today()}, {name}'s horoscope for {zodiac_sign} {f'with date of birth {dob} ' if (dob != None) else ''}is: "}
            ]
        )

        horoscope = openAi_response.choices[0].message.content
        response.status_code = status.HTTP_200_OK
        return {"message": horoscope}
    
    except Exception as e:
            return {"message": "Failed to retrieve horoscope. Error: {}".format(e)}