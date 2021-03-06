from Crypto.Cipher import AES
from Crypto import Random
import base64
import random, string
import config
def generate_aes_key(length):
    alphanum = string.ascii_letters.replace("o","").replace("O","")+string.digits.replace("0","")
    return "".join([random.choice(alphanum) for i in range(length)])


def pad_key(key):
    return key[:16].ljust(16)


def decrypt_aes(payload,key):
    if config.DISABLE_ENCRYPTION:
        return payload
    padded_key = pad_key(key)
    iv = payload[:AES.block_size]
    payload= payload[AES.block_size:]
    cipher = AES.new(padded_key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(payload)
    return msg


def encrypt_aes(payload,key):
    if config.DISABLE_ENCRYPTION:
        return payload
    key = pad_key(key)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(payload)
    return msg


if __name__ == "__main__":
    payload = "{472ae34e-4a84-4e3b-94a1-77a2d7fe4238}"
    key ="1234567890"
    msg = encrypt_aes(payload,key)
    print base64.b64encode(msg)
    print [hex(ord(c)) for c in msg]
    print decrypt_aes(msg,key)