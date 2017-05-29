#!/usr/bin/python
# -*- coding: utf-8 -*-


import signal
import sys


def signal_handler(signal, frame):
    print("\nCtrl+C received!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Waiting for Ctrl+C')
signal.pause()
