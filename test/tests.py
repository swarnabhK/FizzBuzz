import sys
import unittest

# adding fizzbuzz to the system path
sys.path.append("c:\\Users\\swarn\\OneDrive\\Desktop\\Interview_prep2\\FizzBuzz\\FizzBuzz\\src")

from fizzbuzz import fizzbuzz
class FizzBuzzTests(unittest.TestCase):
  def test_n_is_1(self):
    self.assertEqual(fizzbuzz(1),[1])
  def test_n_is_3(self):
    self.assertEqual(fizzbuzz(3),[1,2,'Fizz'])
  def test_n_is_5(self):
    self.assertEqual(fizzbuzz(5),[1,2,'Fizz',4,'Buzz'])
  def test_n_is_15(self):
    self.assertEqual(fizzbuzz(15),[1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz'])


if __name__ == '__main__':
    unittest.main()
