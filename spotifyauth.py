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