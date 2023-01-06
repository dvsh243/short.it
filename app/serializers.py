from pydantic import BaseModel

class CreateSerializer(BaseModel):
    longurl: str = "https://www.google.com"