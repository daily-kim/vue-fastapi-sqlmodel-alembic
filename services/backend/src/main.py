from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from sqlmodel import select
from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession

from src.database.db import get_session, init_db
from src.database.models import Song, SongCreate, SongUpdate, SongPublic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello, World!"



@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song

@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]

@app.get("/song/{id}", response_model=SongPublic)
async def get_song(id: int, session: AsyncSession = Depends(get_session)):
    song = await session.get(Song, id)
    return song

#update song
@app.patch("/song/{id}",response_model=SongPublic)
async def update_song(id: int, song: SongUpdate, session: AsyncSession = Depends(get_session)):
    db_song = await session.get(Song, id)
    if db_song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    song_data = song.model_dump(exclude_unset=True)
    db_song.sqlmodel_update(song_data)
    await session.commit()
    await session.refresh(db_song)
    return db_song

# delete song
@app.delete("/song/{id}")
async def delete_song(id: int, session: AsyncSession = Depends(get_session)):
    song = await session.get(Song, id)
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    await session.delete(song)
    await session.commit()
    return {"ok": True}

