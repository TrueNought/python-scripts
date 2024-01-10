import instaloader
import os
from dotenv import load_dotenv

load_dotenv()

L = instaloader.Instaloader()

USERNAME = os.getenv('IG_USERNAME')
PASSWORD = os.getenv('IG_PASSWORD')
print(USERNAME)
print(PASSWORD)

L.login(USERNAME, PASSWORD)

profile = instaloader.Profile.from_username(L.context, USERNAME)

response = profile.get_followers()
result = [x.username for x in response]
print(result)
