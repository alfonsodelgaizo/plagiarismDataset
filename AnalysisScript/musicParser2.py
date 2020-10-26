import music21 as m
import os
import csv


#Creo una nuova classe con lo scopo di poter generare una lista di canzoni con il
# parsing dell'MXL in string e vettore numerico di intervalli associato
class SongParse:
  def __init__(self, songName, songString):
    self.songName = songName
    self.songString = songString

songParseList=[]


def generateCSV():

    with open('datasetParsing2DEF.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['N','SongName', 'SongString'])
        i=1
        for song in songParseList:
            filewriter.writerow([i,song.songName,song.songString])
            i=i+1

def folderRead(folderName):
    location = os.getcwd()  # get present working directory location here
    counter = 0  # keep a count of all files found
    csvfiles = []  # list to store all csv files found at location
    filebeginwithhello = []  # list to keep all files that begin with 'hello'
    otherfiles = []  # list to keep any other file that do not match the criteria

    for file in os.listdir(folderName):
        try:
            if file.endswith((".mid",".mxl")):
                print("mxl file found:\t", file)
                generateString(file,folderName);
                csvfiles.append(str(file))
                counter = counter + 1
        except Exception as e:
            raise e
            print("No files found here!")

    print("Total files found:\t", counter)

    generateCSV();
    print("-------- END ----------")

def generateSongArray(songString):
    for letter in songString:
        print(letter)

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


def pauseSearchForward(noteOrRests,ind,nlenOfPart):
    print("SONO NELLA RICORSIONE")
    print("LUNGHEZZA :  ",nlenOfPart)
    if(ind>=nlenOfPart):
        return -1
    if (noteOrRests[ind].isRest):
        return  pauseSearchForward(noteOrRests,ind+1,nlenOfPart)
    if (noteOrRests[ind].isNote):
        print("termina")
        return ind
    if (noteOrRests[ind].isChord):
        print("termina")
        return ind


def generateString(songName,folderName):
    path="./"+folderName+"/"+songName
    song = m.converter.parse(path)
    i = 0;

    s2 = '';
    s3='';
    # Snippet per recuperare il numero di note del primo spartito
    # partStream è l' array degli strumenti
    # parStream[0] rappresenta il primo spartito
    partStream = song.parts.stream()
    # print(partStream[0])
    # Questa riga sottostante permette di recuperare il numero di note del primo spartito (o primo strumento)
    # NB: nel numero totale sono incluse anche le pause (oltre le note effettive)
    lenOfPart = partStream[0].recurse().notesAndRests
    # print(len(lenOfPart))
    nlenOfPart = len(lenOfPart)
    # for p in partStream:
    #  print(p.id)

    it = iter(range(0, nlenOfPart))

    print('pitch, duration_string, duration, tie, midi pitch, octave')
    for i in it:
        a = song.recurse().notesAndRests[i]
        # print(a)
        print('... ', i, ' ...')

        if (a.isRest):
            print("PAUSA")
            duration=a.duration.quarterLength

            if (duration<1):
                duration = str(duration)
                s3 = s3 + "p" + duration
            else:
                duration=round(duration)
                duration=str(duration)
                s3=s3 + "p"+ duration


        if (a.isNote):
            print("NOTA")
            print("indice utile aggiornato in note: ", i)
            indUtile = pauseSearch(song.recurse().notesAndRests, i - 1)
            print("INDICE :", indUtile)
            if (indUtile <= -1):
                print("NON FARE NULLA")
            else:
                if (song.recurse().notesAndRests[indUtile].isChord):
                    max = 0;
                    maxDur = 0;
                    for x in song.recurse().notesAndRests[indUtile]._notes:
                        if (x.pitch.ps > max):
                            max = x.pitch.ps
                            maxD = x.duration.quarterLength

                    pitchCorrente = a.pitch.ps
                    pitchPrec = max;
                    pitchDiff = pitchCorrente - pitchPrec
                    pitchDiff = round(pitchDiff)
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';

                    #Calcolo Seconda Rappresentazione (pitch*duration)

                    pitchCorrente = a.pitch.ps * a.duration.quarterLength
                    pitchPrec = max * maxD;
                    pitchDiff = pitchCorrente - pitchPrec
                    print("OPERAZIONE :",pitchCorrente," - ",pitchPrec)

                    if (isinstance(pitchDiff, float)):
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';
                    else:
                        pitchDiff = round(pitchDiff)
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';


                if (song.recurse().notesAndRests[indUtile].isNote):
                    pitchCorrente = a.pitch.ps
                    pitchPrec = song.recurse().notesAndRests[indUtile].pitch.ps;
                    print("OPERAZIONE: ",pitchCorrente, " - ",pitchPrec)
                    pitchDiff = pitchCorrente - pitchPrec
                    # Cast from Float to String
                    pitchDiff = round(pitchDiff)
                    # Cast from String to Float
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';

                    #Calcolo Seconda Rappresentazione (pitch*duration)

                    pitchCorrente = a.pitch.ps * a.duration.quarterLength
                    pitchPrec = song.recurse().notesAndRests[indUtile].pitch.ps * song.recurse().notesAndRests[indUtile].duration.quarterLength;
                    pitchDiff = pitchCorrente - pitchPrec
                    print("OPERAZIONE :",pitchCorrente," - ",pitchPrec)

                    if (isinstance(pitchDiff, float)):
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';
                    else:
                        pitchDiff = round(pitchDiff)
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';

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
                            notaChord = x

                    pitchCorrente = 0;
                    pitchCorrenteD = 0;
                    for x in a._notes:
                        if (x.pitch.ps > pitchCorrente):
                            pitchCorrente = x.pitch.ps
                            pitchCorrenteD = x.duration.quarterLength
                            notaChord = x

                    pitchDiff = pitchCorrente - pitchPrec
                    pitchDiff = round(pitchDiff)
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';


                    #Calcolo Seconda Rappresentazione (pitch*duration)

                    pitchCorrente= pitchCorrente* pitchCorrenteD
                    pitchPrec= pitchPrec* pitchPrecD
                    pitchDiff=pitchCorrente-pitchPrec
                    print("OPERAZIONE :",pitchCorrente," - ",pitchPrec)

                    if (isinstance(pitchDiff, float)):
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';
                    else:
                        pitchDiff = round(pitchDiff)
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';


                if (song.recurse().notesAndRests[indUtile].isNote):
                    pitchCorrente = 0;
                    pitchCorrenteD = 0;
                    for x in a._notes:
                        if (x.pitch.ps > pitchCorrente):
                            pitchCorrente = x.pitch.ps
                            pitchCorrenteD = x.duration.quarterLength
                            notaChord = x

                    pitchPrec = song.recurse().notesAndRests[indUtile].pitch.ps;

                    pitchDiff = pitchCorrente - pitchPrec
                    # Cast from Float to String
                    pitchDiff = round(pitchDiff)
                    # Cast from String to Float
                    pitchDiff = str(pitchDiff)
                    s2 = s2 + pitchDiff + '*';

                    #Calcolo Seconda Rappresentazione (pitch*duration)

                    pitchPrec= song.recurse().notesAndRests[indUtile].pitch.ps *  song.recurse().notesAndRests[indUtile].duration.quarterLength
                    pitchCorrente=pitchCorrente* pitchCorrenteD
                    pitchDiff = pitchCorrente - pitchPrec
                    print("OPERAZIONE :",pitchCorrente," - ",pitchPrec)
                    if (isinstance(pitchDiff, float)):
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';
                    else:
                        pitchDiff = round(pitchDiff)
                        pitchDiff = str(pitchDiff)
                        s3 = s3 + pitchDiff + '*';





    # s2=s2.replace("p*p","p")
    # s2=s2.replace("p*p*p","p")
    # s2=s2.replace("p*p*p*p","p")
    s3= s3.replace("*", "");
    s3= s3.replace(".0", "");

    print(s3)

    #generateSongArray(s2)

    #Aggiungo un nuovo elemento nella lista delle canzoni di cui ho effettuato il Parsing
    songParseList.append(SongParse(songName,s3))

    print("Done.")




folderRead('Parts')