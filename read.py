import os

script_dir = os.path.dirname(__file__)
relpath1 = "Characters/Obi_Wan_Kenobi.chf"
filepath1 = os.path.join(script_dir, relpath1)
data = open(filepath1, 'rb').read()

relpath2 = "Characters/jSchlatt.chf"
filepath2 = os.path.join(script_dir, relpath2)
data2 = open(filepath2, 'rb').read()

def print_something(starting_idx, idx, changed):
    print("something"+str(somethingCount)+" = data["+str(starting_idx)+":"+str(idx)+"] #"+(" changed" if changed else " unchanged"))

same = True
starting_idx = 0
somethingCount = 1
data2_split = data2.hex(' ').split(' ')
for idx, i in enumerate(data.hex(' ').split(' ')):
    a = i
    b = data2_split[idx]
    if a == b:
        if(same == False):
            print_something(starting_idx, idx, True)
            same = True
            starting_idx = idx
            somethingCount+=1
    else:
        if(same == True):
            print_something(starting_idx, idx, False)
            same = False
            starting_idx = idx
            somethingCount+=1

signature = data[:4] # unchanged, always 42 42 00 00

something2 = data[4:9] # changed
something3 = data[9:23] # unchanged
something4 = data[23:24] # changed
something5 = data[24:26] # unchanged
something6 = data[26:29] # changed
something7 = data[29:31] # unchanged
something8 = data[31:90] # changed
something9 = data[90:91] # unchanged
something10 = data[91:92] # changed
something11 = data[92:93] # unchanged
something12 = data[93:94] # changed
something13 = data[94:95] # unchanged
something14 = data[95:188] # changed
something15 = data[188:189] # unchanged
something16 = data[189:320] # changed
something17 = data[320:321] # unchanged
something18 = data[321:388] # changed
something19 = data[388:389] # unchanged
something20 = data[389:524] # changed
something21 = data[524:525] # unchanged
something22 = data[525:542] # changed
something23 = data[542:543] # unchanged
something24 = data[543:620] # changed
something25 = data[620:621] # unchanged
something26 = data[621:1014] # changed

# variable length, find first instance TODO
deadbeef = data[1014:4089] # unchanged

eof = data[4089:4091] # changed

# DEADBEEF padding to reach 4k file size

wow = 1