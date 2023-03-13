import RPi.GPIO as f

f.setmode(f.BCM)

f.setup(14, f.OUT)
f.output(14, 0)