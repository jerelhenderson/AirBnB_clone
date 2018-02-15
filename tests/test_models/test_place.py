#!/usr/bin/python3
"""
Test Module: Place
test_base_model.py - unittests for 'Place'
"""
import unittest
from models.place import Place


class test_place(unittest.TestCase):
    ''' 'Place Tests '''
    def test_place(self):
        ''' test 'Place' exists '''
        inst_1 = Place()
        self.assertTrue(inst_1)

    def test_place_instance_del(self):
        ''' test 'Place' deletes '''
        inst_1_1 = Place()
        del inst_1_1

    def test_place_instance(self):
        ''' test 'Place' instance '''
        inst_2 = Place()
        self.assertIsInstance(inst_2, Place)

    def test_place_save(self):
        ''' test 'Place' saves '''
        inst_3 = Place()
        updated_place = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_place, new_inst_3)

    def test_name_str(self):
        ''' test 'Place' type '''
        inst_4 = Place()
        self.assertIsInstance(inst_4.name, str)

    def test_city_id_str(self):
        ''' test 'Place' type '''
        inst_5 = Place()
        self.assertIsInstance(inst_5.city_id, str)

    def test_user_id_str(self):
        ''' test 'Place' type '''
        inst_5 = Place()
        self.assertIsInstance(inst_5.user_id, str)

    def test_description_str(self):
        ''' test 'Place' type '''
        inst_6 = Place()
        self.assertIsInstance(inst_6.description, str)

    def test_number_rooms_int(self):
        ''' test 'Place' type '''
        inst_7 = Place()
        self.assertIsInstance(inst_7.number_rooms, int)

    def test_number_bathrooms_int(self):
        ''' test 'Place' type '''
        inst_8 = Place()
        self.assertIsInstance(inst_8.number_bathrooms, int)

    def test_max_guest_int(self):
        ''' test 'Place' type '''
        inst_9 = Place()
        self.assertIsInstance(inst_9.max_guest, int)

    def test_price_by_night_int(self):
        ''' test 'Place' type '''
        inst_10 = Place()
        self.assertIsInstance(inst_10.price_by_night, int)

    def test_latitude_flt(self):
        ''' test 'Place' type '''
        inst_11 = Place()
        self.assertIsInstance(inst_11.latitude, float)

    def test_longitude_flt(self):
        ''' test 'Place' type '''
        inst_12 = Place()
        self.assertIsInstance(inst_12.longitude, float)

    def test_amenity_ids_lst(self):
        ''' test 'Place' type '''
        inst_13 = Place()
        self.assertIsInstance(inst_13.amenity_ids, list)

if __name__ == '__main__':
    unittest.main()
