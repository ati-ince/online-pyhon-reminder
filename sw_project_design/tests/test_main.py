# pylint: disable=C0301 #Line too long (%s/%s)
# pylint: disable=C0303 #Trailing whitespace
# pylint: disable=C0304 #Final newline missing

""" This module developed for basic unit testing sctripting 
"""
import unittest

'''Global functions are not necessary, but it could be usefull for development. Just added for keep in mind.'''
def fn_global1():
    """[summary]
    """
    pass    

def fn_global2():
    """[summary]
    """    
    pass


class TestMain(unittest.TestCase):
    ''' Basic Unit Test structure for future development, 
    The class must have setUp and tearDown method for all development (constructor/destructor)'''
    
    def setUp(self):
        '''Initilizer, set any variables, object etc. It creates from beginning for all sub-test function'''
        pass

    def tearDown(self):
        '''delete for clean creation'''
        pass
    
    #@unittest.skip('')
    def test_function1(self):
        """[All sub-test function must start with test_]

        Raises:
            Exception: [description]
        """        

if __name__ == '__main__':
    unittest.main()