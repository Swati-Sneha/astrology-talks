import datetime
import json
import jwt as pyjwt
from fastapi import Request, Response, status, APIRouter
from fastapi.responses import JSONResponse
from openai import OpenAI

# from openai import models as openAI_models
from app.enums import openAI_models

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

    name = payload.get("firstName") or request.query_params.get("name")
    zodiac_sign = request.query_params.get("zodiac_sign")
    username = name or payload.get("emailId")

    if not name or not zodiac_sign:
        "either the user should be logged in or should provide name and zodiac sign."
        response.status_code = status.HTTP_400_BAD_REQUEST
        return JSONResponse(
            content={"message": "Name and zodiac sign are required."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    try:
        openAi_response = open_ai_client.chat.completions.create(
            model=openAI_models.GPT_35_TURBO_1106[0],
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant designed to output JSON.",
                },
                {
                    "role": "user",
                    "content": f"On {datetime.date.today()}, {name}'s horoscope for {zodiac_sign} is:",
                },
            ],
        )

        horoscope_obj: dict = json.loads(openAi_response.choices[0].message.content)
        horoscope: str = horoscope_obj.get("horoscope")

        message = f"Hi {username}, what a beautiful day today to be a {zodiac_sign}! Here is your horoscope: {horoscope}"
        return JSONResponse(
            content={"horoscope": message}, status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Failed to retrieve horoscope. Error: {}".format(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
