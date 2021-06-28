from math import gcd


class Fraction(object):
    """
    O fractie este compusa din numarator si numitor.
    Se poate initializa ca o fractie ireductibila prin parametrul irreducible=True.
    """

    def __init__(self, _numarator, _numitor, irreducible=False):
        if irreducible:
            cmmdc = gcd(_numarator, _numitor)
            self.numarator = int(_numarator / cmmdc)
            self.numitor = int(_numitor / cmmdc)
        else:
            self.numarator = _numarator
            self.numitor = _numitor

    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    def __add__(self, other):
        if self.numitor == other.numitor:
            new_fraction = Fraction(self.numarator + other.numarator, other.numitor)
            new_fraction.reduce_fraction()
            return new_fraction
        else:
            self_numarator = self.numitor

            self.numarator *= other.numitor
            self.numitor *= other.numitor

            other.numarator *= self_numarator
            other.numitor *= self_numarator

            new_fraction = Fraction(self.numarator + other.numarator, other.numitor)
            new_fraction.reduce_fraction()
            return new_fraction

    def __sub__(self, other):
        if self.numitor == other.numitor:
            new_fraction = Fraction(self.numarator - other.numarator, other.numitor)
            new_fraction.reduce_fraction()
            return new_fraction
        else:
            self_numarator = self.numitor

            self.numarator *= other.numitor
            self.numitor *= other.numitor

            other.numarator *= self_numarator
            other.numitor *= self_numarator

            new_fraction = Fraction(self.numarator - other.numarator, other.numitor)
            new_fraction.reduce_fraction()
            return new_fraction

    def reduce_fraction(self):
        cmmdc = gcd(self.numarator, self.numitor)
        self.numarator = int(self.numarator / cmmdc)
        self.numitor = int(self.numitor / cmmdc)

    def inverse(self):
        return Fraction(self.numitor, self.numarator, irreducible=True)


fractie1 = Fraction(20, 4, irreducible=True)
fractie2 = Fraction(4, 5, irreducible=True)

print(f'Fractie 1: {fractie1}   Fractie 2: {fractie2}')
print(f'Suma: {fractie1 + fractie2}')
print(f'Diferenta: {fractie1 - fractie2}')
print(f'Inversa fractiei 1: {fractie1.inverse()}')
print(f'Inversa fractiei 2: {fractie2.inverse()}')
