import logging
from google import genai
from google.genai import types

log = logging.getLogger(__name__)


class GeminiService:

    MODEL_NAME = "gemini-1.5-flash"

    def __init__(self, api_key: str) -> None:
        self.client = genai.Client(api_key=api_key)

        self.generation_config = types.GenerateContentConfig(
            temperature=0.7,
            max_output_tokens=2048,
        )

        log.info("GeminiService initialized with model '%s'", self.MODEL_NAME)

    async def generate_response(self, prompt: str) -> str:
        try:
            response = await self.client.aio.models.generate_content(
                model=self.MODEL_NAME,
                contents=prompt,
                config=self.generation_config,
            )
            return response.text or "⚠️ The model returned an empty response."

        except Exception as exc:
            log.error("Gemini API error: %s", exc, exc_info=True)
            return f"❌ **AI Error:** {exc}"
