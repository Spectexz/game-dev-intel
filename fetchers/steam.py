import requests
from dotenv import load_dotenv

load_dotenv()

steam_url= 'https://store.steampowered.com/api/featuredcategories'

def get_top_seller_ids():
    response = requests.get(steam_url)
    data = response.json()    
    items = data.get("top_sellers", {}).get("items", [])
    seen = set()
    ids = []

    for item in items:
        if item['type'] == 0 and item['id'] not in seen:
            seen.add(item['id'])
            ids.append(item['id'])

    return ids[:10]

def get_game_detail(app_id):
    appdetail_url = f"https://store.steampowered.com/api/appdetails?appids={app_id}"
    detail_response = requests.get(appdetail_url)
    data_detail = detail_response.json()
    app_data = data_detail.get(str(app_id), {}).get("data", {})
    list_description = app_data.get("genres", [])
    all_desc = ', '.join([g['description'] for g in list_description])
    devs = app_data.get("developers", [])
    return {
        "steam_appid": app_data.get("steam_appid"),
        "name": app_data.get("name"),
        "short_desc": app_data.get("short_description"),
        "header_image": app_data.get("header_image"),
        "genres": all_desc,
        "recommendations": app_data.get("recommendations", {}).get("total"),
        "release_date": app_data.get("release_date", {}).get("date"),
        "is_free": app_data.get("is_free"),
        "devs": devs[0] if devs else None,
        "metacritic_score": app_data.get("metacritic", {}).get("score")
    }


ids = get_top_seller_ids()
for id in ids:
    in_detail = get_game_detail(id)
    print(in_detail)
        