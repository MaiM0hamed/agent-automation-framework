# Dummy audioop module for Python 3.13 compatibility
class error(Exception): pass

def lin2lin(fragment, width, newwidth): return b""
def bias(fragment, width, bias): return b""
def lin2adpcm(fragment, width, state): return (b"", (0, 0))
def adpcm2lin(fragment, width, state): return (b"", (0, 0))
def lin2alaw(fragment, width): return b""
def alaw2lin(fragment, width): return b""
def lin2ulaw(fragment, width): return b""
def ulaw2lin(fragment, width): return b""
def mul(fragment, width, factor): return b""
def max(fragment, width): return 0
def minmax(fragment, width): return (0, 0)
def avg(fragment, width): return 0
def rms(fragment, width): return 0
def findfit(fragment, reference): return (0, 0)
def findmax(fragment, length): return 0
def findfactor(fragment, reference): return 0.0
def cross(fragment, width): return 0
def add(fragment1, fragment2, width): return b""
def tomono(fragment, width, lfactor, rfactor): return b""
def tostereo(fragment, width, lfactor, rfactor): return b""
def getsample(fragment, width, index): return 0
def reverse(fragment, width): return b""
def byteswap(fragment, width): return b""
def ratecv(fragment, width, nchannels, inrate, outrate, state, weightA=1, weightB=0): return (b"", (0, 0))
