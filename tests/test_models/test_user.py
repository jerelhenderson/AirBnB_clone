#!/usr/bin/python3
"""
Test Module: User
test_base_model.py - unittests for 'User'
"""
import unittest
from models.user import User


class test_user(unittest.TestCase):
    ''' 'User Tests '''
    def test_user(self):
        ''' test 'User' exists '''
        inst_1 = User()
        self.assertTrue(inst_1)

    def test_user_instance_del(self):
        ''' test 'User' deletes '''
        inst_1_1 = User()
        del inst_1_1

    def test_user_instance(self):
        ''' test 'User' instance '''
        inst_2 = User()
        self.assertIsInstance(inst_2, User)

    def test_user_save(self):
        ''' test 'User' saves '''
        inst_3 = User()
        updated_user = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_user, new_inst_3)

    def test_email_str(self):
        ''' test 'User' type '''
        inst_4 = User()
        self.assertIsInstance(inst_4.email, str)

    def test_password_str(self):
        ''' test 'User' type '''
        inst_5 = User()
        self.assertIsInstance(inst_5.password, str)

    def test_first_name_str(self):
        ''' test 'User' type '''
        inst_6 = User()
        self.assertIsInstance(inst_6.first_name, str)

    def test_last_name_str(self):
        ''' test 'User' type '''
        inst_7 = User()
        self.assertIsInstance(inst_7.last_name, str)


if __name__ == '__main__':
    unittest.main()
