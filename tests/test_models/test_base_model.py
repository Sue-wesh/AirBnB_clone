#!/usr/bin/env python3
"""Defines unittests for BaseModel Class"""

import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittests for testing the BaseModel Class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models(self):
        first = BaseModel()
        secnd = BaseModel()
        self.assertNotEqual(first.id, secnd.id)

    def test_diff_creation(self):
        first = BaseModel()
        sleep(0.05)
        secnd = BaseModel()
        self.assertLess(first.created_at, secnd.created_at)

    def test_diff_updation(self):
        first = BaseModel()
        sleep(0.05)
        secnd = BaseModel()
        self.assertLess(first.updated_at, secnd.updated_at)
