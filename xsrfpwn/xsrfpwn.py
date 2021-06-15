#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-::-:-:#
#    XSRF Pwn     #
#-:-:-:-:-:-:-::-:-:#

# Author: duckstroms
# This module requires XSRFPwn
# https://github.com/duckstroms/XSRFPwn

def startEngine():
    from xsrfprobe.core import main  # import stuff
    main.Engine()  # start the Scanner Engine ;)
