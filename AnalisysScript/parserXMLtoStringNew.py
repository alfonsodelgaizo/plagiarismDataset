import music21 as m

song = m.converter.parse('calledlove.mxl')


def getMusicProperties(x):
    s = '';
    t='';
    s = str(x.pitch) + ", " + str(x.duration.type) + ", " + str(x.duration.quarterLength);
    s += ", "
    if x.tie != None:
        t = x.tie.type;
    s += t + ", " + str(x.pitch.ps) + ", " + str(x.octave); # + str(x.seconds)  # x.seconds not always there
    return s



def pauseSearch(noteOrRests,ind):
    if (ind<=-1):
        return -1;
    if (noteOrRests[ind].isNote):
        print("termina")
        return ind
    if (noteOrRests[ind].isChord):
        print("termina")
        return ind
    if (noteOrRests[ind].isRest):
        return pauseSearch(noteOrRests,ind-1)


def pauseSearchForward(noteOrRests,ind):
    if (noteOrRests[ind].isRest):
        return  pauseSearchForward(noteOrRests,ind+1)
    if (noteOrRests[ind].isNote):
        print("termina")
        return ind



i=0;

s2='';

#Snippet per recuperare il numero di note del primo spartito
#partStream è l' array degli strumenti
#parStream[0] rappresenta il primo spartito
partStream = song.parts.stream()
#print(partStream[0])
#Questa riga sottostante permette di recuperare il numero di note del primo spartito (o primo strumento)
#NB: nel numero totale sono incluse anche le pause (oltre le note effettive)
lenOfPart=partStream[0].recurse().notesAndRests
#print(len(lenOfPart))
nlenOfPart= len(lenOfPart)
#for p in partStream:
  #  print(p.id)

it = iter(range(0,nlenOfPart))


print('pitch, duration_string, duration, tie, midi pitch, octave')
for i in it:
    a=song.recurse().notesAndRests[i]
    #print(a)
    print('... ',i,' ...')


    if (a.isRest):
        print("PAUSA")
        s2=s2+"p*"
        indUtileForward=pauseSearchForward(song.recurse().notesAndRests,i+1)
        print("indice utile: ",indUtileForward)
        for j in range (i,indUtileForward-1):
            next(it)
        i=indUtileForward


    if (a.isNote):
        print("NOTA")
        print("indice utile aggiornato in note: ",i)
        indUtile=pauseSearch(song.recurse().notesAndRests,i-1)
        print("INDICE :", indUtile)
        if (indUtile<=-1):
            print ("NON FARE NULLA")
        else:
            if (song.recurse().notesAndRests[indUtile].isChord):
                max = 0;
                maxDur = 0;
                for x in song.recurse().notesAndRests[indUtile]._notes:
                    if (x.pitch.ps > max):
                        max = x.pitch.ps
                        maxD = x.duration.quarterLength
                pitchCorrente = a.pitch.ps
                pitchPrec=max;
                pitchDiff = pitchCorrente - pitchPrec
                pitchDiff = round(pitchDiff)
                pitchDiff = str(pitchDiff)
                s2 = s2 + pitchDiff + '*';

            if (song.recurse().notesAndRests[indUtile].isNote):
                pitchCorrente = a.pitch.ps
                pitchPrec = song.recurse().notesAndRests[indUtile].pitch.ps;
                print("OPERAZIONE: ",pitchCorrente," - ",pitchPrec)
                pitchDiff = pitchCorrente - pitchPrec
                #Cast from Float to String
                pitchDiff = round(pitchDiff)
                #Cast from String to Float
                pitchDiff = str(pitchDiff)
                s2 = s2 + pitchDiff + '*';


        x = a;
        s = getMusicProperties(x);
        print(s);

    if (a.isChord):
        print("ACCORDO")
        for x in a._notes:
            s = getMusicProperties(x);
            print(s);

        indUtile = pauseSearch(song.recurse().notesAndRests, i - 1)
        if (indUtile <= -1):
            print("NON FARE NULLA")
        else:
            if (song.recurse().notesAndRests[indUtile].isChord):
                pitchPrec = 0;
                pitchPrecD = 0;
                for x in song.recurse().notesAndRests[indUtile]._notes:
                    if (x.pitch.ps > pitchPrec):
                        pitchPrec = x.pitch.ps
                        pitchPrecD = x.duration.quarterLength
                        notaChord=x


                pitchCorrente=0;
                pitchCorrenteD=0;
                for x in a._notes:
                    if (x.pitch.ps > pitchCorrente):
                        pitchCorrente = x.pitch.ps
                        pitchCorrenteD = x.duration.quarterLength
                        notaChord=x

                pitchDiff = pitchCorrente - pitchPrec
                pitchDiff = round(pitchDiff)
                pitchDiff = str(pitchDiff)
                s2 = s2 + pitchDiff + '*';

            if (song.recurse().notesAndRests[indUtile].isNote):
                pitchCorrente = 0;
                pitchCorrenteD = 0;
                for x in a._notes:
                    if (x.pitch.ps > pitchCorrente):
                        pitchCorrente = x.pitch.ps
                        pitchCorrenteD = x.duration.quarterLength
                        notaChord=x


                pitchPrec = song.recurse().notesAndRests[indUtile].pitch.ps;
                print("OPERAZIONE: ", pitchCorrente, " - ", pitchPrec)
                pitchDiff = pitchCorrente - pitchPrec
                # Cast from Float to String
                pitchDiff = round(pitchDiff)
                # Cast from String to Float
                pitchDiff = str(pitchDiff)
                s2 = s2 + pitchDiff + '*';




#s2=s2.replace("p*p","p")
#s2=s2.replace("p*p*p","p")
#s2=s2.replace("p*p*p*p","p")
#s2= s2.replace("*", "");


print(s2)

print("Done.")