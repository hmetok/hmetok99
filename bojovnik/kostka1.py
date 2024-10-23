#!/usr/bin/env python3



import random


class Kostka:


    '''
    trida reprezentujici hraci kostku
    '''

    def __init__(self, pocet_sten=6):
        self.pocet_sten = pocet_sten

    def __str__(self):
         return f'Kostka s {self.pocet_sten} stenami.'

    def hod(self):
        return(random.randint(1,self.pocet_sten))

    def get_pocet_sten(self):
        return self.pocet.sten

    def set_pocet_sten(self, novy_pocet_sten):
        try:
            novy_pocet_sten = int(novy_pocet_sten)
            if novy_pocet_sten > 0:
                self.pocet_sten = novy_pocet_sten
            else:    
                print ('novy_pocet_sten musi byt > 0')
        except:
            print('Cislo musi byt kladne cele cislo')
