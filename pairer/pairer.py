#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      daniel
#
# Created:     09/04/2013
# Copyright:   (c) daniel 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import safe
import db
import config
import threading
import network

class stage2_fetcher(threading.Thread):
    def __init__(self, shared_dict):
        self.shared_dict = shared_dict
        threading.Thread.__init__(self)
    def run(self):
        response = network.recv_bcast(config.UDP_PAIRING_PORT)
        #CONTINUE HERE
        self.shared_dict["done"


class Pairer(object):
    def __init__(self, username):
        #Open the passwd file and user record.
        self.passwddb = db.PasswdDB()
        self.user_info = self.passwddb.load_user_info(username)

    def stage1(self): #Generate the AES key and print it.
        self.user_info.aes_key = safe.generate_aes_key(config.AES_KEY_LENGTH)
        print "Pairing key for smartphone with %s: %s"%(self.user_info.username,self.user_info.aes_key)

    def stage2(self):


if __name__=="__main__":
    username = raw_input("Enter username to pair: ")
    pairer = Pairer(username)
    pairer.stage1()

