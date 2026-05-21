from fastapi import FastAPI, Request
from app.models import GameSnapshot, TrendingRepo
from app.database import SessionLocal
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/games")
def topgames():
    session = SessionLocal()
    games = session.query(GameSnapshot).all()
    session.close()
    return games


@app.get("/repos")
def toprepos():
    session = SessionLocal()
    repos = session.query(TrendingRepo).all()
    session.close()
    return repos

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    session = SessionLocal()
    games = session.query(GameSnapshot).order_by(GameSnapshot.last_updated.desc()).limit(10).all()
    repos = session.query(TrendingRepo).order_by(TrendingRepo.last_updated.desc()).limit(10).all()
    session.close()
    return templates.TemplateResponse("index.html",
        {
            "request": request,
            "games": games,
            "repos": repos
        })
