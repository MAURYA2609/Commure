from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["health"])


class EchoRequest(BaseModel):
    message: str


class EchoResponse(BaseModel):
    message: str
    length: int


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/hello")
def hello(name: str = "world") -> dict[str, str]:
    return {"message": f"Hello, {name}! The backend is connected."}


@router.post("/echo")
def echo(payload: EchoRequest) -> EchoResponse:
    text = payload.message.strip()
    if not text:
        raise HTTPException(status_code=400, detail="message must not be blank")
    return EchoResponse(message=text, length=len(text))
