#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#    XSRF Pwn     #
#-:-:-:-:-:-:-::-:-:#

# Author: duckstroms
# This module requires XSRFPwn
# https://github.com/duckstroms/XSRFPwn

from xsrfprobe.core.colors import *
from xsrfprobe.files.config import DEBUG as verbose

def verbout(stat, content_info):
    '''
    This module is for giving a verbose
                output.
    '''

    # If debug mode is chosen as True
    if verbose:
        # Concatenate the stat type and string value and print out
        print(stat+content_info)

#def verbo_sity(*verb_args):
#    if verb_args[0] > (3 - args.verbose):
#        print verb_args[1]
