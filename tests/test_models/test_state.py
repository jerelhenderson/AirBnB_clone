#!/usr/bin/python3
"""
Test Module: State
test_base_model.py - unittests for 'State'
"""
import unittest
from models.state import State


class test_state(unittest.TestCase):
    ''' 'State Tests '''
    def test_state(self):
        ''' test 'State' exists '''
        inst_1 = State()
        self.assertTrue(inst_1)

    def test_state_instance_del(self):
        ''' test 'State' deletes '''
        inst_1_1 = State()
        del inst_1_1

    def test_state_instance(self):
        ''' test 'State' instance '''
        inst_2 = State()
        self.assertIsInstance(inst_2, State)

    def test_state_save(self):
        ''' test 'State' saves '''
        inst_3 = State()
        updated_state = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_state, new_inst_3)

    def test_name_str(self):
        ''' test 'State' type '''
        inst_4 = State()
        self.assertIsInstance(inst_4.name, str)


if __name__ == '__main__':
    unittest.main()
