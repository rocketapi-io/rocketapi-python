from rocketapi.exceptions import NotFoundException, BadResponseException
from rocketapi.rocketapi import RocketAPI


class InstagramAPI(RocketAPI):
    def __init__(self, token, threads=1):
        super().__init__(token, threads=1)

    def request(self, method, data):
        response = super().request(method, data)
        if response['status'] == 'done':
            if response['response']['status_code'] == 200 and response['response']['content_type'] == 'application/json':
                return response['response']['body']
            elif response['response']['status_code'] == 404:
                raise NotFoundException('Instagram resource not found')
            else:
                raise BadResponseException('Bad response from Instagram')
        raise BadResponseException('Bad response from RocketAPI')

    def search(self, query):
        return self.request('instagram/search', {'query': query})

    def get_user_info(self, username):
        return self.request('instagram/user/get_info', {'username': username})

    def get_user_info_by_id(self, user_id):
        return self.request('instagram/user/get_info_by_id', {'id': user_id})

    def get_user_media(self, user_id, count=12, max_id=None):
        payload = {'id': user_id, 'count': count}
        if max_id is not None:
            payload['max_id'] = max_id
        return self.request('instagram/user/get_media', payload)

    def get_user_following(self, user_id, count=12, max_id=None):
        payload = {'id': user_id, 'count': count}
        if max_id is not None:
            payload['max_id'] = max_id
        return self.request('instagram/user/get_following', payload)

    def search_user_following(self, user_id, query):
        return self.request('instagram/user/get_following', {'id': user_id, 'query': query})

    def get_user_followers(self, user_id, count=12, max_id=None):
        payload = {'id': user_id, 'count': count}
        if max_id is not None:
            payload['max_id'] = max_id
        return self.request('instagram/user/get_followers', payload)

    def search_user_followers(self, user_id, query):
        return self.request('instagram/user/get_followers', {'id': user_id, 'query': query})

    def get_user_stories_bulk(self, user_ids):
        return self.request('instagram/user/get_stories', {'ids': user_ids})

    def get_user_stories(self, user_id):
        return self.get_user_stories_bulk([user_id])

    def get_media_info(self, media_id):
        return self.request('instagram/media/get_info', {'id': media_id})

    def get_media_likes(self, shortcode, count=12, max_id=None):
        payload = {'shortcode': shortcode, 'count': count}
        if max_id is not None:
            payload['max_id'] = max_id
        return self.request('instagram/media/get_likes', payload)

    def get_media_comments(self, media_id, can_support_threading=True, min_id=None):
        payload = {'id': media_id, 'can_support_threading': can_support_threading}
        if min_id is not None:
            payload['min_id'] = min_id
        return self.request('instagram/media/get_comments', payload)

    def get_comment_likes(self, comment_id, max_id=None):
        payload = {'id': comment_id}
        if max_id is not None:
            payload['max_id'] = max_id
        return self.request('instagram/comment/get_likes', payload)
