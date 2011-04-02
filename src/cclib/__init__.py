"""
cclib (http://cclib.sf.net) is (c) 2006-2010, the cclib development team
and licensed under the LGPL (http://www.gnu.org/copyleft/lgpl.html).
"""

__revision__ = "$Revision$"
__version__ = "1.0.1"

from . import parser
from . import progress
from . import method
from . import bridge

# The test module can be imported if it was installed with cclib.
try:
    import test
except:
    pass
