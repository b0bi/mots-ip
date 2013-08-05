#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      daniel
#
# Created:     06/08/2013
# Copyright:   (c) daniel 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import db
import network
import config
import safe

class LoginHandler(object):
    def __init__(self, username):
        self.username = username
        self.passwddb = db.PasswdDB()
        self.user_info = self.passwddb.load_user_info(username)

    def stage1(self):
        enc_msg = "REQUEST:"+self.user_info.smartphone_guid+":"+self.passwddb.get_server_guid()+":"+self.username
        msg = self.user_info.smartphone_guid + ":" + safe.encrypt_aes(enc_msg, self.user_info.aes_key)
        network.send_bcast(config.UDP_AUTH_PORT,msg)

    def stage2(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()
