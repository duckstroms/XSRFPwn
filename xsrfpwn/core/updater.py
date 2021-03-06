#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#    XSRF Pwn     #
#-:-:-:-:-:-:-::-:-:#

# Author: duckstroms
# This module requires XSRFPwn
# https://github.com/duckstroms/XSRFPwn

import os
from requests import get
from xsrfprobe import __version__
from xsrfprobe.core.colors import *

def updater():
    '''
    Function to update XSRFProbe seamlessly.
    '''
    print(GR+'Checking for updates...')
    vno = get('https://raw.githubusercontent.com/0xInfection/XSRFProbe/master/xsrfprobe/files/VersionNum').text
    print(GR+'Version on GitHub: '+color.CYAN+vno.strip())
    print(GR+'Version You Have : '+color.CYAN+__version__)
    if vno != __version__:
        print(G+'A new version of XSRFProbe is available!')
        current_path = os.getcwd().split('/') # if you know it, you know it
        folder = current_path[-1] # current directory name
        path = '/'.join(current_path) # current directory path
        choice = input(O+'Would you like to update? [Y/n] :> ').lower()
        if choice != 'n':
            print(GR+'Updating XSRFProbe...')
            os.system('git clone --quiet https://github.com/0xInfection/XSRFProbe %s' % (folder))
            os.system('cp -r %s/%s/* %s && rm -r %s/%s/ 2>/dev/null' % (path, folder, path, path, folder))
            print(G+'Update successful!')
    else:
        print(G+'XSRFProbe is up to date!')
    quit()
