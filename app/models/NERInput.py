from pydantic import BaseModel


class NERInput(BaseModel):
    text: str