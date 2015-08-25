#Archivo de inicializacion del programa
#Desde aqui se carga la memoria guardada anterior
#Y se crea la memoria al final de la ejecucion
import chess
import fichas
import random
import os.path
import turno


actual = []

def main():
    #Se verifica si existe una memoria para cargar
    if os.path.exists("./infografo.txt"):
        #Se carga en el grafo esta informacion
        arch = open('./infografo.txt', 'r')
        linea = arch.readline()
        posicion = 0
        while linea != "":
            infotab = linea
            tabinfo = infotab[:65]
            puntinfo = infotab[65:]
            n = chess.Tablero(tabinfo)
            n.puntaje = puntinfo
            turno.grafo.append(n)
            turno.tabs[tabinfo] = posicion
            arisinfo = arch.readline()
            i = 0
            listaris = []
            while i < len(arisinfo):
                aux = ""
                while i < len(arisinfo) and arisinfo[i] != ",":
                    aux = aux + arisinfo[i]
                    i = i+1
                if (aux != '' and aux != '\n'):
                    print ord(aux)
                    entero = int(aux)
                    listaris.append(entero)
                i = i+1
            turno.aristas.append(listaris)
            linea = arch.readline()
            posicion = posicion + 1
        arch.close()
        os.remove("./infografo.txt")
    #Se verifica si no se cargo ninguna informacion de la memoria
    #Si esto sucede se agrega el tablero inicial
    if(len(turno.grafo) == 0):
        st = "TCARKACTPPPPPPPPbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbpppppppptcarkact0"
        #st = "bBbKbAbBBbBbBbBbbPbPbBbBBbtbBbBRbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
        #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBBbBbBbBbBBbBbBbBbPBbBbPbBBbBbBbBb1"
        #st = "bBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbRBbBbBbBb1"
        #st = "bBbBbBbBBbBbBbBbbBbBbBbBCbBbBbBbbBbBbBbBBbBbBbBbbBbBbBbCBbBbBbBb1"
        #st = "bbBbBbBbBCbBbBbBpppppppppppppppppppppppppppppCCCPPPppppPPPppPPpp0"
        #st = "bbbbbbbbbbbbbbbbbbbrrrrbbbbbbbbbbbbbbbbbKbbbbbbbbbbbbbbbbbbbbbbb0"
        m = chess.Tablero(st)
        turno.tabs[st] = 0
        turno.grafo.append(m)
        a = []
        turno.aristas.append(a)
    archivo = open('infografo.txt', 'w')
    jugar = 1
    while jugar:
        m = turno.grafo[0]
        b = 1
        while b:
            #Se comienza el juego como un ciclo de turnos
            blancas = []
            actual.append(turno.tabs[m.strTab])
            juego = turno.juegaHM(m)
            #Se verifica si hay jaque mate en el tablero del jugador humano
            if juego == 0:
                print ('Jaque mate, gana learningbot')
                turno.grafo[tabs[m.strTab]].puntaje = \
                turno.grafo[tabs[m.strTab]].puntaje + 20
                break
            elif juego == 1:
                print ('Tablas, Rey blanco ahogado')
                turno.grafo[tabs[m.strTab]].puntaje = \
                turno.grafo[tabs[m.strTab]].puntaje + 5
                break
            #Juega la computadora, creando los posibles movimientos
            #Se elige el mejor en base de un puntaje
            turno.posib(juego)
            pos = turno.tabs[juego.strTab]
            actual.append(pos)
            posibles = []
            maximo = 0
            for i in range(len(turno.aristas[pos])):
                tabAux = turno.grafo[turno.aristas[pos][i]]
                if (tabAux.puntaje == maximo):
                    posibles.append(tabAux)
                elif (tabAux.puntaje > maximo):
                    posibles = []
                    posibles.append(tabAux)
                    maximo = tabAux.puntaje
            if (len(posibles) == 0):
                turno.imprimirTablero(juego)
                mate = chess.Tablero(juego.strTab[:64] + '0')
                if (turno.jaque(mate)):
                    print('Jaque mate, gana jugador humano')
                    turno.grafo[pos].puntaje = turno.grafo[pos].puntaje - 20
                else:
                    print('Tablas, Rey negro ahogado')
                    turno.grafo[pos].puntaje = turno.grafo[pos].puntaje + 5
                b = 0
            else:
                ran = random.randrange(len(posibles))
                m = posibles[ran]
        suma = 0
        for i in range(len(actual)):
            aux = len(actual) - i - 1
            punt = turno.grafo[actual[aux]].puntaje
            suma = suma + punt
            turno.grafo[actual[aux]].puntaje = suma
        rpta = raw_input('Desea un nuevo juego? (Y/N):')
        if rpta == "n" or rpta == "N":
            jugar = 0
    #Se crea una memoria como archivo de texto con la informacion del grafo
    for i in range(len(turno.grafo)):
        cadenaux = turno.grafo[i].strTab + str(turno.grafo[i].puntaje)
        archivo.write(cadenaux)
        archivo.write('\n')
        nodoaux = ""
        for j in range(len(turno.aristas[i])):
            nodoaux = nodoaux + str(turno.aristas[i][j]) + ","
        archivo.write(nodoaux)
        archivo.write('\n')
    archivo.close()
main()
