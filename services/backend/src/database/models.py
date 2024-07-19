from sqlmodel import SQLModel, Field


class SongBase(SQLModel):
    name: str
    artist: str

class Song(SongBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)

class SongCreate(SongBase):
    pass

class SongPublic(SongBase):
    id: int

class SongUpdate(SQLModel):
    name: str | None = None
    artist: str | None = None
