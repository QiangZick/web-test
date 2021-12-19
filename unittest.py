#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 19:58:25 2021

"""
import unittest, os
from Flasky_API_test import Apitest
import HTMLTestRunner

''' Hyper-parameters '''
url_register = "http://localhost:8080/api/users"
url_login = "http://localhost:8080/api/auth/token"
headers = {"Content-Type":"application/json"}

class Testwebapi(unittest.TestCase):
    
    def test_register(self):
        """Register new user"""
        self.api_test = Apitest(url_register, url_login, headers)
        self.api_test.register()
        self.assertEqual(self.api_test.response_register.json()["status"], "SUCCESS")
        
    def test_review(self):
        """Review registered users"""
        self.api_test = Apitest(url_register, url_login, headers)
        self.api_test.review_users()
        self.assertEqual(self.api_test.response_review.json()["status"], "SUCCESS")
         
    def test_getinfo(self):
        """Get user information"""
        self.api_test = Apitest(url_register, url_login, headers)
        self.api_test.register()
        self.api_test.get_user_info(self.api_test.username, self.api_test.password)
        self.assertEqual(self.api_test.user_info.json()["status"], "SUCCESS")
        
    def test_updateinfo(self):
        """Update user information"""
        self.api_test = Apitest(url_register, url_login, headers)
        self.api_test.register()
        self.api_test.update_info(self.api_test.username, self.api_test.password)
        self.assertEqual(self.api_test.updated_info.json()["status"], "SUCCESS")
        
if __name__ == "__main__":
    file_path = os.path.join(os.getcwd() + '/report/' + 'Web_api_testreport.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='web_api_unittest', 
                                       description="This demonstrates the report output by HTMLTestRunner.")
    testunit = unittest.TestSuite()
    testunit .addTests(unittest.TestLoader().loadTestsFromTestCase(Testwebapi))
    runner.run(testunit)
    fp.close()
    
