from rocketapi import InstagramAPI
from rocketapi.exceptions import NotFoundException, BadResponseException

api = InstagramAPI(token="put your token here")

# Get user info by username
username = "kanyewest"
try:
    user = api.get_user_info(username)
    print(user)
except NotFoundException:
    print(f"User {username} not found")
except BadResponseException:
    print(f"Can't get {username} info from API")
