import hashlib
import base64
from Crypto.PublicKey import RSA

# Load public key
pubkey_str = """-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJcINDJ8k5+dCh5AHbg0vimO0cT6GV10
w/NKurLCOmiQEkvEq455IJo5P2TktoXm/w6nwMq+CSjILhwG6mA4QUMCAwEAAQ==
-----END PUBLIC KEY-----"""
pubkey = RSA.import_key(pubkey_str)

# Encode messagegit 
message = b"sp@innovatio.lv"
hash_object = hashlib.sha256(message)
hash_value = int.from_bytes(hash_object.digest(), byteorder='big')
encoded = pow(hash_value, pubkey.e, pubkey.n)

# Print encoded message
print(encoded)