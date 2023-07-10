from rocketapi.exceptions import NotFoundException, BadResponseException
from rocketapi.rocketapi import RocketAPI


class ThreadsAPI(RocketAPI):
    def __init__(self, token, max_timeout=30):
        """
        Threads API client.

        Args:
            token (str): Your RocketAPI token (https://rocketapi.io/dashboard/)
            max_timeout (int): Maximum timeout for requests. Please, don't use values lower than 15 seconds, it may cause problems with API.

        For debugging purposes you can use the following variables:
            last_response (dict): contains the last response from the API.
            counter (int): contains the number of requests made in the current session.

        For more information, see documentation: https://docs.rocketapi.io/api/
        """
        self.last_response = None
        self.counter = 0
        super().__init__(token, max_timeout=max_timeout)

    def request(self, method, data):
        response = super().request(method, data)
        self.last_response = response
        self.counter += 1
        if response["status"] == "done":
            if (
                response["response"]["status_code"] == 200
                and response["response"]["content_type"] == "application/json"
            ):
                return response["response"]["body"]
            elif response["response"]["status_code"] == 404:
                raise NotFoundException("Instagram resource not found")
            else:
                raise BadResponseException("Bad response from Threads")
        raise BadResponseException("Bad response from RocketAPI")

    def search_users(self, query):
        """
        Search for a specific user in Threads

        Args:
            query (str): Username to search for

        For more information, see documentation: https://docs.rocketapi.io/api/threads/search_users
        """
        return self.request("threads/search_users", {"query": query})

    def get_user_info(self, user_id):
        """
        Retrieve Threads user information by id.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_info
        """
        return self.request("threads/user/get_info", {"id": user_id})

    def get_user_feed(self, user_id, max_id=None):
        """
        Retrieve Threads user feed by id.

        Args:
            user_id (int): User id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_feed
        """
        payload = {"id": user_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("threads/user/get_feed", payload)

    def get_user_replies(self, user_id, max_id=None):
        """
        Retrieve Threads user replies by id.

        Args:
            user_id (int): User id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_replies
        """
        payload = {"id": user_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("threads/user/get_replies", payload)

    def get_user_followers(self, user_id, max_id=None):
        """
        Retrieve Threads user followers by id.

        Args:
            user_id (int): User id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through followers (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_followers
        """
        payload = {"id": user_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("threads/user/get_followers", payload)

    def search_user_followers(self, user_id, query):
        """
        Search Threads user followers by user id.

        Args:
            user_id (int): User id
            query (str): Search query

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_followers
        """
        return self.request(
            "threads/user/get_followers", {"id": user_id, "query": query}
        )

    def get_user_following(self, user_id, max_id=None):
        """
        Retrieve Threads user following by id.

        Args:
            user_id (int): User id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through followers (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_following
        """
        payload = {"id": user_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("threads/user/get_following", payload)

    def search_user_following(self, user_id, query):
        """
        Search Threads user following by user id.

        Args:
            user_id (int): User id
            query (str): Search query

        For more information, see documentation: https://docs.rocketapi.io/api/threads/user/get_following
        """
        return self.request(
            "threads/user/get_following", {"id": user_id, "query": query}
        )

    def get_thread_replies(self, thread_id, max_id=None):
        """
        Retrieve thread replies by id.

        Args:
            thread_id (int): Thread id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `paging_tokens["downwards"]` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/threads/thread/get_replies
        """
        payload = {"id": thread_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("threads/thread/get_replies", payload)

    def get_thread_likes(self, thread_id):
        """
        Retrieve thread likes by id.

        Args:
            thread_id (int): Thread id

        For more information, see documentation: https://docs.rocketapi.io/api/threads/thread/get_likes
        """
        payload = {"id": thread_id}
        return self.request("threads/thread/get_likes", payload)
