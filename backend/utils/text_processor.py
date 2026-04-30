class TextProcessor:
    @staticmethod
    def clean_text(text: str) -> str:
        # MVP: 最低限の整形
        return text.strip()