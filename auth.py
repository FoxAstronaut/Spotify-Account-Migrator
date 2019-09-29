import sys
import spotipy.util as util

def retrieve_or_request_token(username, scopes):
  token = util.prompt_for_user_token(username, ' '.join(scopes))

  if token:
    print("Token retrieved for", username, "for the scopes of", ','.join(scopes))
    return token
  else:
    print("Error: Can't get token for", username)
    sys.exit()