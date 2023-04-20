import os
from Text import Text
from Perceptron import Perceptron

dirpath = "Data"
dirlist = os.listdir(dirpath)

languages = list()
for ii in dirlist:
    if os.path.isdir(os.path.join(dirpath, ii)):
        languages.append(ii)

languages = sorted(languages)


def sortline(line, fpath, numberr, testortrain):
    lista = list(line)
    a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z \
        = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for letter in lista:
        if letter == 'a':
            a += 1
        elif letter == 'b':
            b += 1
        elif letter == 'c':
            c += 1
        elif letter == 'd':
            d += 1
        elif letter == 'e':
            e += 1
        elif letter == 'f':
            f += 1
        elif letter == 'g':
            g += 1
        elif letter == 'h':
            h += 1
        elif letter == 'i':
            i += 1
        elif letter == 'j':
            j += 1
        elif letter == 'k':
            k += 1
        elif letter == 'l':
            ll += 1
        elif letter == 'm':
            m += 1
        elif letter == 'n':
            n += 1
        elif letter == 'o':
            o += 1
        elif letter == 'p':
            p += 1
        elif letter == 'q':
            q += 1
        elif letter == 'r':
            r += 1
        elif letter == 's':
            s += 1
        elif letter == 't':
            t += 1
        elif letter == 'u':
            u += 1
        elif letter == 'v':
            v += 1
        elif letter == 'w':
            w += 1
        elif letter == 'x':
            x += 1
        elif letter == 'y':
            y += 1
        elif letter == 'z':
            z += 1
    suma = a+b+c+d+e+f+g+h+i+j+k+ll+m+n+o+p+q+r+s+t+u+v+w+x+y+z
    a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z = a/suma, b/suma, c/suma, d/suma,\
        e/suma, f/suma, g/suma, h/suma, i/suma, g/suma, k/suma, ll/suma, m/suma, n/suma, o/suma, p/suma, q/suma,\
        r/suma, s/suma, t/suma, u/suma, v/suma, w/suma, x/suma, y/suma, z/suma
    vector = list()
    vector.extend((a, b, c, d, e, f, g, h, i, j, k, ll, m, n, o, p, q, r, s, t, u, v, w, x, y, z))
    if testortrain == 'train':
        fpath = fpath.replace("Data/", "")
        fpath = fpath.replace(f".txt", "")
        fpath = fpath.replace("/", "")
        fpath = fpath.replace(str(numberr+1), "")
        text1 = Text(vector, fpath)
    else:
        text1 = Text(vector, "default")
    return text1


def readfile(fpath, numberr, testortrain):
    arr = list()
    ffile = open(fpath, 'r')
    oneline = ""
    for line in ffile:
        oneline += line
    arr.append(sortline(oneline.replace("\n", ""), fpath, numberr, testortrain))
    return arr


def howaccurate(correctno, allno):
    return correctno/allno*100


def decision(isgood, language):
    if isgood:
        return language
    else:
        return "other"


def train(perceptronlista, v_trainlist, desiredvalues):
    czydalejj = True
    while czydalejj:
        checklist = list()
        for nr in range(len(v_trainlist)):
            for numr in range(len(v_trainlist[nr])):
                for pernr in range(len(perceptronlista)):
                    czynauczon = perceptronlista[pernr].czynauczony(v_trainlist[nr][numr].vector)
                    # print(czynauczon)
                    print(f"desired: {desiredvalues[nr][pernr]} == {czynauczon}")

                    if desiredvalues[nr][pernr] == int(czynauczon):
                        perceptronlista[pernr].setczyucz(False)
                        print(v_trainlist[nr][numr].language)
                    else:
                        print("musial sie nauczyc")
                        perceptronlista[pernr].setczyucz(True)
                print(' ')
                for percnr in range(len(perceptronlista)):
                    if perceptronlista[percnr].czyucz:
                        perceptronlista[percnr].naucz(desiredvalues[nr][percnr], not desiredvalues[nr][percnr],
                                                      v_trainlist[nr][numr].vector)
            print('petla sie skonczyla')
            ctrn = 0
            for pe in perceptronlista:
                if not pe.czyucz:
                    ctrn += 1
            if ctrn == 3:
                checklist.append(False)
        counter = 0
        for val in checklist:
            if not val:
                counter += 1
        if counter == 3:
            czydalejj = False


def decicisionwhichperc(perclistt, najblizej):
    for jj in range(len(perclistt)):
        if perclistt[jj].wynik == najblizej:
            # print(f"{perclistt[jj].wynik} == {najblizej} {jj} {perclistt[jj].language}")
            return perclistt[jj]


def test(perclistt, testlistt, accurlist):
    good = 0
    for i in range(len(testlistt)):
        wyniklist = list()
        for j in range(len(perclistt)):
            wynikk = perclistt[j].czyaktywowany(testlistt[i].vector)
            perclistt[j].setwynik(wynikk)
            wyniklist.append(wynikk)
        najblizej = max(wyniklist)
        activeperc = decicisionwhichperc(perclistt, najblizej)
        if activeperc.language == accurlist[i]:
            good += 1
    accuracy = howaccurate(good, len(testlistt))
    print(f"Ogolna poprawnosc: {accuracy}%\n")


trainset = list()

for lan in languages:
    tmpset = list()
    ppath = f"{dirpath}/{lan}"
    length = os.listdir(ppath)
    count = len(length)
    for number in range(count):
        ppath = f"{dirpath}/{lan}/{number+1}.txt"
        tmpset += readfile(ppath, number, 'train')
    trainset.append(tmpset)


perclist = list()
for lan in languages:
    perceptron = Perceptron(26, 0.5, 1, 2, lan)
    perclist.append(perceptron)

desired = list()
for j in range(len(languages)):
    tmp = list()
    for i in range(len(languages)):
        if i == j:
            tmp.append(1)
        else:
            tmp.append(0)
    desired.append(tmp)

train(perclist, trainset, desired)

testpath = "Test"
testlist = list()

testlen = os.listdir(testpath)
ctr = len(testlen)
for number in range(ctr):
    ppath = f"{testpath}/{number + 1}.txt"
    testlist += readfile(ppath, number, 'test')

accuracylist = list()
fille = open("Accuracy.txt", 'r')
for line in fille:
    accuracylist.append(line.replace("\n", ""))

test(perclist, testlist, accuracylist)
