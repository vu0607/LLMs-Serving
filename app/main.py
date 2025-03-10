from fastapi import FastAPI, HTTPException
import openai
import os
import uvicorn

app = FastAPI()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(prompt: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            api_key=OPENAI_API_KEY
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )