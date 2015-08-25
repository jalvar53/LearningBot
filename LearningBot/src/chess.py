# -*- coding: utf-8 -*-

import fichas

class Tablero():
    strTab = ""
    puntaje = 0
    turno = 0
    tablero = []
    #Constructor de la clase Tablero
    def __init__(self, tab):
        self.strTab = tab
        self.tablero = []
        #Funciones que crean las fichas y las agregan a tablero
        def casillaBlanca():
            self.tablero.append(fichas.casilla("Blanco"))
        def casillaNegra():
            self.tablero.append(fichas.casilla("Negro"))
        def peonBlanco(i):
            self.tablero.append(fichas.peon(i,"Blanco"))
        def peonNegro(i):
            self.tablero.append(fichas.peon(i,"Negro"))
        def torreBlanca():
            self.tablero.append(fichas.torre("Blanco"))
        def torreNegra():
            self.tablero.append(fichas.torre("Negro"))
        def alfilBlanco():
            self.tablero.append(fichas.alfil("Blanco"))
        def alfilNegro():
            self.tablero.append(fichas.alfil("Negro"))
        def caballoBlanco():
            self.tablero.append(fichas.caballo("Blanco"))
        def caballoNegro():
            self.tablero.append(fichas.caballo("Negro"))
        def reinaBlanca():
            self.tablero.append(fichas.reina("Blanco"))
        def reinaNegra():
            self.tablero.append(fichas.reina("Negro"))
        def reyBlanco():
            self.tablero.append(fichas.rey("Blanco"))
        def reyNegro():
            self.tablero.append(fichas.rey("Negro"))
        def juegaBlanco():
            turno = 0
        def juegaNegro():
            turno = 1
        #"Switch case" para los caracteres de cada ficha con su respectivo
        #codigo ASCII
        options = {98: casillaBlanca,   #b
                    66: casillaNegra,   #B
                    112: peonBlanco,    #p
                    80: peonNegro,      #P
                    116: torreBlanca,   #t
                    84: torreNegra,     #T
                    97: alfilBlanco,    #a
                    65: alfilNegro,     #A
                    99: caballoBlanco,  #c
                    67: caballoNegro,   #C
                    114: reinaBlanca,   #r
                    82: reinaNegra,     #R
                    107: reyBlanco,     #k
                    75: reyNegro,       #K
                    48: juegaBlanco,    #0
                    49: juegaNegro,     #1
        }

        #Asignacion de las fichas creadas al tablero
        for j in range(len(tab)):
            a = ord(tab[j])
            if(a == 112  or a == 80):
                options[a](j)
            else:
                options[a]()

