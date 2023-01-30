from json import dumps
from auth0.authentication.token_verifier import TokenVerifier, AsymmetricSignatureVerifier

domain = 'myaccount.auth0.com'
client_id = 'exampleid'

# After authenticating
id_token = auth_result['id_token']

jwks_url = 'https://{}/.well-known/jwks.json'.format(domain)
issuer = 'https://{}/'.format(domain)

sv = AsymmetricSignatureVerifier(jwks_url)  # Reusable instance
tv = TokenVerifier(signature_verifier=sv, issuer=issuer, audience=client_id)
tv.verify(id_token)


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

    return 'test123'

# from six.moves.urllib.request import urlopen
# from functools import wraps
#
# from jose import jwt
#
#
# AUTH0_DOMAIN = 'dev-twa5tnu1.eu.auth0.com'
# API_AUDIENCE = 'https://just-in-ti.me/api'
# ALGORITHMS = ["RS256"]
#
#
# def check_auth(evt):
#     token = evt.get('Authorization', ' ').split(' ')[1]
#     if not token:
#         return
#
#     jsonurl = urlopen(
#         "https://dev-twa5tnu1.eu.auth0.com/.well-known/jwks.json")
#     jwks = json.loads(jsonurl.read())
#     unverified_header = jwt.get_unverified_header(token)
#     rsa_key = {}
#     for key in jwks["keys"]:
#         if key["kid"] == unverified_header["kid"]:
#             rsa_key = {
#                 "kty": key["kty"],
#                 "kid": key["kid"],
#                 "use": key["use"],
#                 "n": key["n"],
#                 "e": key["e"]
#             }
#     if rsa_key:
#         try:
#             payload = jwt.decode(
#                 token,
#                 rsa_key,
#                 algorithms=ALGORITHMS,
#                 audience=API_AUDIENCE,
#                 issuer="https://dev-twa5tnu1.eu.auth0.com/"
#             )
#         except jwt.ExpiredSignatureError:
#             print({"code": "token_expired",
#                    "description": "token is expired"}, 401)
#         except jwt.JWTClaimsError:
#             print({"code": "invalid_claims",
#                    "description":
#                    "incorrect claims,"
#                    "please check the audience and issuer"}, 401)
#         except Exception:
#             print({"code": "invalid_header",
#                    "description":
#                    "Unable to parse authentication"
#                    " token."}, 401)
#         print(payload)
