
import string
import math
from numpy import *
import matplotlib.pyplot as plt
from scipy.constants import *

CURRENT = 6.24*10**12
A_Zn = 67
XS = 10**(-27)
CI_in_BQ = 3.7*10**10
DECAY = 1.0 - math.e**(-0.693*2/78.264)

SR_DATA = [
    '12.00 MeV   2.357E-02  1.166E-05  416.39 um    20.26 um    28.42 um',
    '13.00 MeV   2.223E-02  1.087E-05  477.01 um    22.77 um    32.30 um',
    '14.00 MeV   2.104E-02  1.018E-05  541.18 um    25.32 um    36.39 um',
    '15.00 MeV   1.999E-02  9.577E-06  608.85 um    27.92 um    40.67 um',
    '16.00 MeV   1.905E-02  9.046E-06  679.97 um    30.59 um    45.15 um',
    '17.00 MeV   1.821E-02  8.574E-06  754.48 um    33.31 um    49.82 um']

TALIS_DATA = [
    '1.200E+01 1.61654E+01',
    '1.300E+01 3.57061E+01',
    '1.400E+01 7.68215E+01',
    '1.500E+01 1.05143E+02',
    '1.600E+01 1.20884E+02',
    '1.700E+01 1.28235E+02']

TALIS_DATA_N = [
    '1.200E+01 3.90093E+02',
    '1.300E+01 2.83251E+02',
    '1.400E+01 1.99790E+02',
    '1.500E+01 1.41941E+02',
    '1.600E+01 1.04488E+02',
    '1.700E+01 8.11343E+01']

def extract_talis(l):
    return float(string.split(l)[1])

def extract_sr(l):
    return float( string.split(l)[2])

sr_data = map(extract_sr, SR_DATA)
talis_data = map(extract_talis, TALIS_DATA_N)

sr_array = array(sr_data)*1000
talis_array = array(talis_data)

SUM = (talis_array / sr_array).sum()

activity_per_hour = SUM*N_A*XS/A_Zn*CURRENT/CI_in_BQ * DECAY

print "%.4e Ci" % activity_per_hour
print "%.4e Ci" % (activity_per_hour*60)
