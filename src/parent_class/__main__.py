### FYI, this will give an import error if executed while in the current working directory

import sys
sys_args = sys.argv[1:]

from parent_class.parent_class import run
run( *sys_args )

