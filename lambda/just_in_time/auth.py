from json import dumps


def check_auth(evt):
    print('Call to check auth')
    print('evt:', evt)
    try:
        print(dumps(evt, indent=4))
    except:
        pass
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
