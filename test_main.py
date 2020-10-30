import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_exponential(self) : 
        lam,mean=2,0
        for i in range(100) : mean = mean + exponential(lam)
        mean = mean / 100

        bar = np.sqrt(1/(lam*lam)/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - 1/lam )<bar, "your exponential function does not appear to be working correctly" )
        
    def test_firstevent(self) : 
        mean=0
        for i in range(100) : mean = mean + firstevent(4,5)
        mean = mean / 100

        pp = 4 / (4+5)
        bar = np.sqrt(pp*(1-pp)/100)*st.norm.ppf( (0.99 + 1) / 2 )
        self.assertTrue( np.fabs( mean - pp )<bar, "your firstevent function does not appear to be working correctly"  )
