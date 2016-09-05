"""
Created on Sat Jan 23 13:06:36 2016
Modified on Tue Apr 12 15:08:45 2016
Original Author: Kivanc Yazan, Ryan Compton
Modified: Andrei Ignat

Update 1: April 17, 2016 14:50. Empty-one element tests are now numpy arrays.
Update 2: April 18, 2016 17:35. Test array has integers only now.

How do you test?
================

1) Copy this file to the folder where you saved hw2.py, rename this file to "hw2test.py"
2) Just run this on terminal (you can also click green button in Spyder)

    python3 hw2test.py

3) If the output is similar to

    ----------------------------------------------------------------------
    Ran 5 tests in 0.008s

    OK

   this means that you are good to go. If not, look at the error messages and
   at the way we run the tests in order to figure out what might be wrong
   with your code.

4) Note that the file check will fail until you have created all the neccessary
files for submission.

5) Once you are done with all of this, don't forget to submit!

May the odds be ever in your favor!
"""
import hw2 as solution
import numpy as np
import os.path 
import unittest

class Homework2Test(unittest.TestCase):
    def setUp(self):
        """ set up the neccessary variables and generate the array"""
        # look for the functions
        self.selectionsort = solution.selectionsort
        self.insertionsort = solution.insertionsort
        self.mergesort = solution.mergesort

        # generate an array to be sorted
        self.array = np.random.randint(-10,500,25)
        self.sorted_array = np.sort(self.array)

    def test_files(self):
        """ test to see if you have all the needed files """
        self.assertTrue(os.path.isfile("../partners.txt"),
                        msg="Cannot find file  partners.txt in root.")

        # Files for problem 2
        self.assertTrue(os.path.isfile("selection.pdf"),
                        msg="Cannot find file  selection.pdf for Question 2.")
        self.assertTrue(os.path.isfile("insertion.pdf"),
                        msg="Cannot find file  insertion.pdf for Question 2.")
        self.assertTrue(os.path.isfile("merge.pdf"),
                        msg="Cannot find file  merge.pdf for Question 2.")
        self.assertTrue(os.path.isfile("all-sorted.pdf"),
                        msg="Cannot find file  all-sorted.pdf for Question 2.")
        self.assertTrue(os.path.isfile("all-unsorted.pdf"),
                        msg="Cannot find file  all-unsorted.pdf for Question 2.")

        # Files for problem 3
        self.assertTrue(os.path.isfile("explanation.txt"),
                        msg="Cannot find file  explanation.txt for Question 3.")

        # Files for problem 4
        self.assertTrue(os.path.isfile("average.pdf"),
                        msg="Cannot find file  average.pdf for Question 4.")
        self.assertTrue(os.path.isfile("average-explanation.txt"),
                        msg="Cannot find file  average-explanation.txt for Question 4.")

        # Files for problem 5
        self.assertTrue(os.path.isfile("large-input.txt"),
                        msg="Cannot find file  large-input.txt for Question 5.")

    def test_goodimplementation(self):
        """ test to see if you can sort an empty array """
        self.assertTrue(np.array_equal(np.array([]), self.selectionsort(np.array([]))),
                        msg="Your Selection Sort implementation cannot "
                            "handle empty arrays")
        self.assertTrue(np.array_equal(np.array([]), self.insertionsort(np.array([]))),
                        msg="Your Insertion Sort implementation cannot "
                            "handle empty arrays")
        self.assertTrue(np.array_equal(np.array([]), self.mergesort(np.array([]))),
                        msg="Your Merge Sort implementation cannot "
                            "handle empty arrays")

    def test_singleelement(self):
        """ test to see if you can sort a single element array """
        self.assertTrue(np.array_equal(np.array([0]), self.selectionsort(np.array([0]))),
                        msg="Your Selection Sort implementation cannot "
                            "handle single element arrays")
        self.assertTrue(np.array_equal(np.array([0]), self.insertionsort(np.array([0]))),
                        msg="Your Insertion Sort implementation cannot "
                            "handle single element arrays")
        self.assertTrue(np.array_equal(np.array([0]), self.mergesort(np.array([0]))),
                        msg="Your Merge Sort implementation cannot "
                            "handle single element arrays")

    def test_selectionsort(self):
        """ test to see if you are sorting correctly """
        selectionsorted = self.selectionsort(self.array)
        self.assertTrue(np.array_equal(selectionsorted, self.sorted_array),
                        msg="Your Selection Sort method is not running properly")

    def test_insertionsort(self):
        insertionsorted = self.insertionsort(self.array)
        self.assertTrue(np.array_equal(insertionsorted, self.sorted_array),
                        msg="Your Insertion Sort method is not running properly")

    def test_mergesort(self):
        mergesorted = self.mergesort(self.array)
        self.assertTrue(np.array_equal(mergesorted, self.sorted_array),
                        msg="Your Merge Sort method is not running properly")


if __name__ == '__main__':
    unittest.main(exit=False)