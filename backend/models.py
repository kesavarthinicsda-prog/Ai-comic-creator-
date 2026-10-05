from pydantic import BaseModel


class ComicRequest(BaseModel):

    story_prompt: str

    character_name: str

    setting: str

    tone: str

    art_style: str

    panels: int = 4
