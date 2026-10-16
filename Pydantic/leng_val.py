from pydantic import BaseModel, field_validator
from langdetect import detect

class NewsInput(BaseModel):
    text: str

    @field_validator("text")
    @classmethod
    def validate_english(cls, value):

        language = detect(value)

        if language != "en":
            raise ValueError("Only English news text is allowed")

        return value


news = NewsInput(
    text="smjh mein aya kya"
)

print(news)