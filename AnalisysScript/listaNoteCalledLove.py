import music21 as m

song = m.converter.parse('ilpostino.mxl')
# process the ties
song = song.stripTies()

# unfold repetitions
i = 0;
for a in song:
    if a.isStream:
        e = m.repeat.Expander(a)
        s2 = e.process()
        timing = s2.secondsMap
        song[i] = s2
    i += 1;

# todo: add note onsets

def getMusicProperties(x):
    s = '';
    t='';
    s = str(x.pitch) + ", " + str(x.duration.type) + ", " + str(x.duration.quarterLength);
    s += ", "
    if x.tie != None:
        t = x.tie.type;
    s += t + ", " + str(x.pitch.ps) + ", " + str(x.octave); # + str(x.seconds)  # x.seconds not always there
    return s

i=1;

print('pitch, duration_string, duration, tie, midi pitch, octave')
for a in song.recurse().notesAndRests:
    print(a)
    print('... ',i,' ...')

    if (a.isRest):
        print("PAUSA")

    if (a.isNote):
        print("NOTA")
        x = a;
        s = getMusicProperties(x);
        print(s);

    if (a.isChord):
        print("ACCORDO")
        for x in a._notes:
            s = getMusicProperties(x);
            print(s);

    i=i+1;


print("Done.")