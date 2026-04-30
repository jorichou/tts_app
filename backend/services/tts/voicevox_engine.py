import httpx
from services.tts.base import TTSEngine

VOEICEVOX_URL = "http://localhost:50021" # voicevox_engineのURL

class VoiceVoxEngine(TTSEngine):
    async def synthesize(self, text: str) -> bytes:
        async with httpx.AsyncClient() as client:
            # audio_query
            query_res = await client.post(
                f"{VOEICEVOX_URL}/audio_query",
                params={"text": text, "speaker": 1}
            )
            query = query_res.json()
            
            # synthesis
            synth_res = await client.post(
                f"{VOEICEVOX_URL}/synthesis",
                params={"speaker": 1},
                json=query
            )
            
            return synth_res.content
