import unittest
from bitops import *

class TestBitcat( unittest.TestCase ):
	def test_single_num( self ):
		self.assertEqual( 1, bitcat( [1], [1]  ) )
		self.assertEqual( 5, bitcat( [5], [3]  ) )
		self.assertEqual( 5, bitcat( [5], [10] ) )
	
	def test_multi_num( self ):
		self.assertEqual( 0b1_10,        bitcat( [1,2],   [1,2]   ) )
		self.assertEqual( 0b1_10_11,     bitcat( [1,2,3], [1,2,2] ) )
		self.assertEqual( 0b001_010_011, bitcat( [1,2,3], [3,3,3] ) )
		
	def test_type_errors( self ):
		with self.assertRaises( TypeError ):
			bitcat( 1, [1] )             # first not list
		
		with self.assertRaises( TypeError ):
			bitcat( [1], 1 )             # second not list
		
		with self.assertRaises( TypeError ):
			bitcat( [1.0], [1] )         # num not int
		
		with self.assertRaises( TypeError ):
			bitcat( [1,2.0,3], [1,2,2] ) # any num location not int
		
		with self.assertRaises( TypeError ):
			bitcat( [1], [1.0] )         # bit not int
		
		with self.assertRaises( TypeError ):
			bitcat( [1,2,3], [1,2.0,2] ) # any bit location not int
		
	def test_value_errors( self ):
		with self.assertRaises( ValueError ):
			bitcat( [1], [1,2] )         # not same length
		
		with self.assertRaises( ValueError ):
			bitcat( [1,2], [1] )         # not same length

		with self.assertRaises( ValueError ):
			bitcat( [2], [1] )           # larger than n bits


class TestBitsplit( unittest.TestCase ):
	def test_single_num( self ):
		self.assertEqual( [1], bitsplit( 0b1,   [1] ) )
		self.assertEqual( [5], bitsplit( 0b101, [5] ) )
	
	def test_multi_num( self ):
		self.assertEqual( [1,2],   bitsplit( 0b1_10,        [1,2]   ) )
		self.assertEqual( [1,2,3], bitsplit( 0b001_010_011, [3,3,3] ) )
	
	def test_type_errors( self ):
		with self.assertRaises( TypeError ):
			bitsplit( 1.0, [1] )             # first not int
		
		with self.assertRaises( TypeError ):
			bitsplit( 1, 1 )                 # second not list
		
		with self.assertRaises( TypeError ):
			bitsplit( 1, [1.0] )             # bit not int
		
		with self.assertRaises( TypeError ):
			bitsplit( 0b1_10_11, [1,2.0,2] ) # any bit location not int


if __name__ == '__main__':
	unittest.main()
