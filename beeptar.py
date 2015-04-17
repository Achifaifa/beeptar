#!/usr/bin/env python

import subprocess, select, sys, termios, time, tty

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

def main():

  freq={
    "0000":   "392"       ,# G4
    "0001":   "415.30"    ,# G#4 / Ab4
    "0010":   "440"       ,# A4
    "0011":   "466.16"    ,# A#4 / Bb4
    "0100":   "493.88"    ,# B4
    "0101":   "523.25"    ,# C5  
    "0110":   "554.37"    ,# C#5 / Db5   
    "0111":   "587.33"    ,# D5  
    "1000":   "622.25"    ,# D#5 / Eb5   
    "1001":   "659.25"    ,# E5  
    "1010":   "698.46"    ,# F5  
    "1011":   "739.99"    ,# F#5 / Gb5   
    "1100":   "783.99"    ,# G5  
    "1101":   "830.61"    ,# G#5 / Ab5   
    "1110":   "880.00"    ,# A5  
    "1111":   "932.33"     # A#5 / Bb5  
  }

  keys=["1","2","3","4"]
  outp=["0","0","0","0"]
  notes=[]

  while 1:
    a=pressed()
    if a not in ["","\n"]: notes.append(a)
    if a=="\n":
      if keys[0] in notes: outp[0]="1"
      if keys[1] in notes: outp[1]="1"
      if keys[2] in notes: outp[2]="1"
      if keys[3] in notes: outp[3]="1"
      subprocess.Popen(["beep","-f "+freq["".join(outp)]])
      outp=["0","0","0","0"]
      notes=[]


try:
  main()
except KeyboardInterrupt:
  exit()


  