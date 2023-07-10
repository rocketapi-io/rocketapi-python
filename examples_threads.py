from rocketapi import ThreadsAPI
from rocketapi.exceptions import NotFoundException, BadResponseException

api = ThreadsAPI(token="put your token here")

# Get user feed by id
user_id = 35670846775
try:
    user = api.get_user_feed(user_id)
    print(user)
except NotFoundException:
    print(f"User {user_id} not found")
except BadResponseException:
    print(f"Can't get {user_id} feed from API")
