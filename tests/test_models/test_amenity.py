#!/usr/bin/python3
"""
Test Module: Amenity
test_base_model.py - unittests for 'Amenity'
"""
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    ''' 'Amenity Tests '''
    def test_amenity(self):
        ''' test 'Amenity' exists '''
        inst_1 = Amenity()
        self.assertTrue(inst_1)

    def test_amenity_instance_del(self):
        ''' test 'Amenity' deletes '''
        inst_1_1 = Amenity()
        del inst_1_1

    def test_amenity_instance(self):
        ''' test 'Amenity' instance '''
        inst_2 = Amenity()
        self.assertIsInstance(inst_2, Amenity)

    def test_amenity_save(self):
        ''' test 'Amenity' saves '''
        inst_3 = Amenity()
        updated_amenity = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_amenity, new_inst_3)

    def test_name_str(self):
        ''' test 'Amenity' type '''
        inst_4 = Amenity()
        self.assertIsInstance(inst_4.name, str)


if __name__ == '__main__':
    unittest.main()
