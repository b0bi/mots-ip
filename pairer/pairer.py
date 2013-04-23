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


class Pairer(object):
    def __init__(self, username):
        #Open the passwd file and user record.
        self.passwddb = db.PasswdDB()
        self.user_info = self.passwddb.load_user_info(username)

    def stage1(self): #Generate the AES key and print it.
        self.user_info.aes_key = safe.generate_aes_key(config.AES_KEY_LENGTH)
        print "Pairing key for smartphone with %s: %s"%(self.user_info.username,self.user_info.aes_key)

    def stage2(self):
        s2_success = False
        while not s2_success:
            s2_buffer = network.recv_bcast(config.UDP_PAIRING_PORT)
            #decode and see if it matches



if __name__=="__main__":
    username = raw_input("Enter username to pair: ")
    pairer = Pairer(username)
    pairer.stage1()

