class FileHandler:
    @staticmethod
    async def read_text(file):
        content = await file.read()
        return content.decode("utf-8")