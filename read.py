import os

script_dir = os.path.dirname(__file__)
relpath = "Characters/Obi_Wan_Kenobi.chf"
filepath = os.path.join(script_dir, relpath)

data = open(filepath, 'rb').read()

signature = data[:4] # always the same: 42 42 00 00
something1 = data[4:9] # changed
something2 = data[9:23] # unchanged
something3 = data[23:24] # changed
something4 = data[24:26] # unchanged

something5 = data[90:91] # unchanged 00
something6 = data[91:92] # changed
something7 = data[92:93] # unchanged 00
something8 = data[93:94] # changed
something9 = data[94:95] # unchanged 00

# everything else

# DEADBEEF padding to reach 4k file size

wow = 1