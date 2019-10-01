import auth
import sys
import spotipy
import spotipy.util as util
import json

# remove after testing
from pprint import pprint

def migrate(source, dest):

  if len(sys.argv) > 1:
    username = sys.argv[1]
  else:
    # We need a username to auth
    print("Error: Username is required", username)
    sys.exit()

  data = fetch_source_data(source)
  # outcome = write_destination_data(data)


def fetch_source_data(username):
  read_scopes = ['playlist-read-private', 'user-library-read', 'user-follow-read']

  token = auth.retrieve_or_request_token(username, read_scopes)
  spot = spotipy.Spotify(auth=token)

  data = {}

  spot_source_user = spot.current_user()

  spot_playlists = spot.current_user_playlists().get('items')
  
  spot_user_playlists = []
  spot_followed_playlists = []

  for pl in spot_playlists:
    playlist_owner = pl.get('owner')

    if playlist_owner is None:
      print('Error:',pl.get('name'),'has no owner. Playlist has been skipped')
    elif playlist_owner.get('id') != spot_source_user.get('id'):
      spot_followed_playlists.append(pl)
    else:
      spot_user_playlists.append(pl)

  data['playlists'] = spot_user_playlists
  data['followed_playlist'] = spot_followed_playlists
  data['followed_artists'] = spot.current_user_followed_artists().get('artists').get('items')
  data['albums'] = spot.current_user_saved_albums().get('items')
  data['tracks'] = spot.current_user_saved_tracks().get('items')

  with open('data.json', 'w') as file:
    json.dump(data, file, indent=2)

def write_destination_data(username, data):
  write_scopes = ['playlist-modify-private', 'playlist-modify-public', 'user-library-modify']

  # Generate new playlists and add all the old playlists songs
  # user_playlist_create(user, name, public=True, description='')

  # Add all the followed playlists
  # user_playlist_add_tracks(user, playlist_id, tracks, position=None)

  # Add all the saved artists
  # user_follow_artists(ids=[])

  # Add all the saved albums
  # current_user_saved_albums_add(albums=[])

  # Add all the saved songs
  # current_user_saved_tracks_add(tracks=None)

  token = auth.retrieve_or_request_token(username, write_scopes)
  spot = spotipy.Spotify(auth=token)
  print(spot)
