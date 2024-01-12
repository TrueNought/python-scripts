import instaloader
import os
from dotenv import load_dotenv

load_dotenv()

L = instaloader.Instaloader()

USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')

session = f'{USERNAME}.session'

if os.path.exists(session):
  L.load_session_from_file(USERNAME, session)
else:
  L.login(USERNAME, PASSWORD)
  L.save_session_to_file(session)

profile = instaloader.Profile.from_username(L.context, USERNAME)

followers = {x.username for x in profile.get_followers()}
following = {x.username for x in profile.get_followees() if not x.is_verified}

print(following.difference(followers))