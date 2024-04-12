import os

script_dir = os.path.dirname(__file__)
#first_file = "Characters/M_Default.chf" # default male
first_file = "Characters/M_Default.chf" # default female
filepath1 = os.path.join(script_dir, first_file)
data = open(filepath1, 'rb').read()

#second_file = "Characters/F_Default.chf" # default female
second_file = "Characters/F_Eyes_Brown.chf"
filepath2 = os.path.join(script_dir, second_file)
data2 = open(filepath2, 'rb').read()

def print_something(starting_idx, idx, changed):
    print("something"+str(somethingCount)+" = data["+str(starting_idx)+":"+str(idx)+"].hex(\' \') #"+(" changed" if changed else " unchanged"))

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

hash = data[4:8].hex(' ') # changed, always changes? possible hash

something0 = data[8:9].hex() # changes
something1 = data[9:10].hex() # changed in 1 file
separator1 = data[10:12].hex(' ') # always unchanged? 00 00
something2 = data[12:13].hex() # changes
something3 = data[12:14].hex(' ') # changed after sex change

identifier1 = data[14:21].hex(' ') # always unchanged - 00 00 28 B5 2F FD 60

something5 = data[21:23].hex(' ') # changed after sex change
something6 = data[23:25].hex(' ')

identifier2 = data[25:26].hex(' ') # always unchanged - 00

eye_color = data[783:786].hex() # RGB values
eye_color2 = data2[783:786].hex()

# variable length, find first instance TODO
deadbeef = data[1014:4089].hex(' ') # unchanged

eof = data[4089:4091].hex(' ') # changed, always 3 bytes?

# DEADBEEF padding to reach 4k file size

wow = 1