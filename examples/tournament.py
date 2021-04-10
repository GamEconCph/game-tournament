import importlib.util
import os
import sys


# TODO: Decide on what student's files should be named
# TODO: Decide on where student's files should be read from

# student_file_path
# 


# import module using full path to file 
spec = importlib.util.spec_from_file_location(
    "module.name",
    r"C:\Users\tobi_\OneDrive - Københavns Universitet\KU\GameTheory\game-tournament\examples\discrete\brian.py",
)
foo = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = foo
spec.loader.exec_module(foo)
Player1 = foo.brian("TEST")