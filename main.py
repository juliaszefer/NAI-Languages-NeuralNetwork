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


def train(perceptronn, v_trainlist, lang, leng):
    czydalejj = True
    while czydalejj:
        good = 0
        for traintext in v_trainlist:
            v_type = traintext.language
            czynauczon = perceptronn.czynauczony(traintext.vector)
            odp = decision(czynauczon, lang)
            if odp == v_type:
                good += 1
            else:
                perceptronn.naucz(not czynauczon, czynauczon, traintext.vector)
        accuracy = howaccurate(good, len(v_trainlist)/leng)
        print(f"Ogolna poprawnosc {lang}: {accuracy}%\n")
        if accuracy > 99:
            czydalejj = False
        else:
            ask = input("powtorzyc nauczanie? (y/n)\n")
            if ask == "n":
                czydalejj = False


trainset = list()

for lan in languages:
    ppath = f"{dirpath}/{lan}"
    length = os.listdir(ppath)
    count = len(length)
    for number in range(count):
        ppath = f"{dirpath}/{lan}/{number+1}.txt"
        trainset += readfile(ppath, number, 'train')

perclist = list()
for lan in languages:
    perceptron = Perceptron(26, 0.5, 1, 2)
    train(perceptron, trainset, lan, len(languages))
    perclist.append(perceptron)

testpath = f"{dirpath}/Test"
testlist = list()

testlen = os.listdir(testpath)
ctr = len(testlen)
for number in range(ctr):
    ppath = f"{testpath}/{number + 1}.txt"
    testlist += readfile(ppath, number, 'test')

