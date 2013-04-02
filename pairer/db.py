import filedict

class UserInformation(object):
    username = None
    public_key = None
    last_aes_key = None
    last_challenge = None
    last_login = None
    failed_attempts = None
    enabled = True

def load_db():
    return filedict.FileDict(filename="passwd.db")

def load_user_info(username):
    db = load_db()
    key = username+"_info"
    return db[key]

def save_user_info(info):
    db = load_db()
    username = info.username
    key = username+"_info"