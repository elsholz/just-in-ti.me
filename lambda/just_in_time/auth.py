from json import dumps
from auth0.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier

VERIFIER = None
AUTH0_DOMAIN = 'dev-twa5tnu1.eu.auth0.com'
API_AUDIENCE = 'https://just-in-ti.me/api'

jwks_url = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
issuer = f'https://{AUTH0_DOMAIN}/'

sv = AsymmetricSignatureVerifier(jwks_url)  # Reusable instance
VERIFIER = TokenVerifier(
    signature_verifier=sv, issuer=issuer, audience=API_AUDIENCE
)


class BadRequestError(Exception):
    pass


class InvalidTokenError(Exception):
    pass


def check_auth(evt):
    print('Entered check_auth function')
    headers = evt.get('headers', {})
    auth_header = headers.get(
        'Authorization',
        headers.get('authorization', None)
    )

    stage = evt.get('requestContext', {}).get('stage', None)
    print('Stage:', stage)

    if not auth_header or not isinstance(auth_header, str):
        raise BadRequestError('Missing auth header or in invalid format')

    try:
        token = auth_header.split(' ')[-1]
        try:
            verified = VERIFIER.verify(token)
        except Exception as e:
            raise InvalidTokenError('Error validating token')

        try:
            assert verified['aud'] == API_AUDIENCE
            assert 'sub' in verified
            assert isinstance(verified['sub'], str)
            assert all([x in '|@' or x.isalnum() for x in verified['sub']])
        except AssertionError as e:
            raise InvalidTokenError('Token missing sub or aud is incorrect')

        userid = verified['sub']

        return userid

    except Exception as e:
        print("Error in check_auth:", e)
        raise e
