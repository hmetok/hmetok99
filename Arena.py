#!/usr/bin/env python3


class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def _vykresli(self):
        self._vycisti()
        print('--------Arena-------\n')
        print('Bojovnik: \n')
        self._vypis_bojovnika(self._bojovnik_1)
        self._vypis_bojovnika(self._bojovnik_2)


    def _vycisti(self):
        import sys as _sys
        import subprocess as _subporocess 
        if _sys.platform.startswith('win'):
            _subporocess.call(['cmd.exe', '/C', 'cls'])
        else:
            _subporocess.call(['clear'])    

    def _vypis_bojovnika(self,bojovnik):
        print(bojovnik)
        print(f'Zivot: {bojovnik.graficky_zivot()}')

    def zapas(self):
        print("Vitejte v arene")
        print(f'Dnes se utkaji {self._bojovnik_1} a {self._bojovnik_2}!')
        print('Zapas muze zacit...', end='  ' )

        while self._bojovnik_1.nazivu and self._bojovnik_2.nazivu:
            self._bojovnik_1.utoc(self._bojovnik_2) 
            self._vykresli()
            self._bojovnik_2.utoc(self._bojovnik_1)
            self._vykresli()


if __name__=='__main__':
    from kostka1 import Kostka
    from bojovnik import Bojovnik
    k = Kostka(10)
    b1 = Bojovnik('Honza', 100, 30, 40, k)
    b2 = Bojovnik('Adam', 110, 30, 20, k)

    a = Arena(b1, b2, k)
    a.zapas()