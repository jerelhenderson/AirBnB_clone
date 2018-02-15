#!/usr/bin/python3
"""
Test Module: City
test_base_model.py - unittests for 'City'
"""
import unittest
from models.city import City


class test_city(unittest.TestCase):
    ''' 'City Tests '''
    def test_city(self):
        ''' test 'City' exists '''
        inst_1 = City()
        self.assertTrue(inst_1)

    def test_city_instance_del(self):
        ''' test 'City' deletes '''
        inst_1_1 = City()
        del inst_1_1

    def test_city_instance(self):
        ''' test 'City' instance '''
        inst_2 = City()
        self.assertIsInstance(inst_2, City)

    def test_city_save(self):
        ''' test 'City' saves '''
        inst_3 = City()
        updated_city = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_city, new_inst_3)

    def test_name_str(self):
        ''' test 'City' type '''
        inst_4 = City()
        self.assertIsInstance(inst_4.name, str)

    def test_state_id_str(self):
        ''' test 'City' type '''
        inst_5 = City()
        self.assertIsInstance(inst_5.state_id, str)

if __name__ == '__main__':
    unittest.main()
