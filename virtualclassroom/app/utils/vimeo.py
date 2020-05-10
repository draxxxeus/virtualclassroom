import vimeo
from .config import Config

creds = Config().creds.vimeo


class Vimeo:

    def __init__(self):
        self.client = vimeo.VimeoClient(
            token=creds.private_upload_token,
            key=creds.client_id,
            secret=creds.client_secret)
        # embed settings are set via embed presets on vimeo settings UI


    def test(self, uri='/tutorial'):
        response = self.client.get(uri)
        print(response.json())

    def patch(self, uri, settings):
        """
        # settings description can be seen here: https://developer.vimeo.com/api/reference/videos#edit_video
        example settings:

        :param uri: str eg: /videos/1234567
        :param settings: dict eg:
        {
            'privacy': {
                'embed': 'public',
                'comments': 'nobody',
                'download': False,
                'view': 'anybody'
            }
        }
        :return:
        """

        self.client.patch(uri, data=self.video_settings)

    def upload(self, file_path: str, name: str = 'testname', description: str = 'destdescription'):

        settings = dict(name=name, description=description)
        uri = self.client.upload(file_path, data=settings)

        response = self.client.get(uri + '?fields=link').json()
        return response['link']


if __name__ == '__main__':
    v = Vimeo()
    v.test()
    v.upload('/Users/rshaw/Movies/test_movie.mp4')