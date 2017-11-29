gl = {}
execfile("../../config/config.py", gl)

import runpy
file_globals = runpy.run_path("../../config/config.py")

# print file_globals

# print gl
print file_globals['root']