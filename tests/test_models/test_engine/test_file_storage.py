 #!/usr/bin/python3
'''
Module: File Storage Test
file_storage.py - FileStorageDocs tests
'''
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class test_file_storage(unittest.TestCase):
    ''' FileStorage Tests '''
    def test_file_storage_instance(self):
        ''' test instance exists '''
        inst_1 = FileStorage()
        self.assertTrue(inst_1)

    def test_all(self):
        ''' test console method 'all' '''
        inst_2 = FileStorage()
        all_inst_2 = inst_2.all()
        self.assertTrue(type(all_inst_2) is dict)
 
    def test_new(self):
        ''' test console method 'new' '''
        inst_3 = BaseModel()
        inst_3_1 = FileStorage()
        inst_3_1.new(inst_3)
        inst_3_str = "{}.{}".format(inst_3.__class__.__name__, inst_3.id)
        inst_3_dict = inst_3_1.all()
        self.assertIn(inst_3_str, inst_3_dict)
