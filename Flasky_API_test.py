#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 11:25:30 2021

"""

import requests
import string, random
from requests.auth import HTTPBasicAuth

''' Hyper-parameters '''
url_register = "http://localhost:8080/api/users"
url_login = "http://localhost:8080/api/auth/token"
headers = {"Content-Type":"application/json"}

''' Class '''
class Apitest():
    def __init__(self, url_register, url_login, headers):
        self.url_r = url_register
        self.url_lg = url_login
        self.headers = headers

    def random_user_generator(self, flag=0):
        if (flag == 0):
            self.username = ''.join(random.choices(
                string.ascii_letters + string.digits, k = random.randint(2, 9))) 
            self.password = ''.join(random.choices(
                string.ascii_letters + string.digits, k = random.randint(2, 9)))
        self.first_name = ''.join(random.choices(
            string.ascii_letters, k = random.randint(2, 5))) 
        self.last_name = ''.join(random.choices(
            string.ascii_letters, k = random.randint(2, 5))) 
        self.phone = ''.join(random.choices(
            string.digits, k = random.randint(6, 9))) 
        print("\n----random_user_generator----")
        print("Username:\t", self.username,
              "\nPassword:\t", self.password,
              "\nFirst name:\t", self.first_name,
              "\nLast name:\t", self.last_name,
              "\nPhone num:\t", self.phone
              )
        
    def register(self):
        self.random_user_generator()
        self.register_info={
                        "username":self.username, 
                        "password":self.password, 
                        "firstname":self.first_name,
                        "lastname":self.last_name,
                        "phone":self.phone
                        }
        self.response_register = requests.post(self.url_r, json=self. register_info)
        print("\n----------register-------------")
        print("Status:\t", self.response_register.json()["status"])
        print("Register message:\t", self.response_register.json()["message"])
        return self.username, self.password
        
    def get_user_info(self, username, password):
        response_login = requests.get(self.url_lg, auth=HTTPBasicAuth(username, password))
        self.token = response_login.json()["token"]
        self.headers["Token"] = self.token
        url = self.url_r + '/' + str(username)
        self.user_info = requests.get(url, headers=self.headers)
        print("\n--------get_user_info---------")
        print("Status: \t", self.user_info.json()["status"])
        print("User info: \t", self.user_info.json()["payload"])
        return self.user_info
        
    def review_users(self):
        self.response_review = requests.get(self.url_r)
        print("\n--------review registered users---------")
        print("Status: \t", self.response_review.json()["status"])
        print("\nThe registered user is: \n", self.response_review.json()["payload"])
        
    def update_info(self, username, password):
        self.get_user_info(username, password)
        self.random_user_generator(flag=1)
        new_user_info = {
                        "firstname": self.first_name,
                        "lastname": self.last_name,
                        "phone": self.phone,
                        }
        url_get_info = self.url_r + '/' + str(username)
        self.updated_info=requests.put(url_get_info, json=new_user_info, headers=self.headers)
        print("\nUpdate Status:\t", self.updated_info.json()["status"])

''' Main Function ''' 
def main():
    
    api_object = Apitest(url_register, url_login, headers) # Initialize an object to api class
    username, password = api_object.register()              # Register a user with random information
    user_info = api_object.get_user_info(username, password) #Get personal information
    api_object.update_info(username, password) #Update personal information
    api_object.get_user_info(username, password) # Check performation after update
    api_object.review_users() #Review registered users
    
    
if __name__ == "__main__":
    main()


