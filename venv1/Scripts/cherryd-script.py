#!C:\Michi\new1\PolArg\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'CherryPy==13.1.0','console_scripts','cherryd'
__requires__ = 'CherryPy==13.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('CherryPy==13.1.0', 'console_scripts', 'cherryd')()
    )
