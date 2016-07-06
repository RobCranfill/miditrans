#!/usr/bin/python3
#
# Command-line app to write data for MPK mapper app
# Note that we want Python 3, not 2!
# robcranfill@gmail.com

import sys
 
SR18voiceNames_ = [
        "kick",
        "snare_1",
        "snare_2",
        "highhat_1",
        "highhat_2",
        "highhat_3",
        "tom_1",
        "tom_2",
        "tom_3",
        "crash",
        "ride",
        "bell"
        ]

# default assignment
MPKmap_ = ["kick",  "snare_1",  "highhat_1",   "highhat_3",
           "tom_1", "tom_3",    "crash",        "ride"]

# show the choices
def print_pads():
	print("--- SR18 pads ---")
	i = 0
	for v in SR18voiceNames_:
		i = i + 1
		print("voice {0:2}: {1}".format(i, v))

def print_mapped_pads():
	print("--- mapping ---")
	for i,v in enumerate(MPKmap_):
		print("pad {0}: {1}".format(i, v))


# return false iff we are done processing
def process_command():
	p = str(input("\nSet pad number: "))
	if not p:
		return False
	v = input("To voice #? ")
	np = int(p)
	nv = int(v)
	voice = SR18voiceNames_[nv-1]
	print("voice {0} is '{1}'".format(nv, voice))
	MPKmap_[np] = voice
	return True



def output_pad_mapping_code(filehandle):
        filehandle.write("\n\n# Written by python front-end\n" \
        "mapMPKPadsToSR18Pads = [\n" \
        "\tChannelFilter(10) >> [\n" \
#        "\t\t~KeyFilter(notes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),\n" \
        "\t\t~KeyFilter(notes=[0,1,2,3,4,5,6,7]),\n" \
        "\t\tKeyFilter(notes=[0]) >> pad_{0},\n" \
        "\t\tKeyFilter(notes=[1]) >> pad_{1},\n" \
        "\t\tKeyFilter(notes=[2]) >> pad_{2},\n" \
        "\t\tKeyFilter(notes=[3]) >> pad_{3},\n" \
        "\t\tKeyFilter(notes=[4]) >> pad_{4},\n" \
        "\t\tKeyFilter(notes=[5]) >> pad_{5},\n" \
        "\t\tKeyFilter(notes=[6]) >> pad_{6},\n" \
        "\t\tKeyFilter(notes=[7]) >> pad_{7}\n" \
#        "     KeyFilter(notes=[8]) >> pad_snare_1,\n" \
#        "     KeyFilter(notes=[9]) >> pad_kick,\n" \
#        "     KeyFilter(notes=[10]) >> pad_highhat_1,\n" \
#        "     KeyFilter(notes=[11]) >> pad_highhat_3,\n" \
#        "     KeyFilter(notes=[12]) >> pad_tom_1,\n" \
#        "     KeyFilter(notes=[13]) >> pad_tom_3,\n" \
#        "     KeyFilter(notes=[14]) >> pad_ride,\n" \
#        "     KeyFilter(notes=[15]) >> pad_crash\n" \
        "\t\t]\n" \
        "\t]\n\n".format(MPKmap_[0], MPKmap_[1], MPKmap_[2], MPKmap_[3],
                         MPKmap_[4], MPKmap_[5], MPKmap_[6], MPKmap_[7]))


def output_mididings_code():
        with open('midi_mapper.py', 'w') as outfile:
                with open("changer_1.py.part") as infile:
                        outfile.write(infile.read())

                output_pad_mapping_code(outfile)

                with open("changer_2.py.part") as infile:
                        outfile.write(infile.read())


# start
while (True):
	print_pads()
	print_mapped_pads()
	if not process_command():
		print("gubbeye!")
		break
output_mididings_code()

# end

