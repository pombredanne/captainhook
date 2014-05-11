# # # # # # # # # # # # # #
# CAPTAINHOOK IDENTIFIER  #
# # # # # # # # # # # # # #
from .utils import bash, python_files_for_commit

DEFAULT = 'on'


def run(arg=''):
    "Check flake8 errors in the code base."
    py_files = str(python_files_for_commit())
    if not py_files:
        return
    b = bash("flake8 {0} {1}".format(py_files.replace('\n', ' '), arg))
    if b.err:
        if b"command not found" in b.err:
            return (
                "flake8 is required for the flake8 plugin.\n"
                "`pip install flake8` or turn it off in your tox.ini file.")
    return b