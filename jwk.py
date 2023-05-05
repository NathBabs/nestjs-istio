"""
This script generates RSA public/private key pair using python.
And uses the Keys to Generate JWT Token.
The series of steps are listed below
1. Generate the Key
2. Generate the Public and Private Keys
3. Generate the Token using the Private Key from step 2
4. Validate the JWT Token using the Public key from step 2
"""


# ______________________________ Step 0 ______________________________________
# import python_jwt
import python_jwt as jwt, jwcrypto.jwk as jwk, datetime

# ______________________________ Step 1 ______________________________________
# ______________________________ GENERATE KEY ______________________________________
# Generate the keys.
# The private key will be used to Generate the Token
# The 2048-bit is about the RSA key pair: 
# RSA keys are mathematical objects which include a big integer, and a "2048-bit key" is a key such that 
# the big integer is larger than 2^2047 but smaller than 2^2048.
key = jwk.JWK.generate(kty='RSA', size=2048)

# Define payload
# payload that the server will send back the client encoded in the JWT Token
# While generating a token, you can define any type of payload in valid JSON format
# the iss(issuer), sub(subject) and aud(audience) are reserved claims. https://tools.ietf.org/html/rfc7519#section-4.1
# These reserved claims are not mandatory to define in a standard JWT token.
# But when working with Istio, it's better you define these.

payload = {
    'iss':'seamless', 
    'sub':'SUBJECT', 
    'aud':'AUDIENCE', 
    'roles': 'USER',
    'permission': 'read' 
}

# ______________________________ Step 2 ______________________________________
# ______________________________ GENERATE PUBLIC AND PRIVATE KEY ______________________________________
# Export the private and public key

private_key = key.export_private()
public_key = key.export_public()


# ______________________________ Step 3 ______________________________________
# ______________________________ GENERATE JWT TOKEN ______________________________________
# Generate the JWT Tokes using the Private Key
# Provide the payload and the Private Key. RS256 is the Hash used and last value is the expiration time.
# You can set the expiration time according to your need.
# To generate JWT Token, you need the private key as a JWK object
token = jwt.generate_jwt(payload, jwk.JWK.from_json(private_key), 'RS256', datetime.timedelta(minutes=40320))



# Print the public key, private key and the token
print("\n_________________PUBLIC___________________\n")
print(public_key)
print("\n_________________PRIVATE___________________\n")
print(private_key)
print("\n_________________TOKEN___________________\n")
print(token)




# ______________________________ Step 4 ______________________________________
# ______________________________ VALIDATE JWT TOKEN USING PUBLIC KEY ______________________________________


# To validate JWT Token, you need the public key as a JWK object
header, claims = jwt.verify_jwt(token, jwk.JWK.from_json(public_key), ['RS256'])

print("\n_________________TOKEN INFO___________________\n")
print(header)
print(claims)
