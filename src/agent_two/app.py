from fastapi import FastAPI

from agent_two.config import settings

app = FastAPI()
app.state.settings = settings


@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "hello"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
