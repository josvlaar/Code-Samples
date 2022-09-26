import filename     # filename's executable statements are executed only the first time module is imported
filename.methodname(par)
filename.__name__   # module name as string
var = filename.methodname
var(par)
var2 = filename.varname # access other module's global variables

# import statements should be placed at beginning of file (but also works elsewhere)
# module names are added to global namespace if module is not imported from within functions or classes

from filename import method1, method2
method1(par)
from filename import *  # imports all names except those beginning with _ (not widely used because it overwrites local variables and is ugly code)
method1(par)

import filename as alias
alias.methodname(par)
from filename import method1 as method2
method2(par)

# when imported modules are changed, interpreter must be restarted or module reloaded with importlib.reload()

# make the code usable as a script as well as as an importable module (add at the end):
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
# code is not run if the module is imported

# modules of scripts being run can override modules in de standard library if they have the same name (higher precedence)

import sys
print(dir(sys)) # finds out which names a module defines
print(dir())    # names you have defined currently

import builtins
print(dir(builtins))    # builtin functions and variables


# Packages are a folder in sys.path with an __init__.py file.
import packagename.modulename   # all except last identifier must be a package, last can be module or package (not a function of class or variable from the previous package)
packagename.modulename.method(par)  # methods in an imported package must be invoked with full package name
from packagename import modulename
modulename.method(par)
from packagename.modulename import method
method(par)
# import first tests if the item is defined in the package, if not it is assumed to be a module, if not importerror is raised
from packagename import *   # looks for __all__ variable in __init__.py to find modules to load. If there is no __all__, only the parent module/package is loaded (not it's submodules)
# if you need to use modules with the same name but from different packages, use import 'as alias' for it's local name

from . import modulename    # parent module
from .. import modulename   # parent of parent module
from ..package import modulename    # different parent of parent
# modules intended for use as the main module of a program must use absolute imports (relative won't work because the name of the main module is "__main__")

# __path__ variable indicates where __init__.py is