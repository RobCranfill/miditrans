#!/usr/bin/python
# from http://dsacre.github.io/mididings/doc/start.html#anatomy-of-a-mididings-script
#
# Uses dictionary of kit names; filters out SYSRT from DM6 in printout.
# Fixed typo in scenes, all work OK now.
#

from mididings import *

from mididings.extra.osc import OSCInterface

# For 'livedings' GUI
#hook(OSCInterface())

# For 'webdings' GUI
hook(OSCInterface(4011, 4012))

config(
    in_ports  = [('in_1',  'MPKmini2:0'), ('in_2', 'e-drum:0')],
    out_ports = [('out_1', 'MidiSport 1x1:0'), ('out_2', 'MidiSport 1x1:0')]
)


kits_ = {
  'Ambient': 01,
  'DarkKit01': 13,
  'ElectTR08': 16,
  'ElectTR09': 17,
  'Latin01': 43,
  'Rock01': 55,
  'Rock02': 56,
  'Rock03': 57,
  'Rock04': 58,
  'Rock05': 59,
  'Rock06': 60,
  'Techno01': 79
  };

def makeScenes():
  s = {}
  s[1] = makeScene('Rock01')
  s[2] = makeScene('Rock02')
  s[3] = makeScene('Rock03')
  s[4] = makeScene('Rock04')
  s[5] = makeSceneWithPrint('Ambient')
  s[6] = makeScene('ElectTR08')
  s[7] = makeScene('Techno01')
  s[8] = makeScene('Latin01')
  return s

def makeScene(name):
  return Scene(name,[outputKit(name),mapDM6toSR18_b])

def makeSceneWithPrint(name):
  return Scene(name,[~Filter(SYSRT_SENSING) >> Print('event: '),outputKit(name),mapDM6toSR18_b])
                
def outputKit(kitName):
  global kit_
  return Output('out_1', channel=10, program=(0,kits_[kitName]))

mapDM6toSR18_b = [
  ~KeyFilter(notes=[40, 45, 43]),
   KeyFilter(notes=[40]) >> Key(37),
   KeyFilter(notes=[45]) >> Key(47),
   KeyFilter(notes=[43]) >> Key(41)
   ]


run(
  scenes = makeScenes(),
  control = Filter(PROGRAM) >> SceneSwitch(),
  pre = ~Filter(PROGRAM),
  )

