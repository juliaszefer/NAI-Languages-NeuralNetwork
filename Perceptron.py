class Perceptron:
    def __init__(self, length, a, prog, start):
        self.vectorwag = list()
        for i in range(length):
            self.vectorwag.append(start)
        self.a = a
        self.prog = prog

# metoda sprawdzajaca czy perceptron zostal juz nauczony na bazie iloczynu skalarnego
# podanego wektora i wektora wag i tego czy jest wiekszy lub rowny progowi perceptronu
    def czynauczony(self, vector):
        if len(vector) != len(self.vectorwag):
            quit("Podany wektor i wektor wag nie sa tej samej dlugosci")
        suma = 0
        for i in range(len(vector)):
            suma += vector[i] * self.vectorwag[i]
        return suma >= self.prog

    def czyaktywowany(self, vector):
        if len(vector) != len(self.vectorwag):
            quit("Podany wektor i wektor wag nie sa tej samej dlugosci")
        suma = 0
        for i in range(len(vector)):
            suma += vector[i] * self.vectorwag[i]
        return suma

# nauczanie na bazie ponizszego wzoru
# W' = W + (d-y) * alfa * X
    def naucz(self, przewidywana, otrzymana, vector):
        rightside = (przewidywana - otrzymana)*self.a
        for i in range(len(vector)):
            vector[i] = vector[i]*rightside
        for i in range(len(vector)):
            self.vectorwag[i] += vector[i]
        self.prog += rightside*(-1)
