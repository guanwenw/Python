import unittest
#import os
import sys

"""
python -m unittest -v TestStringMethods
test_isupper (TestStringMethods.TestStringMethods) ... ok
test_split (TestStringMethods.TestStringMethods) ... ok
test_upper (TestStringMethods.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")


    @unittest.skipIf( True,
#    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass


    #@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    @unittest.skipUnless(False, "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        print "Windows"
        pass

    def skipUnlessHasattr(obj, attr):
        if hasattr(obj, attr):
            return lambda func: func
        return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass

    
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")





if __name__ == '__main__':
    #s = 'hello world'
    #print s.split(2)
    unittest.main()
