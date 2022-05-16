from fastapi import APIRouter, FastAPI, Form, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, validator

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], allow_credentials=True
)

router = APIRouter(prefix="/api", tags=["users"], responses={404: {"description": "Not Found"}})


class RegisterRequest(BaseModel):
    account: str
    password: str

    @validator("account")
    def check_account(cls, v):
        if len(v) < 6:
            raise ValidationError("Account must be at least 6 characters")
        return v

    @classmethod
    def as_form(cls, account: str = Form(...), password: int = Form(...)) -> "RegisterRequest":
        return cls(account=account, password=password)


@router.post("/register", response_model=RegisterRequest)
async def register(register: RegisterRequest = Depends(RegisterRequest.as_form)):
    return {"account": register.account, "password": register.password}


app.include_router(router)
