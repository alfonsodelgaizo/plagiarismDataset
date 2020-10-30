from music21 import *

allBach = corpus.search('bach')

x = allBach[0]

print(x)
p = x.parse()

partStream = p.parts.stream()

for n in p.flat.notes:
    print("Note: %s%d %0.1f" % (n.pitch.name, n.pitch.octave, n.duration.quarterLength))