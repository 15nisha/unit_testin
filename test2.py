from attr import resolve_types
import pytest
import  unittest
from flask import json
from s import palindro,rev,sorting


class TestSum(unittest.TestCase):
   

   def test_1(self):
      string=''
      result=palindro(string)
      self.assertEqual(result,True)
      print('test_1 succes')
      # working for null string too.


   def test_2(self):
      string = '@3nn3@'
      result=palindro(string)
      self.assertEqual(result,True)
      print('test_2 succes')
      # working for alphanumeric value
   
   def test_3(self):
      string = 'Nen'
      result=palindro(string)
      self.assertEqual(result,False)
      print('test_3 succes')
      # considering differently  to Uppercase and Lowercase of same char.
   

   def test_4(self):
      string = 'Never odd or even'
      result=palindro(string)
      self.assertEqual(result,False)
      print('test_4 succes')
      #also working  for  sentence but only in negative case.


   def test_5(self):
      # given string is palindrom without spaces
      string='do geese see god'
      result=palindro(string)
      # print(result)
      self.assertEqual(result,False)
      print('test_5 succes')
   # not recognising palindrom  for sentence bcz they are being affected by spaces.



#  testing for reverse function


   def test_6(self):
      string='kukku'
      result=rev(string)
      self.assertEqual(result,'ukkuk')
      print('test_6 succes')
      # working fine for a string

   def test_7(self):
      string='honesty is policy'
      result=rev(string)
      self.assertEqual(result,'ycilop si ytsenoh')
      print('test_7 succes')
   # considering the spaces while reversing


   def test_8(self):
      string=''
      result=rev(string)
      self.assertEqual(result,'')
      print('test_8 succes')
      # working for null string.
   

   # def test_9(self):
      # string=
      # result=rev(string)
      # self.assertEqual(result,'')
      # print('test_9 succes')


      # testing for sorting fuction.

   def test_10(self):
      string = ''
      result=sorting(string)
      self.assertEqual(result,'')
      print('test_10 succes')
      # working for null string
   
   def test_11(self):
      string = 'AaB'
      result=sorting(string)
      self.assertEqual(result,'ABa')
      print('test_11 succes')
      # uppercase are given lesser value than lowercase char.

   def test_12(self):
      string = 'all is well'
      result=sorting(string)
      self.assertEqual(result,'  aeillllsw')
      print('test_12 succes')
      # it is  considering spaces  and assignig least value while sorting

   def test_13(self):
      string = ' '
      result=sorting(string)
      self.assertEqual(result,' ')
      print('test_13 succes')
      # working  properly for null string 

   def test_14(self):
      string = '@124asd'
      result=sorting(string)
      self.assertEqual(result,'124@ads')
      print('test_14 succes')
      # working properly for alphanumeric strings.


   

if __name__=="__main__":
   unittest.main()


