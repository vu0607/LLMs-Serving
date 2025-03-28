import asyncio
from fastapi import FastAPI
from services.service import LMDeployService
from fastapi.responses import StreamingResponse
from typing import Optional
from configs.service_config import MAX_TOKENS

app = FastAPI()
service = LMDeployService(engine_type="turbomind", model_name="OpenGVLab/InternVL2_5-1B-MPO", model_format="hf", cache_max_entry_count=0.95)

@app.post("/generate")
async def generate(prompt: str, system_prompt: Optional[str] = None, max_tokens: int = MAX_TOKENS):
    async def response_stream():
        async for response in service.generate(prompt, system_prompt, max_tokens):
            yield response

    return StreamingResponse(response_stream(), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
