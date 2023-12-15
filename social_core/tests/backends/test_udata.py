from urllib.parse import urlencode

import responses

from .oauth import OAuth2Test


class DatagouvfrOAuth2Test(OAuth2Test):
    backend_path = "social_core.backends.udata.DatagouvfrOAuth2"
    user_data_url = "https://www.data.gouv.fr/api/1/me/"
    expected_username = "foobar"
    access_token_body = {
        "access_token": "foobar",
        "token_type": "bearer",
        "first_name": "foobar",
        "email": "foobar@example.com",
    }
    request_token_body = urlencode(
        {
            "oauth_token_secret": "foobar-secret",
            "oauth_token": "foobar",
            "oauth_callback_confirmed": "true",
        }
    )
    user_data_body = {}

    @responses.activate
    def test_login(self):
        self.do_login()

    @responses.activate
    def test_partial_pipeline(self):
        self.do_partial_pipeline()
