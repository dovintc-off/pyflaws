import sys

def wertis(*args, **kwargs):
    frame = sys._getframe(1)
    caller_globals = frame.f_globals
    for key in list(caller_globals.keys()):
        caller_globals[key] = None