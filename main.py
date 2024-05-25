from fastapi import FastAPI

app = FastAPI()


@app.get('/v1/health_check/')
async def check_health():
    return {"message": "Hello World"}
