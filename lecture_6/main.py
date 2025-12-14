from fastapi import FastAPI
import uvicorn

# FastAPI application instanc
app = FastAPI()

# Health check endpoint used by orchestration and monitoring systems
@app.get("/healthcheck")
async def healthcheck() -> dict:
    return {"status" : "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
