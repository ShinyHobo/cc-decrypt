import os

script_dir = os.path.dirname(__file__)
relpath1 = "Characters/Default_Male.chf" # default
filepath1 = os.path.join(script_dir, relpath1)
data = open(filepath1, 'rb').read()

#relpath2 = "Characters/Freckle_49.chf" # freckle offset 1
#relpath2 = "Characters/Green_Eyes.chf" # green eyes
relpath2 = "Characters/Blue_Eyes.chf" # blue eyes
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

signature = data[:4].hex(' ') # unchanged, always 42 42 00 00

hash = data[4:9].hex(' ') # changed, always changes? possible hash
possible_client_info = data[9:23].hex(' ') # unchanged, never changes for same user - identifying info?

eye_color = data[783:786].hex(' ') # RGB values

# variable length, find first instance TODO
deadbeef = data[1014:4089].hex(' ') # unchanged

eof = data[4089:4091].hex(' ') # changed, always 3 bytes?

# DEADBEEF padding to reach 4k file size

wow = 1