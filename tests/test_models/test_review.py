#!/usr/bin/python3
"""
Test Module: Review
test_base_model.py - unittests for 'Review'
"""
import unittest
from models.review import Review


class test_review(unittest.TestCase):
    ''' 'Review Tests '''
    def test_review(self):
        ''' test 'Review' exists '''
        inst_1 = Review()
        self.assertTrue(inst_1)

    def test_review_instance_del(self):
        ''' test 'Review' deletes '''
        inst_1_1 = Review()
        del inst_1_1

    def test_review_instance(self):
        ''' test 'Review' instance '''
        inst_2 = Review()
        self.assertIsInstance(inst_2, Review)

    def test_review_save(self):
        ''' test 'Review' saves '''
        inst_3 = Review()
        updated_review = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_review, new_inst_3)

    def test_place_id_str(self):
        ''' test 'Review' type '''
        inst_4 = Review()
        self.assertIsInstance(inst_4.place_id, str)

    def test_user_id_str(self):
        ''' test 'Review' type '''
        inst_5 = Review()
        self.assertIsInstance(inst_5.user_id, str)

    def test_text_str(self):
        ''' test 'Review' type '''
        inst_6 = Review()
        self.assertIsInstance(inst_6.text, str)


if __name__ == '__main__':
    unittest.main()
