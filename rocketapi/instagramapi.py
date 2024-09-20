from rocketapi.exceptions import NotFoundException, BadResponseException
from rocketapi.rocketapi import RocketAPI


class InstagramAPI(RocketAPI):
    def __init__(self, token, max_timeout=30):
        """
        Instagram API client.

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
                raise BadResponseException(
                    f"Bad response from Instagram ({method}: {response['response']['status_code']})"
                )
        raise BadResponseException(f"Bad response from RocketAPI ({method})")

    def search(self, query):
        """
        Search for a specific user, hashtag or place.

        As of September 2024, we no longer recommend using this method, as it now only returns a maximum of 5 users and leaves the places and hashtags arrays empty. Instead, please use the separate methods:
        - `search_users`
        - `search_hashtags`
        - `search_locations`
        - `search_audios`

        Args:
            query (str): The search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/search
        """
        return self.request("instagram/search", {"query": query})

    def get_user_info(self, username):
        """
        Retrieve user information by username.

        Args:
            username (str): Username

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_info
        """
        return self.request("instagram/user/get_info", {"username": username})

    def get_user_info_by_id(self, user_id):
        """
        Retrieve user information by id.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_info_by_id
        """
        return self.request("instagram/user/get_info_by_id", {"id": user_id})

    def get_user_media(self, user_id, count=12, max_id=None):
        """
        Retrieve user media by id.

        Args:
            user_id (int): User id
            count (int): Number of media to retrieve (max: 12)
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_media
        """
        payload = {"id": user_id, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_media", payload)

    def get_user_clips(self, user_id, count=12, max_id=None):
        """
        Retrieve user clips (videos from "Reels" section) by id.

        Args:
            user_id (int): User id
            count (int): Number of media to retrieve (max: 50)
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `max_id` (!) field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_clips
        """
        payload = {"id": user_id, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_clips", payload)

    def get_user_guides(self, user_id, max_id=None):
        """
        Retrieve user guides by id.

        Args:
            user_id (int): User id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_guides
        """
        payload = {"id": user_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_guides", payload)

    def get_user_tags(self, user_id, count=12, max_id=None):
        """
        Retrieve user tags by id.

        Args:
            user_id (int): User id
            count (int): Number of media to retrieve (max: 50)
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through the media (take from the `end_cursor` (!) field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_tags
        """
        payload = {"id": user_id, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_tags", payload)

    def get_user_following(self, user_id, count=12, max_id=None):
        """
        Retrieve user following by user id.

        Args:
            user_id (int): User id
            count (int): Number of users to return (max: 200)
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through following (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_following
        """
        payload = {"id": user_id, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_following", payload)

    def search_user_following(self, user_id, query):
        """
        Search user following by user id.

        Args:
            user_id (int): User id
            query (str): Search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_following
        """
        return self.request(
            "instagram/user/get_following", {"id": user_id, "query": query}
        )

    def get_user_followers(self, user_id, count=12, max_id=None):
        """
        Retrieve user followers by user id.

        Args:
            user_id (int): User id
            count (int): Number of users to return (max: 50)
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through followers (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_followers
        """
        payload = {"id": user_id, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/user/get_followers", payload)

    def search_user_followers(self, user_id, query):
        """
        Search user followers by user id.

        Args:
            user_id (int): User id
            query (str): Search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_followers
        """
        return self.request(
            "instagram/user/get_followers", {"id": user_id, "query": query}
        )

    def get_user_stories_bulk(self, user_ids):
        """
        Retrieve user(s) stories by user id(s).
        You can retrieve up to 4 user ids per request.

        Args:
            user_ids (list): List of user ids

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_stories
        """
        return self.request("instagram/user/get_stories", {"ids": user_ids})

    def get_user_stories(self, user_id):
        """
        Retrieve user stories by user id.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_stories
        """
        return self.get_user_stories_bulk([user_id])

    def get_user_highlights(self, user_id):
        """
        Retrieve user highlights by user id.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_highlights
        """
        return self.request("instagram/user/get_highlights", {"id": user_id})

    def get_user_live(self, user_id):
        """
        Retrieve user live broadcast by id.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_live
        """
        return self.request("instagram/user/get_live", {"id": user_id})

    def get_user_similar_accounts(self, user_id):
        """
        Lookup for user similar accounts by id. Typically, up to 80 accounts will be returned.

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_similar_accounts
        """
        return self.request("instagram/user/get_similar_accounts", {"id": user_id})

    def get_media_info(self, media_id):
        """
        Retrieve media information by media id.

        Args:
            media_id (int): Media id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_info
        """
        return self.request("instagram/media/get_info", {"id": media_id})

    def get_media_info_by_shortcode(self, shortcode):
        """
        Retrieve media information by media shortcode. This method provides the same information as the `get_media_info`.

        Args:
            shortcode (str): Media shortcode

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_info_by_shortcode
        """
        return self.request(
            "instagram/media/get_info_by_shortcode", {"shortcode": shortcode}
        )

    def get_media_likes(self, shortcode, count=12, max_id=None):
        """
        Retrieve up to 1000 media likes by media shortcode.

        Args:
            shortcode (str): Media shortcode
            count (int): Not supported right now
            max_id (str): Not supported right now

        Pagination is not supported for this endpoint.

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_likes
        """
        payload = {"shortcode": shortcode, "count": count}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/media/get_likes", payload)

    def get_media_comments(self, media_id, can_support_threading=True, min_id=None):
        """
        Retrieve media comments by media id.

        Args:
            media_id (int): Media id
            can_support_threading (bool): Set `False` if you want chronological order
            min_id (str): Use for pagination

        You can use the `min_id` parameter to paginate through comments (take from the `next_min_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_comments
        """
        payload = {"id": media_id, "can_support_threading": can_support_threading}
        if min_id is not None:
            payload["min_id"] = min_id
        return self.request("instagram/media/get_comments", payload)

    def get_media_shortcode_by_id(self, media_id):
        """
        Get media shortcode by media id. This endpoint is provided free of charge.

        Args:
            media_id (int): Media id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_shortcode_by_id
        """
        return self.request("instagram/media/get_shortcode_by_id", {"id": media_id})

    def get_media_id_by_shortcode(self, shortcode):
        """
        Get media id by media shortcode. This endpoint is provided free of charge.

        Args:
            shortcode (str): Media shortcode

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/media/get_id_by_shortcode
        """
        return self.request(
            "instagram/media/get_id_by_shortcode", {"shortcode": shortcode}
        )

    def get_guide_info(self, guide_id):
        """
        Retrieve guide information by guide id.

        Args:
            guide_id (int): Guide id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/guide/get_info
        """
        return self.request("instagram/guide/get_info", {"id": guide_id})

    def get_location_info(self, location_id):
        """
        Retrieve location information by location id.

        Args:
            location_id (int): Location id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/location/get_info
        """
        return self.request("instagram/location/get_info", {"id": location_id})

    def get_location_media(self, location_id, page=None, max_id=None):
        """
        Retrieve location media by location id.

        Args:
            location_id (int): Location id
            page (int): Page number
            max_id (str): Use for pagination

        In order to use pagination, you need to use both the `max_id` and `page` parameters. You can obtain these values from the response's `next_page` and `next_max_id` fields.

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/location/get_media
        """
        payload = {"id": location_id}
        if page is not None:
            payload["page"] = page
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/location/get_media", payload)

    def get_hashtag_info(self, name):
        """
        Retrieve hashtag information by hashtag name.

        Args:
            name (str): Hashtag name

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/hashtag/get_info
        """
        return self.request("instagram/hashtag/get_info", {"name": name})

    def get_hashtag_media(self, name, page=None, max_id=None):
        """
        Retrieve hashtag media by hashtag name.

        Args:
            name (str): Hashtag name
            page (int): Page number
            max_id (str): Use for pagination

        In order to use pagination, you need to use both the `max_id` and `page` parameters. You can obtain these values from the response's `next_page` and `next_max_id` fields.

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/hashtag/get_media
        """
        payload = {"name": name}
        if page is not None:
            payload["page"] = page
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/hashtag/get_media", payload)

    def get_highlight_stories_bulk(self, highlight_ids):
        """
        Retrieve highlight(s) stories by highlight id(s).

        Args:
            highlight_ids (list): Highlight id(s)

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/highlight/get_stories
        """
        return self.request("instagram/highlight/get_stories", {"ids": highlight_ids})

    def get_highlight_stories(self, highlight_id):
        """
        Retrieve highlight stories by highlight id.

        Args:
            highlight_id (int): Highlight id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/highlight/get_stories
        """
        return self.get_highlight_stories_bulk([highlight_id])

    def get_comment_likes(self, comment_id, max_id=None):
        """
        Retrieve comment likes by comment id.

        Args:
            comment_id (int): Comment id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through likes (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/comment/get_likes
        """
        payload = {"id": comment_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/comment/get_likes", payload)

    def get_comment_replies(self, comment_id, media_id, max_id=None):
        """
        Retrieve comment replies by comment id and media id.

        Args:
            comment_id (int): Comment id
            media_id (int): Media id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through replies (take from the `next_max_child_cursor` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/comment/get_replies
        """
        payload = {"id": comment_id, "media_id": media_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/comment/get_replies", payload)

    def get_audio_media(self, audio_id, max_id=None):
        """
        Retrieve audio media by audio id.

        Args:
            audio_id (int): Audio id
            max_id (str): Use for pagination

        You can use the `max_id` parameter to paginate through media (take from the `next_max_id` field of the response).

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/audio/get_media
        """
        payload = {"id": audio_id}
        if max_id is not None:
            payload["max_id"] = max_id
        return self.request("instagram/audio/get_media", payload)

    def get_user_about(self, user_id):
        """
        Obtain user details from «About this Account» section.

        ⭐️ This method is exclusively available to our Enterprise+ clients.
        If you wish to enable it for your account, please get in touch with our support team: https://t.me/rocketapi

        Args:
            user_id (int): User id

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/get_about
        """
        return self.request("instagram/user/get_about", {"id": user_id})

    def search_users(self, query):
        """
        Search for a specific user (max 50 results)

        Args:
            query (str): The search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/user/search
        """
        return self.request("instagram/user/search", {"query": query})

    def search_hashtags(self, query):
        """
        Search for a specific hashtag (max 20 results)

        Args:
            query (str): The search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/hashtag/search
        """
        return self.request("instagram/hashtag/search", {"query": query})

    def search_locations(self, query):
        """
        Search for a specific location (max 20 results)

        Args:
            query (str): The search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/location/search
        """
        return self.request("instagram/location/search", {"query": query})

    def search_audios(self, query):
        """
        Search for a specific audio (max 10 results)

        Args:
            query (str): The search query

        For more information, see documentation: https://docs.rocketapi.io/api/instagram/audio/search
        """
        return self.request("instagram/audio/search", {"query": query})
