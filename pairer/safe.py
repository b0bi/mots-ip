from Crypto.Cipher import AES
from Crypto import Random

def pad_key(key):
    return key[:32].ljust(32)


def decrypt_aes(payload,key):
    key = pad_key(key)
    iv = payload[:AES.block_size]
    payload= payload[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(payload)
    return msg


def encrypt_aes(payload,key):
    key = pad_key(key)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(payload)
    return msg


if __name__ == "__main__":
    payload = "the eagles land at dawn"
    key ="mykey123"
    msg = encrypt_aes(payload,key)
    print [hex(ord(c)) for c in msg]
    print decrypt_aes(msg,key)