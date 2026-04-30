from fastapi import APIRouter, UploadFile, File, Response
from services.audio_service import AudioService

router = APIRouter()
audio_service = AudioService()

@router.post("/synthesize")
async def synthesize(file: UploadFile = File(...)):
    audio_bytes = await audio_service.generate_audio(file)
    return Response(content=audio_bytes, media_type="audio/wav")
