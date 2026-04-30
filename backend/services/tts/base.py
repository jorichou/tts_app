from abc import ABC, abstractmethod

class TTSEngine(ABC):
    @abstractmethod
    async def synthesize(self, text: str) -> bytes:
        pass