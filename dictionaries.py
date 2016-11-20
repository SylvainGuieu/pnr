from __future__ import print_function
from .config import INSTRUMENT, VERBOSE, say
from vlt import openDictionary

def loadDictionaries(to=None):
    global acs, cfg, dcs, ics, os, dpr, osb, pndict
    
    say("Reading main dictionaries ...")
    
    say("   %s_ACS -> `acs` "%INSTRUMENT)
    acs = openDictionary(INSTRUMENT+"_ACS")
    
    say("   %s_CFG -> `cfg` "%INSTRUMENT)
    cfg = openDictionary(INSTRUMENT+"_CFG")
    
    say("   %s_DCS -> `dcs` "%INSTRUMENT)
    dcs = openDictionary(INSTRUMENT+"_DCS")
    
    say("   %s_ICS -> `ics` "%INSTRUMENT)
    ics = openDictionary(INSTRUMENT+"_ICS")
    
    say("   %s_OS -> `os` "%INSTRUMENT)
    os = openDictionary(INSTRUMENT+"_OS")
    
    say("   DPR -> `dpr` ")
    dpr = openDictionary("DPR")
    
    say("   OSB -> `osb` ")
    osb = openDictionary("OSB")
    
    say("All dictionary merged in `pndict`")
    pndict = acs+cfg+dcs+ics+os+dpr+osb

    if to:
        to['acs'] = acs
        to['cfg'] = cfg
        to['dcs'] = dcs
        to['ics'] = ics
        to['os']  = os
        to['dpr'] = dpr
        to['osb'] = osb
        to['pndict']= pndict
    
