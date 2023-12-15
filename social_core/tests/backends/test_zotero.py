from urllib.parse import urlencode

import responses

from .oauth import OAuth1Test


class ZoteroOAuth1Test(OAuth1Test):
    backend_path = "social_core.backends.zotero.ZoteroOAuth"
    expected_username = "FooBar"
    access_token_body = urlencode(
        {
            "oauth_token": "foobar",
            "oauth_token_secret": "rodgsNDK4hLJU1504Atk131G",
            "userID": "123456_abcdef",
            "username": "FooBar",
        }
    )
    request_token_body = urlencode(
        {
            "oauth_token_secret": "foobar-secret",
            "oauth_token": "foobar",
            "oauth_callback_confirmed": "true",
        }
    )

    @responses.activate
    def test_login(self):
        self.do_login()

    @responses.activate
    def test_partial_pipeline(self):
        self.do_partial_pipeline()
