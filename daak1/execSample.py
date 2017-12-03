gl = {}
execfile("../../config/config1.py", gl)

import runpy
file_globals = runpy.run_path("../../config/config1.py")

# print file_globals

# print gl
print file_globals['root']