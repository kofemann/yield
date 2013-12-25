#!/usr/bin/env python

from numpy import *
from scipy.constants import *
from yield_settings import *

# CONSTANTS
mkA = 6.24*10**12     # micro amper
XS_MB = 10**(-27)     # millibarn
CI_in_BQ = 3.7*10**10 # cuirie in beqquerel
DECAY = 1.0 - math.e**(-0.693*TIME_IN_HOURS/HALF_LIVE)
MILLI_GRAM_IN_GRAM = 1000

loses_array = array(LOSES)*MILLI_GRAM_IN_GRAM
xs_array = array(XS)

SUM = (xs_array / loses_array).sum()

activity_per_hour = SUM*N_A*XS_MB/TARGET_A*mkA/CI_in_BQ * DECAY

print "Special Activity              : %.4e Ci/mkA*h" % activity_per_hour
print "Yield in %2dh, current %4dmkA : %.4e Ci" % (TIME_IN_HOURS, CURRENT, activity_per_hour*CURRENT*TIME_IN_HOURS)
