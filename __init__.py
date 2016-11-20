from __future__ import print_function
from vlt import *
from dictionaries import loadDictionaries
from processes import loadProcesses
from .config import INSTRUMENT, say

say(INSTRUMENT+" vlt interface\n")
loadDictionaries(globals())
say("")
loadProcesses(globals())
say("")











