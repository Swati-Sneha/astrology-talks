from fastapi import APIRouter, HTTPException, Request, status
from app.database.models.users import User, Login
from app.database.users import users_db
from app.store.interfaces.response_interfaces import SuccessResponse, ErrorResponse
from pymongo.errors import PyMongoError
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
import jwt as pyjwt
import datetime
import os
from typing import Any, Union
import bcrypt
from app.settings import settings


user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.post(
    "/register",
    response_model=User,
    summary="Register new user",
    status_code=status.HTTP_201_CREATED,
)
async def register(user: User) -> JSONResponse:
    db_user: Union[Any, None]= await users_db.get_user_by_email(user.emailId)

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists."
        )

    try:
        await users_db.register_user(user)
    except PyMongoError:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Error occurred saving user in the db.",
        )

    return JSONResponse(
        content=jsonable_encoder(user), status_code=status.HTTP_201_CREATED
    )


@user_router.post(
    "/login",
    response_description="Login user",
    response_model=SuccessResponse,
    status_code=status.HTTP_200_OK,
)
async def login(request: Request, login: Login):
    try:
        user: Union[Any, None] = await users_db.get_user_by_email(login.emailId)
        if user and bcrypt.checkpw(login.password.encode(), user.get("password")):
            payload = {
                "emailId": user.get("emailId"),
                "firstName": user.get("firstName"),
                "middleName": user.get("middleName"),
                "lastName": user.get("lastName"),
                "phoneNumber": user.get("phoneNumber"),
                "dob": user.get("dob")
                if user.get("dob")
                else None,
                "gender": user.get("gender"),
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(days=2),  # Set expiration time to 2 days
            }
            print(settings.JWT_SECRET)
            secret_key = settings.JWT_SECRET.encode()  # Convert to bytes
            algorithm = "HS256"
            token = pyjwt.encode(payload, secret_key, algorithm)
            return SuccessResponse(
                data={"token": token, "payload": payload},
                message="User logged in successfully",
            )
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    except Exception as error:
        print(f"Error occurred while logging in: {error}")
        raise HTTPException(status_code=500, detail=str(error))
