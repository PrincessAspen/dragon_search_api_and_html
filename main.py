import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from db import get_session
from models.dragons import Dragon

app = FastAPI()

origins = [
    'http://localhost',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

@app.get("/")
def root():
    return {"message" : "Hello World"}

@app.post("/create/dragon")
def create_dragon(name: str, color: str,  size: str, breath_weapon: str, source: str, summary: str, session: Session = Depends(get_session)):
    dragon = Dragon(name=name, color=color, size=size, breath_weapon=breath_weapon, source=source)
    session.add(dragon)
    session.commit()
    session.refresh(dragon)
    return {"dragon": dragon}

@app.get("/dragons")
def list_dragons(session: Session = Depends(get_session)):
    statement = select(Dragon)
    print(f"SQL STATEMENT: {statement}")
    results = session.exec(statement)
    return results.all()

@app.put("/update/dragon/{id}")
def update_dragon(id: int, name: str, color: str, size: str, breath_weapon: str, source: str, summary: str, session: Session = Depends(get_session)):
    dragon = session.get(Dragon, id)
    dragon.name = name
    dragon.color = color
    dragon.size = size
    dragon.breath_weapon = breath_weapon
    dragon.source = source
    dragon.summary = summary
    session.commit()
    session.refresh(dragon)
    return {"dragon": dragon}

@app.put("/delete/dragon/{id}")
def delete_dragon(id: int, session: Session = Depends(get_session)):
    dragon = session.get(Dragon, id)
    session.delete(dragon)
    session.commit()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

