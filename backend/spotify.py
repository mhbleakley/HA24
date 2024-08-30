import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

class Spotify:
    def __init__(self, name, destination_folder, client_id, client_secret):
        self.name = name
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_manager = SpotifyClientCredentials()
        self.scope = ['ugc-image-upload', 'user-read-playback-state', 'user-read-currently-playing']
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.destination_folder = destination_folder

    def get_playback(self):
        print('updating spotify playback')
        results = self.sp.current_playback()

        song_name = results['item']['name']
        progress_ms = results['progress_ms']
        images = results['item']['album']['images']
        image_url = self.get_largest_image_url(images)

        album = results['item']['album']['name']
        artists = []
        for artist in results['item']['artists']:
            artists.append(artist['name'])
        duration_ms = results['item']['duration_ms']

        song_dest = self.destination_folder + '/data/'

        if not os.path.exists(song_dest):
            os.mkdir(song_dest)
        
        with open(song_dest + self.name + '_spotify.txt', 'w') as f:
            html = self.write_song_html(song_name, artists, album, image_url, progress_ms, duration_ms)
            f.write(html)
            f.close()

    def get_largest_image_url(self, images):
        largest = 0
        largest_index = None
        for i, image in enumerate(images):
            h  = image['height']
            if h > largest:
                largest = h
                largest_index = i
        return images[largest_index]['url']

    def write_song_html(self, name, artists, album, image_url, progress_ms, duration_ms):
        artists_str = artists[0]
        if len(artists) > 1:
            artists_str = ''
            for artist in artists:
                artists_str += artist
        html = f'<div class="song">\n\
        <img class="album_cover" src="{image_url}" alt="album cover" height="200">\n\
        <h3>{name}</h3>\n\
        <h5>{artists_str}</h5>\n\
        <progress value="{progress_ms}" max="{duration_ms}"></progress>\n\
        </div>'
        return html