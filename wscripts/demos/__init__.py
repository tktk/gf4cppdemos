# -*- coding: utf-8 -*-

from . import helloworld

from . import window_closeevent
from . import window_paintevent
from . import window_positionevent
from . import window_sizeevent
from . import window_mousebuttonevent
from . import window_closerequest

def build( _context ):
    helloworld.build( _context )

    window_closeevent.build( _context )
    window_paintevent.build( _context )
    window_positionevent.build( _context )
    window_sizeevent.build( _context )
    window_mousebuttonevent.build( _context )
    window_closerequest.build( _context )
