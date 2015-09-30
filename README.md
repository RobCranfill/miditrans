# miditrans
Code - that will run on a dedicated Raspberry Pi? - to allow me to control an SR18 from a MPKMini


Notes to myself
----

```
pi@studiopi ~/proj/studio $lsusb
Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. 
Bus 001 Device 004: ID 05e3:0608 Genesys Logic, Inc. USB-2.0 4-Port HUB
Bus 001 Device 008: ID 2011:0715      {Note: I think this is the MPKMini; don't know why it's blank}
Bus 001 Device 007: ID 0763:1011 Midiman MidiSport 1x1

pi@studiopi ~/proj/studio $aconnect -i
client 0: 'System' [type=kernel]
    0 'Timer           '
    1 'Announce        '
client 14: 'Midi Through' [type=kernel]
    0 'Midi Through Port-0'
client 20: 'MPKmini2' [type=kernel]
    0 'MPKmini2 MIDI 1 '
client 24: 'MidiSport 1x1' [type=kernel]
    0 'MidiSport 1x1 MIDI 1'

pi@studiopi ~/proj/studio $aconnect -o
client 14: 'Midi Through' [type=kernel]
    0 'Midi Through Port-0'
client 20: 'MPKmini2' [type=kernel]
    0 'MPKmini2 MIDI 1 '
client 24: 'MidiSport 1x1' [type=kernel]
    0 'MidiSport 1x1 MIDI 1'

```
