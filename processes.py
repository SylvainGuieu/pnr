from __future__ import print_function
from .config import INSTRUMENT, VERBOSE, say
from vlt import openProcess, setDefaultProcess

def loadProcesses(to=None):
    global pnoc
    
    say("Opening Processes ...")
    say("    pnoControl -> `pnoc`")
    pnoc = openProcess("pnoControl")

    say("pnoControl is now the default process")
    setDefaultProcess(pnoc)
    if to:
        to['pnoc'] = pnoc
            
    
