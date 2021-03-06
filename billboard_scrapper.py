from datetime import date
from config import config
import requests
from bs4 import BeautifulSoup

def get_billboard_url_for_date(user_date:date = None) -> str:
    billboard_date_url = config.billboard_url
    if user_date:
        billboard_date_url = config.billboard_url+str(user_date)
    return billboard_date_url

def get_url_response_text(url:str) -> str:
    response = requests.get(url)
    url_extract = BeautifulSoup(response.text, 'html.parser')
    return url_extract

def get_top_100_dict(url_extract:str, **kwargs) -> dict:
    songs_extract = url_extract.find_all(**kwargs)
    song_titles = [song.getText().strip() for song in songs_extract]
    return dict(enumerate(song_titles, 1))

# def main() -> None:
#     user_date = get_user_date()
#     billboard_url = get_billboard_url_for_date(user_date)
#     url_extract = get_url_response_text(billboard_url)
#     top_100_dict = get_top_100_dict(url_extract, name='h3', class_="a-no-trucate")
#     print(top_100_dict)

# if __name__ == '__main__':
#     main()

