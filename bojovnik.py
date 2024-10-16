#!/usr/bin/env python3


class Bojovnik:
    '''
    Trida reprezentujici bojovnika
    '''
    
    def __init__ (self, jmeno, zivot, utok, obrana, kostka):
        self.jmeno = jmeno
        self.zivot = zivot
        self.max_zivot = zivot 
        self.utok = utok
        self.obrana = obrana
        self.kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self.jmeno) 

    @property 
    def nazivu(self):
        return self.zivot > 0

    def utoc(self, souper):
        uder = self.utok + self.kostka.hod()
        souper.bran_se(uder)
    
    def graficky_zivot(self):
        celkem = 20
        pocet = int(self.zivot / self.max_zivot * celkem)
        return f'[{"#" * pocet}{" "*(celkem-pocet)}]'

    def bran_se(self, uder):
        zraneni = uder - (self.obrana + self.kostka.hod())
        if zraneni > 0:
            self.zivot = self.zivot - zraneni
            zprava = f'{self.jmeno} utrpel zraneni o sile {zraneni}'
            if self.zivot <= 0:
                self.zivot = 0
                zprava = zprava + ' a zemrel.'
        else:
            zprava = f'{self.jmeno} zcela odrazil utok'
        self.set_zprava(zprava)

    def set_zprava(self, zprava):
        self._zprava = zprava 

    def get_zprava(self):
        return self._zprava




if __name__=='__main__':
    import kostka1
    andrej = Bojovnik('Andrej', 70, 50, 40, kostka1.Kostka(20))
    mira = Bojovnik('Mirek', 100, 40, 50, kostka1.Kostka(20))
    print(andrej.jmeno, andrej.zivot, andrej.utok, andrej.obrana)
    print(mira.jmeno, mira.zivot, mira.utok, mira.obrana)

    andrej.utoc(mira)
    print(mira.get_zprava())
    print(mira.graficky_zivot(mira.zivot,mira.max_zivot))