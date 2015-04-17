#!/usr/bin/env python

import subprocess, sys, termios, time, tty

freq={
  "0":    392       ,# G4
  "1":    415.30    ,# G#4 / Ab4
  "2":    440       ,# A4
  "3":    466.16    ,# A#4 / Bb4
  "4":    493.88    ,# B4
  "5":    523.25    ,# C5  
  "6":    554.37    ,# C#5 / Db5   
  "7":    587.33    ,# D5  
  "8":    622.25    ,# D#5 / Eb5   
  "9":    659.25    ,# E5  
  "10":   698.46    ,# F5  
  "11":   739.99    ,# F#5 / Gb5   
  "12":   783.99    ,# G5  
  "13":   830.61    ,# G#5 / Ab5   
  "14":   880.00    ,# A5  
  "15":   932.33     # A#5 / Bb5  
}

keys=["1","2","3","4"]
notes=[]

timepool=0
previoustime=time.time()

def pressed():
  """
  Returns a pressed key (Supposedly non-blocking)
  """

  def isData():
    return select.select([sys.stdin], [], [], 0.01)==([sys.stdin], [], [])

  c=""
  old_settings=termios.tcgetattr(sys.stdin)
  try:
    tty.setcbreak(sys.stdin.fileno())
    if isData():
      c=sys.stdin.read(1)
  finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return c

if __name__=="__main__":
  while 1:
    a=pressed()
    if a: notes.append(a)
    print "\r",notes,

  