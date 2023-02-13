#!/usr/bin/python3
"""Defines unittests for basemodel"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing basemodel"""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        first = BaseModel()
        sec = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_diff_created_at(self):
        first = BaseModel()
        sleep(0.05)
        sec = BaseModel()
        self.assertLess(first.created_at, sec.created_at)

    def test_diff_updated_at(self):
        first = BaseModel()
        sleep(0.05)
        sec = BaseModel()
        self.assertLess(first.updated_at, sec.created_at)

    def test_str_rep(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)
