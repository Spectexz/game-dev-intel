from fetchers.steam import get_top_seller_ids, get_game_detail
from fetchers.github_trending import get_trending_repos
from app.models import TrendingRepo
from app.models import GameSnapshot
from app.database import SessionLocal
from datetime import datetime, timezone, timedelta
from sqlalchemy.dialects.postgresql import insert

session = SessionLocal()
  
#### Get top selling games on steam
ids = get_top_seller_ids()
wib = timezone(timedelta(hours=7))
for id in ids:
    in_detail = get_game_detail(id)
    in_detail['last_updated'] = datetime.utcnow()
    game = insert(GameSnapshot).values(**in_detail)
    game = game.on_conflict_do_update(
        index_elements=['steam_appid'],
        set_=in_detail
    )
    session.execute(game)

#### Get trending repos on github and programming language
repos = get_trending_repos()
for repo in repos:
    repo['last_updated'] = datetime.utcnow()
    top_repo = insert(TrendingRepo).values(**repo)
    top_repo = top_repo.on_conflict_do_update(
        index_elements=['repo_name'],
        set_= repo
    )
    session.execute(top_repo)

session.commit()
session.close()

