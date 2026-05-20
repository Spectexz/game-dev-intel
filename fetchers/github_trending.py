from bs4 import BeautifulSoup
import requests


git_url = "https://github.com/trending"
response = requests.get(git_url)
soup = BeautifulSoup(response.text, "html.parser")

repos = soup.find_all("article", class_="Box-row")

def get_trending_repos():
    result = []
    for repo in repos:        

        #get repos names
        a_tags = repo.find("h2", class_="h3 lh-condensed").find("a")
        repo_name = a_tags["href"]
        names = repo_name.replace("/","",1)
        
        #get programming language
        language_names = repo.find("span", itemprop="programmingLanguage") 
        language = language_names.get_text(strip=True) if language_names else None
        
        #get star
        list_stars = repo.find("span", class_="d-inline-block float-sm-right")
        star = list_stars.get_text(strip=True) if list_stars else None
        clean_stars = int(star.replace(' stars today', '').replace(',', '')) if star else None

        result.append({
            "repo_name": names,
            "language": language,
            "Stars": clean_stars
        })

    return result[:10]
    
get_trending_repos()