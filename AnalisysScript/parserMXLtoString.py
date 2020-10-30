import music21 as m

song = m.converter.parse('calledlove.mxl')
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

i=0;

s2='';

#Snippet per recuperare il numero di note del primo spartito
#partStream è l' array degli strumenti
#parStream[0] rappresenta il primo spartito
partStream = song.parts.stream()
print(partStream[0])
#Questa riga sottostante permette di recuperare il numero di note del primo spartito (o primo strumento)
#NB: nel numero totale sono incluse anche le pause (oltre le note effettive)
lenOfPart=partStream[0].recurse().notesAndRests
print(len(lenOfPart))
nlenOfPart= len(lenOfPart)
#for p in partStream:
  #  print(p.id)

it = iter(range(0,nlenOfPart))



print('pitch, duration_string, duration, tie, midi pitch, octave')
for a in song.recurse().notesAndRests:
    print(a)
    print('... ',i,' ...')

    if (i==(nlenOfPart-1)):
        break

    if (a.isRest):
        s2=s2+"p*"
        print("PAUSA")

    if (a.isNote):
        print("NOTA")

        #pitchPrec= song.recurse().notesAndRests[i-1].pitch.ps;
        if (song.recurse().notesAndRests[i-1].isRest):
            if (song.recurse().notesAndRests[i - 2].isNote):
                pitchCorrente = a.pitch.ps
                pitchPrec = song.recurse().notesAndRests[i - 2].pitch.ps;
                pitchDiff = pitchCorrente - pitchPrec
                pitchDiff = round(pitchDiff)
                pitchDiff = str(pitchDiff)
                s2 = s2 + pitchDiff + '*';
            if (song.recurse().notesAndRests[i - 2].isRest):
                if (song.recurse().notesAndRests[i - 3].isNote):
                    pitchCorrente = a.pitch.ps
                    pitchPrec = song.recurse().notesAndRests[i - 3].pitch.ps;
                    pitchDiff = pitchCorrente - pitchPrec
                    pitchDiff = round(pitchDiff)
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';
                if (song.recurse().notesAndRests[i - 3].isRest):
                  if (song.recurse().notesAndRests[i - 4].isNote):
                    pitchCorrente = a.pitch.ps
                    pitchPrec = song.recurse().notesAndRests[i - 4].pitch.ps;
                    pitchDiff = pitchCorrente - pitchPrec
                    pitchDiff = round(pitchDiff)
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';
                  if (song.recurse().notesAndRests[i - 4].isRest):
                            if (song.recurse().notesAndRests[i - 5].isNote):
                                pitchCorrente = a.pitch.ps
                                pitchPrec = song.recurse().notesAndRests[i - 5].pitch.ps;
                                pitchDiff = pitchCorrente - pitchPrec
                                pitchDiff = round(pitchDiff)
                                pitchDiff = str(pitchDiff)
                                s2 = s2 + pitchDiff + '*';



        if (song.recurse().notesAndRests[i-1].isNote):
         pitchCorrente=a.pitch.ps
         pitchPrec= song.recurse().notesAndRests[i-1].pitch.ps;
         pitchDiff=pitchCorrente-pitchPrec
         pitchDiff=round(pitchDiff)
         pitchDiff=str(pitchDiff)
         s2 = s2 + pitchDiff+'*';

        x = a;
        s = getMusicProperties(x);
        print(s);

    if (a.isChord):
        print("ACCORDO")
        max=0;
        maxDur=0;
        for x in a._notes:
            if(x.pitch.ps>max):
                max=x.pitch.ps
                maxD=x.duration.quarterLength


    i=i+1;


print(s2)

print("Done.")