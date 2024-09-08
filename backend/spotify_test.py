import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

mb_spotify_id = os.environ.get('MB_SPOTIPY_CLIENT_ID')
mb_spotify_secret = os.environ.get('MB_SPOTIPY_CLIENT_SECRET')
mb_spotify_redirect_uri = os.environ.get('MB_SPOTIPY_REDIRECT_URI')

scope = "user-library-read"

# auth_manager = SpotifyOAuth(scope=scope,
#                         client_id=mb_spotify_id,
#                         client_secret=mb_spotify_secret,
#                         redirect_uri=mb_spotify_redirect_uri,
#                         show_dialog=True,
#                         open_browser=False
#                         )


auth_manager = SpotifyClientCredentials(client_id=mb_spotify_id,
                                        client_secret=mb_spotify_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.current_user_saved_tracks()

print(results['href'])