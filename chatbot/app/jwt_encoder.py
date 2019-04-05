import jwt

'''
Uses HS256 algorithm to encode tokens
Usage:
    When a timeslot is reserved by a user, a jwt.encode('uesr_id') 
    will be stored in the database of timeslot service.
    Thus other services don't need to decode the jwt token.
    
    If it's required to send some sensitive data between services,
    I believe it's better to use RS256(RSA) encryption.
    
    In that way, the private key is stored in this service, 
    and the public keys are assigned as env vars in the other two services,
    for them to decode the encrypted information.
'''
# dummy secret key here
key = 'secret'


def encode_user_id(user_id):
    payload = {'user_id': user_id}
    encoded = jwt.encode(payload, key, algorithm='HS256')
    return encoded