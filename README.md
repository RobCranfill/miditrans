# miditrans
Code to run on a Raspberry Pi to allow me to control an SR18 from a MPKMini

Raison d'être
----
I have an [Alesis DM6 drum kit] (http://www.alesis.com/dm6) that has a small set of sounds built-in, but a) I never liked them very much, and b) the "brain" died and the built-in sounds don't work any more. I also have an [Alesis SR18 drum module] (http://www.alesis.com/sr18) that has a much bigger and nicer set of sounds built in, so I wanted to use that instead. One problem is that the notes the DM6 puts out aren't the same as what the SR18 wants (just for a few pads: two toms and one cymbal, IIRC). Another issue is that the DM6 uses USB MIDI, but the SR18 sports "real" 5-pin MIDI connectors, so you can't hook them directly together anyway.

I tried using [hydrogen] (http://www.hydrogen-music.org/hcms/) and a desktop PC running [kxStudio](http:kxstudio.linuxaudio.org), but that's a very heavyweight solution. Then I found [mididings](http://das.nasophon.de/mididings/), and realized I could probably run that on a [Raspberry Pi](https://www.raspberrypi.org) quite nicely, and use my [Akai MPKmini](http://www.akaipro.com/product/mpk-mini-mkii) as a controller. And so you have this project, which so far isn't much more than one mididings script, but might evolve to more. We shall see!


Requirements
----
1) ALSA and other prerequisites weren't included by default in Raspbian:
 * ``sudo apt-get install alsa-base alsa-utils alsa-oss``
 * ``sudo apt-get install libglib2.0-dev``
 * ``sudo apt-get install libboost-dev``
 * ``sudo apt-get install jackd libjack-dev``
 * ``sudo apt-get install libasound2 libasound2-dev``
 * ``sudo apt-get install python-dev libboost-python-dev``

2) [Mididings](http://das.nasophon.de/mididings/)


Things I'd like this to be able to do (aka "shortcomings" or "todo")
----
1) Change drum kits so I can play the DM6 thru the SR18 (or is it the other way around?).
2) Can it do more? Like pump MIDI events into my MIDI keyboard, thus using it as a tone generator?


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
