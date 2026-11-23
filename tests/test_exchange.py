"""核对交换资料的字段和数值关系。"""
import json
from pathlib import Path
import unittest

import numpy as np


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "data" / "exchange.json"
        self.data = json.loads(source.read_text(encoding="utf-8"))

    def test_exchange_data(self):
        self.assertEqual({row[2] for row in self.data['tile_views']}, {-1, 1})
        self.assertEqual(set(self.data['tide'][0]['wet']) - set(self.data['tide'][1]['wet']), {'we'})
        self.assertNotEqual(self.data['coarse'], self.data['tide'][2]['coarse'])
