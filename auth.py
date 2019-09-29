import sys
import spotipy.util as util

def retrieve_or_request_token(username, scope):
  token = util.prompt_for_user_token(username, scope)

  if token:
    print("Token retrieved for", username)
    return token
  else:
    print("Error: Can't get token for", username)
    sys.exit()