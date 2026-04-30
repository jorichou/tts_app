from utils.file_handler import FileHandler
from utils.text_processor import TextProcessor
from services.tts.voicevox_engine import VoiceVoxEngine

class AudioService:
    def __init__(self):
        self.tts_engine = VoiceVoxEngine()
        
    async def generate_audio(self, file):
            # 1. ファイル読み込み
            text = await FileHandler.read_text(file)
    
            # 2. テキスト整形
            text = TextProcessor.clean_text(text)
    
            # 3. 音声生成
            audio = await self.tts_engine.synthesize(text)
    
            return audio