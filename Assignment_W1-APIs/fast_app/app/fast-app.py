from fastapi import FastAPI, Request
import uvicorn
from bmi import bmi

# instantiate FastAPI
app = FastAPI()

@app.get('/')
async def bmi_api(request:Request):
    params = await request.json()

    return bmi(params["weight"], params["height"])

if __name__ == "__main__":
    uvicorn.run()
