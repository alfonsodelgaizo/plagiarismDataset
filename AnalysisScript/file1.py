from music21 import *
f = note.Note("F5")

print(f.name)
print(f.octave)
song = converter.parse('calledlove.mxl')
#song.measures(1, 5).show() # show first 5 measures
#song.show();
#song.show('text')
print(song.notes)
print(song.elementOffset('D'))