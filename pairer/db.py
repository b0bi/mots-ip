import filedict
import config
import uuid

filedictdb = None

def generate_guid():
    return "{%s}"%str(uuid.uuid4())

class UserInformation(object):
    username = None
    aes_key = None
    last_challenge = None
    last_login = None
    failed_attempts = None
    enabled = True
    smartphone_guid = None
    mobile_factor = True
    password_factor = False

class PasswdDB(object):
    db = None
    dbfilename = "/etc/%s/passwd.db"%(config.PROJECT_NAME)
    def __init__(self):
        self.db= filedict.FileDict(filename=self.dbfilename)

    def load_user_info(self, username):
        key = username+"_info"
        if self.db.has_key(key):
            return self.db[key]
        else:
            new_record = UserInformation()
            new_record.username = username
            return new_record

    def save_user_info(self, info):
        username = info.username
        key = username+"_info"
        self.db[key] = info

    def get_server_guid(self):
        if not self.db.has_key("server_guid"):
            self.db["server_guid"] = generate_guid()
        return self.db["server_guid"]

if __name__=="__main__":
    print generate_guid()