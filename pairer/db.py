import filedict
import config

filedictdb = None

class UserInformation(object):
    username = None
    public_key = None
    last_aes_key = None
    last_challenge = None
    last_login = None
    failed_attempts = None
    enabled = True

class PasswdDB(object):
    db = None
    dbfilename = "/etc/%s/passwd.db"%(config.PROJECT_NAME)
    def __init__(self):

        self.db= filedict.FileDict(filename=dbfilename)

    def load_user_info(self, username):
        db = load_db()
        key = username+"_info"
        return db[key]

    def save_user_info(self, info):
        username = info.username
        key = username+"_info"
        self.db[key] = info

    def store_public_key(self, key):
        self.db["local_public_key"] = key

    def load_public_key(self, key):
        return self.db["local_public_key"]

    def store_private_key(self, key):
        self.db["local_private_key"] = key

    def load_private_key(self, key):
        return self.db["local_private_key"]