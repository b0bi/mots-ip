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
import getpass

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)

    return reduce(lambda x,y:x+y, lst)

class Pairer(object):
    def __init__(self, username):
        #Open the passwd file and user record.
        self.passwddb = db.PasswdDB()
        self.user_info = self.passwddb.load_user_info(username)
        self.candidate_smartphone_guid = None

    def stage1(self): #Generate the AES key and print it.
        self.user_info.aes_key = safe.generate_aes_key(config.AES_KEY_LENGTH)
        print "Pairing key for smartphone with %s: %s"%(self.user_info.username,self.user_info.aes_key)

    def stage2(self):
        s2_success = False
        while not s2_success:
            s2_buffer = network.recv_bcast(config.UDP_PAIRING_PORT)[0]
            #decode and see if it matches
            print "Buffer Received: "+toHex(s2_buffer)
            try:
                smartphone_guid = s2_buffer.split("#")[0]
                print "Declared GUID: "+smartphone_guid
                try:
                    decrypted_part = safe.decrypt_aes(s2_buffer.split("#")[1], self.user_info.aes_key)
                    assert decrypted_part
                except:
                    print "Could not decrypt payload"
                print "Decrypted into: "+decrypted_part
                if decrypted_part == smartphone_guid:
                    self.candidate_smartphone_guid = smartphone_guid
                    s2_success = True
            except IndexError: #No hash in the string...
                print "Invalid buffer format received."

    def stage3(self):
        server_guid = db.PasswdDB.get_server_guid()
        encrypted_server_guid = safe.encrypt_aes(server_guid,self.user_info.aes_key)
        network.send_bcast(config.UDP_PAIRING_PORT, server_guid+"$"+encrypted_server_guid)

    def stage4(self):





if __name__=="__main__":
    try:
        username = getpass.getuser()
        print "Running username: "+getpass.getuser()
        if username == "root": #Allow root to pair other users.
            username = raw_input("Enter username to pair: ")
        pairer = Pairer(username)
        pairer.stage1()
        print "Waiting for the smartphone..."
        pairer.stage2()
        pairer.stage3()

    except KeyboardInterrupt:
        print "User aborted the process"
