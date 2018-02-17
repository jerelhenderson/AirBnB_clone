#!/usr/bin/python3
"""
Test Module: BaseModel
test_base_model.py - unittests for 'BaseModel'
"""
import unittest
# import pep8
from models.base_model import BaseModel
from datetime import datetime


"""
Output Information provided by Guillaume
---------------------------------------------------------------
my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))
---------------------------------------------------------------
"""


# class TestCodeFormat(unittest.TestCase):
#    def test_pep8_conformance(self):
#        ''' test pep8 style '''
#        pep8style = pep8.StyleGuide(quiet=True)
#        result = pep8style.check_files(['models/base_model.py'])
#        self.assertEqual(result.total_errors, 0, "Found style errors.")

class test_base_model(unittest.TestCase):
    """ Class 'BaseModel' tests """
    def test_model_instance(self):
        ''' test instance exists '''
        inst_1 = BaseModel()
        self.assertTrue(inst_1)

    def test_model_id(self):
        ''' test instance id exists '''
        inst_2 = BaseModel(2)
        self.assertTrue(inst_2.id, 2)

    def test_created_at(self):
        ''' test datetime creation '''
        inst_3 = BaseModel()
        self.assertEqual(datetime, type(inst_3.created_at))

    def test_updated_at(self):
        ''' test datetime update '''
        inst_4 = BaseModel()
        self.assertEqual(datetime, type(inst_4.updated_at))

    def test_save_created_at(self):
        ''' test save of 'updated_at' only to datetime '''
        inst_6 = BaseModel()
        created_datetime = inst_6.created_at
        inst_6.save()
        self.assertEqual(created_datetime, inst_6.created_at)

    def test_save_updated_at(self):
        ''' test save of 'updated_at' does not match datetime '''
        inst_6_1 = BaseModel()
        updated_datetime = inst_6_1.updated_at
        inst_6_1.save()
        self.assertNotEqual(updated_datetime, inst_6_1.updated_at)

    def test_class_instance(self):
        ''' test class exists '''
        inst_7 = BaseModel()
        self.assertEqual((inst_7.__class__), BaseModel)

    def test_to_dict_instance(self):
        ''' test to_dict exists '''
        inst_8 = BaseModel()
        self.assertTrue(inst_8.to_dict())

    def test_to_dict_dict(self):
        ''' test to_dict converts to dict '''
        inst_9 = BaseModel()
        inst_9_dict = inst_9.to_dict()
        self.assertEqual(dict, type(inst_9_dict))

    def test_to_dict_id(self):
        ''' test if 'id' is dict '''
        inst_10 = BaseModel()
        inst_10_dict = inst_10.to_dict()
        self.assertIn('id', inst_10_dict)

    def test_--str--_id(self):
        ''' test magic method '''
        inst_11 = BaseModel()
        inst_11_name = inst_11.__class__.__name__
        inst_11_id = inst_11.id
        inst_11_dict = inst_11.__dict__
        self.assertTrue(inst_11.name, str)
        self.assertTrue(inst_11.id, str)
        self.assertTrue(inst_11.__dict__, dict)

if __name__ == '__main__':
    unittest.main()
