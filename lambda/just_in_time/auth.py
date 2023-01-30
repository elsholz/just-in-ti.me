from json import dumps
from auth0.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier


def check_auth(evt):
    print('Entered check_auth function')
    headers = evt.get('headers', {})
    auth_header = headers.get(
        'Authorization',
        headers.get('authorization', None)
    )

    stage = evt.get('requestContext', {}).get('stage', None)
    print('Stage:', stage)

    if auth_header:
        print('Auth Header provided:', auth_header)
    else:
        print('No Auth Header provided')

    try:
        AUTH0_DOMAIN = 'dev-twa5tnu1.eu.auth0.com'
        API_AUDIENCE = 'https://just-in-ti.me/api'

        jwks_url = f'https://{AUTH0_DOMAIN}/.well-known/jwks.json'
        issuer = f'https://{AUTH0_DOMAIN}/'

        token = auth_header.split(' ')[-1]

        sv = AsymmetricSignatureVerifier(jwks_url)  # Reusable instance
        tv = TokenVerifier(
            signature_verifier=sv, issuer=issuer, audience=API_AUDIENCE
        )
        print('Token verify:', tv.verify(token))
    except Exception as e:
        print("Error occured:", e)

    return 'test123'
