#!"d:\aya's old hdd\d\courses\randr project\venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'isort==4.3.9','console_scripts','isort'
__requires__ = 'isort==4.3.9'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('isort==4.3.9', 'console_scripts', 'isort')()
    )
