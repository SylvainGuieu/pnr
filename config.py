from __future__ import print_function
from vlt.config import config as vltconfig
INSTRUMENT = "PIONIER"
VERBOSE = True
vltconfig['isf']['ISF'] = "PIONIER"

if not VERBOSE:
    say = lambda *a,**k: None
else:
    say = print    
