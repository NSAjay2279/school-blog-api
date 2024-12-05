from pydantic import BaseModel


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    id: str
    title: str
    content: str
