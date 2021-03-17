import spotipy
from spotipy.oauth2 import SpotifyOAuth
from env import credential

class SpotifyAuth():
    def __init__(self, scope="playlist-modify-private") -> None:
        self.client_id = credential.SPOTIFY_CLIENT_ID
        self.client_secret = credential.SPOTIFY_CLIENT_SECRET
        self.redirect_uri = 'http://example.com'
        self.scope = scope
        self.sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(
                                                        client_id=self.client_id, 
                                                        client_secret=self.client_secret, 
                                                        scope=self.scope, 
                                                        redirect_uri=self.redirect_uri, 
                                                        show_dialog=True, 
                                                        cache_path='token.txt'))
        self.user_id = self.sp_obj.current_user()['id']

    def get_song_uris(self, song_list:tuple, year:str) -> list:
        song_uris = []
        for song in song_list:
            result = self.sp_obj.search(q=f"track:{song} year:{year}", type="track")
            # print(result)
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        return song_uris

    def setup_playlist(self, song_uris:list, date:str) -> None:
        playlist = self.sp_obj.user_playlist_create(user=self.user_id, name=f"{date} Billboard 100", public=False)
        # print(playlist)
        self.sp_obj.playlist_add_items(playlist_id=playlist["id"], items=song_uris)