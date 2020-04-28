
"""
Dispatcher scripts
==============
Sending data to scripts
"""

__version__ = "1.0.0"


__all__ = [
    'TGDispatcher',
    'TSDispatcher',
    'TWDispatcher',
]


from .tgdispatcher import TGDispatcher
from .tsdispatcher import TSDispatcher
from .twdispatcher import TWDispatcher
