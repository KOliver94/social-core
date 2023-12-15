import responses

from .oauth import OAuth2Test


class WLCGOAuth2Test(OAuth2Test):
    backend_path = "social_core.backends.wlcg.WLCGOAuth2"
    user_data_url = "https://wlcg.cloud.cnaf.infn.it/userinfo"
    expected_username = "foo@bar.com"
    access_token_body = {
        "access_token": "foobar",
        "token_type": "bearer",
    }
    user_data_body = {
        "email": "foo@bar.com",
        "family_name": "Bar",
        "given_name": "Foo",
        "name": "Foo Bar",
        "email_verified": True,
    }

    @responses.activate
    def test_login(self):
        self.do_login()

    @responses.activate
    def test_partial_pipeline(self):
        self.do_partial_pipeline()
