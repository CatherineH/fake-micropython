# Fake Micropython

fake-micropython replicates the modules of micropython without any 
actual functionality.

## Why?

fake-micropython can speed the development of micropython projects for 
two reasons:

- micropython loaded on a micro controller offers little feedback when 
things fail, and
- the process of assembling hex files and loading them onto 
microcontrollers takes much longer than running a python script on a 
computer, thus solving problems locally can speed up the development 
time and reduce distracting breaks.

## Why not?

This is probably a bad way of solving this. There should probably be a 
way to reverse engineer the micropython API, but I don't know enough 
about ARM builds.

## Installation

Run:

```bash
python setup.py install
```

