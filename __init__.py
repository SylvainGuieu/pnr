from __future__ import print_function
from vlt import *

from .dictionaries import loadDictionaries
from .processes import loadProcesses
from .devices import loadDevices
from .config import INSTRUMENT, say
from vlt.config import config

config['debug'] = True
config['cdt']['path'] += ["/Users/sylvain/Dropbox/python/savevlt/CDT"]
config['dictionary']['path'] += ["/Users/sylvain/Dropbox/python/savevlt/Dictionary", 
								 "/Users/sylvain/Dropbox/python/savevlt/Dictionary/CCSLite/"]
 

say(INSTRUMENT+" vlt interface\n")
glb = globals()
#class toto:
#	pass
#glb = toto.__dict__

loadDictionaries(glb)
say("")
loadProcesses(glb)
say("")
loadDevices(glb)
pnoc.setDebug(True)









