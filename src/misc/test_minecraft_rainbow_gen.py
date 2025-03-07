from unittest import TestCase

from minecraft_rainbow_gen import rainbow_generator


class test_rainbow_generator(TestCase):
    def setUp(self):
        self.gen = rainbow_generator()


class test_column_generator(test_rainbow_generator):
    def test_one_half(self):
        self.assertEqual(self.gen.generate_column(1, 2), [True, False])

    def test_eight_sixteenths(self):
        self.assertEqual(self.gen.generate_column(8, 16), [True, False])

    def test_five_eighths(self):
        self.assertEqual(self.gen.generate_column(5, 8), [True, False, True, False])


class test_pattern_generator(test_rainbow_generator):
    def test_height_one(self):
        self.assertEqual(self.gen.generate_pattern(1), [['A']])

    def test_height_three(self):
        self.assertEqual(self.gen.generate_pattern(3), [['A', 'G', 'G'], ['A', 'B', 'A'], ['A', 'B', 'G'], ['A', 'B', 'B']])
