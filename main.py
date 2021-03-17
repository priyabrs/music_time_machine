from billboard_scrapper import ( get_billboard_url_for_date, get_url_response_text, get_top_100_dict )
from spotifyauth import SpotifyAuth
from datetime import date
from config import config

class DateException(Exception):
    pass

def get_user_date() -> date:
    user_date = input('what year you would like to travel to? Please enter the date(YYYY-MM-DD): ')
    if user_date:
        try:
            date_list = [int(value) for value in user_date.split('-')]
            user_date = date(date_list[0], date_list[1], date_list[2])
        except Exception as ex:
            raise DateException('Entered date format is wrong!!!. Please enter date in correct format(YYYY-MM-DD)')
    return user_date

def main() -> None:
    sp = SpotifyAuth()
    user_date = get_user_date()
    # print(user_date.year)
    billboard_url = get_billboard_url_for_date(user_date)
    url_extract = get_url_response_text(billboard_url)
    top_100_dict = get_top_100_dict(url_extract, name=config.billboard_tag_name, class_=config.billboard_class)
    song_uris = sp.get_song_uris(top_100_dict.values(), user_date.year)
    sp.setup_playlist(song_uris,str(user_date))

if __name__ == '__main__':
    main()