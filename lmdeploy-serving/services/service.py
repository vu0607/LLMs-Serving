import uuid
from typing import AsyncGenerator, Optional
from typing_extensions import Annotated
from annotated_types import Ge, Le
from configs.service_config import SYSTEM_PROMPT, PROMPT_TEMPLATE, MAX_TOKENS
from factories.engine_config_factory import EngineConfigFactory
from lmdeploy.serve.async_engine import AsyncEngine
from lmdeploy import GenerationConfig

class LMDeployService:
    def __init__(self, engine_type: str, model_name: str, model_format: str, cache_max_entry_count: float) -> None:
        config = EngineConfigFactory.get_engine_config(engine_type, model_name, model_format, cache_max_entry_count).get_config()
        self.engine = AsyncEngine(model_name, backend_config=config)

    async def generate(
        self,
        prompt: str = "Explain superconductors in plain English",
        system_prompt: Optional[str] = SYSTEM_PROMPT,
        max_tokens: Annotated[int, Ge(128), Le(MAX_TOKENS)] = MAX_TOKENS,
    ) -> AsyncGenerator[str, None]:
        
        gen_config = GenerationConfig(max_new_tokens=max_tokens)

        if system_prompt is None:
            system_prompt = SYSTEM_PROMPT
        prompt = PROMPT_TEMPLATE.format(user_prompt=prompt, system_prompt=system_prompt)

        session_id = abs(uuid.uuid4().int >> 96)
        stream = self.engine.generate(
            prompt, session_id=session_id, gen_config=gen_config
        )

        async for request_output in stream:
            yield request_output.response
