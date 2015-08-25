import chess
import fichas
import random
grafo = []
aristas = []
tabs = {}
blancas = []

#Define la funcion del color que debe de ir la casilla cuando esta
#vacia el tablero
def colorCasilla(pos):
    div = pos/8
    mod = pos%2
    moddiv = div%2
    if moddiv == 0:
        if mod == 0:
            return "b"
        return "B"
    if mod == 0:
        return "B"
    return "b"

#Funcion que verifica si en un tablero existe el jaque
def jaque(tab):
    a = 0
    jug = 0
    if (tab.strTab[64] == '0'):
        a = tab.strTab.find('K')
        jug = 1
    else:
        a = tab.strTab.find('k')
    seg = 1
    mov = 1
    #Verifica si hay jaque al rey hacia arriba.
    while seg:
        aux = a + 8*mov
        if (aux < 64):
            if (tab.tablero[aux].jugador == "n"):
            #Verifica si esta vacia la casilla
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
            #Verifica si en la casilla hay una pieza propia
                seg = 0
            else:
                if (-8) in tab.tablero[aux].come  \
                and mov in tab.tablero[aux].movimientos:
                #Verifica si la casilla que hace el jaque si puede
                #hacer el movimiento para comer
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque al rey hacia abajo.
    while seg:
        aux = a - 8*mov
        if(aux >= 0):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (8) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque desde la derecha.
    while seg:
        aux = a + 1*mov
        #Condiciona si el jaque es en la misma fila
        if (a/8 == aux/8):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-1) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica si hay jaque desde la izquierda.
    while seg:
        aux = a - 1*mov
        if (a/8 == aux/8):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (1) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal abajo derecha
    while seg:
        aux = a + 9*mov
        if (aux < 64 and a/8 == aux/8 - mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-9) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal arriba izquierda
    while seg:
        aux = a - 9*mov
        if (aux >= 0 and a/8 == aux/8 + mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (9) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal abajo a la izquierda
    while seg:
        aux = a + 7*mov
        if (aux < 64 and a/8 == aux/8 - mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (-7) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0
    seg = 1
    mov = 1
    #Verifica el jaque desde la diagonal derecha arriba
    while seg:
        aux = a - 7*mov
        if (aux >= 0 and a/8 == aux/8 + mov):
            if (tab.tablero[aux].jugador == "n"):
                mov = mov + 1
            elif (tab.tablero[aux].jugador == jug):
                seg = 0
            else:
                if (7) in tab.tablero[aux].come \
                and mov in tab.tablero[aux].movimientos:
                    return 1
                else:
                    seg = 0
        else:
            seg = 0

    #Verifica los jaques para el caballo
    aux = a - 17
    if (aux >= 0 and a/8 == aux/8 + 2 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a - 15
    if (aux >= 0 and a/8 == aux/8 + 2 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a - 10
    if (aux >= 0 and a/8 == aux/8 + 1 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a - 6
    if (aux >= 0 and a/8 == aux/8 + 1 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a + 6
    if (aux < 64 and a/8 == aux/8 - 1 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a + 10
    if (aux < 64 and a/8 == aux/8 - 1 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a + 17
    if (aux < 64 and a/8 == aux/8 - 2 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    aux = a + 15
    if (aux < 64 and a/8 == aux/8 - 2 and tab.tablero[aux].jugador != jug):
        if (tab.tablero[aux].type().lower() == 'c'):
            return 1
    return 0



#Funcion que imprime un tablero dado
def imprimirTablero(tab):
    for i in range (8):
        print 8-i,
        for j in range (8):
            aux = tab.tablero[i*8+j]
            print aux.tostring(),
        print
    print ("  A B C D E F G H")
    print ("-----------------")
    print ("-----------------")

#Agrega un tablero al grafo, una lista a sus aristas
#y lo agrega al diccionaro con su string del tablero y la posicion del grafo
def agregarGrafo(origen, destino, puntaje):
    #Se verifica si el tablero esta en ya en el grafo o no
    if (destino.strTab in tabs):
        ax = tabs[destino.strTab]
        out = grafo[ax]
        if (ax not in aristas[tabs[origen.strTab]]):
            aristas[tabs[origen.strTab]].append(tabs[out.strTab])
    else:
        a = len(grafo)
        tabs[destino.strTab] = a
        destino.puntaje = puntaje
        grafo.append(destino)
        aristas[tabs[origen.strTab]].append(a)
        b = []
        aristas.append(b)

#Define la funcion para que juegue el humano
def juegaHM(origen):
    imprimirTablero(origen)
    a = 1
    cadAux = origen.strTab[:64] + '1'
    tbaux = chess.Tablero(cadAux)
    jaq = 0
    if (jaque(tbaux)):
        jaq = 1
        print ("Usted esta en jaque")
    posib(origen)
    #Llama a la funcion posib para sacar todas las posibles
    #jugadas que puede hacer el humano para determinar si esta en jaque
    if (len(blancas) == 0):
        if jaq:
            return 0
        else: 
            return 1
    while a: 
        l = raw_input('Su jugada a continuacion: ')
        if(len(l) != 5):
            print "Por favor repita su jugada"
            continue
        x = l.upper()
        #Se pone en mayusculas la cadena entrada para poder evaluar
        aux = ord(x[0]) - 65
        auxn = 8 - int(x[1])
        inp = auxn*8 + aux
        aux = ord(x[3]) - 65
        auxn = 8 - int(x[4])
        ops = auxn*8 + aux
        if(origen.tablero[inp].jugador == 0):
            if (origen.tablero[ops].jugador != 0):
                taux = 0
                ficha = origen.tablero[inp]
                #Ver si el humano va a coronar
                if (ficha.type() == 'p' and ops < 8):
                    f = raw_input('Que ficha desea coronar (c/a/t/r): ')
                    jugada = origen.strTab[:inp] + colorCasilla(inp) \
                            + origen.strTab[inp+1:ops]
                    jugada = jugada + f + origen.strTab[ops+1:64] + '1'
                    if (not jugada in blancas):
                        print ("No es posible su jugada")
                        continue
                else:
                    #Se crea el tablero con la jugada propuesta por el humano
                    if (inp < ops):
                        jugada = origen.strTab[:inp] + colorCasilla(inp) \
                                + origen.strTab[inp+1:ops]
                        jugada = jugada + origen.tablero[inp].type() \
                                + origen.strTab[ops+1:64] + '1'
                        taux = chess.Tablero(jugada)
                        score = 0
                        if (origen.tablero[ops].jugador == 1):
                            score = score - origen.tablero[ops].score
                        if (jugada in blancas):
                            agregarGrafo(origen, taux, score)
                        else:
                            print ("No es posible su jugada")
                            continue
                    else:
                        jugada = origen.strTab[:ops]+origen.tablero[inp].type()\
                                + origen.strTab[ops+1:inp]
                        jugada = jugada + colorCasilla(inp) + \
                                origen.strTab[inp+1:64] + '1'
                        taux = chess.Tablero(jugada)
                        taux = chess.Tablero(jugada)
                        score = 0
                        if (origen.tablero[ops].jugador == 1):
                            score = score - origen.tablero[ops].score
                        if (jugada in blancas):
                            agregarGrafo(origen, taux, score)
                        else:
                            print ("No es posible su jugada")
                            continue
                    a = 0
                    return taux
            else:
                print ("Error, no es posible moverse a esta posicion")
        else:
            print ("Error, no es posible mover esta ficha")
def posib(origen):
    #Funcion para crear todos los posibles movimientos en un tablero
    cad = origen.strTab
    jug = 0
    op = 1
    if origen.strTab[64] == '1':
        jug = 1
        op = 0
    for i in range (len(cad)-1):
        ficha = origen.tablero[i]
        #Se recorre todas las casillas del tablero y
        #se verifica que esta pertenezca al jugador
        #para luego crear todos los tableros con los movimientos de esta ficha
        if (cad[i] != 'b' and cad[i] != 'B' and ficha.jugador == jug):
            if (ficha.type() != 'C' and ficha.type() != 'P' \
                    and ficha.type() != 'c' and ficha.type() != 'p'):
                for j in range (len(ficha.direccion)):
                    for k in range (len(ficha.movimientos)):
                    #Recorre la cantidad de movimientos y la direccion que pueden
                    #tomar estos y verifica cual de estas es y crea el tablero
                        direc = ficha.direccion[j]
                        movi = ficha.movimientos[k]
                        aux = i+(direc*movi)
                        if ((direc == 1 and aux/8 == i/8) \
                        or (direc == 8 and aux < 64) \
                        or ((direc == 7 or direc == 9) \
                        and (aux < 64 and (aux/8 - movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (origen.strTab[64] == '1'):
                                if (posicion.jugador != 1):
                                    if (posicion.jugador == 0):
                                        fin = cad[0:i] + colorCasilla(i)\
                                              + cad[i+1:aux] + ficha.type() \
                                              + cad[aux+1:64] + '0'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            agregarGrafo(origen, taux,\
                                            origen.tablero[aux].score)
                                        break
                                    else:
                                        fin = cad[0:i] + colorCasilla(i)+\
                                              cad[i+1:aux] + ficha.type()\
                                              + cad[aux+1:64] + '0'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            agregarGrafo(origen, taux, 0)
                                else:
                                    break
                            elif (origen.strTab[64] == '0'):
                                if (posicion.jugador != 0):
                                    if (posicion.jugador == 0):
                                        fin = cad[0:i] + colorCasilla(i) + \
                                              cad[i+1:aux] + ficha.type() + \
                                              cad[aux+1:64] + '1'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            blancas.append(fin)
                                        break
                                    else:
                                        fin = cad[0:i] + colorCasilla(i) +\
                                              cad[i+1:aux] + ficha.type() +\
                                              cad[aux+1:64] + '1'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            blancas.append(fin)
                                else:
                                    break
                        elif ((direc == -1 and aux/8 == i/8) or (direc == -8\
                        and aux >= 0) or ((direc == -9 or direc == -7)\
                        and (aux >=0 and (aux/8 + movi == i/8)))):
                            posicion = origen.tablero[aux]
                            if (origen.strTab[64] == '1'):
                                if (posicion.jugador != 1):
                                    if (posicion.jugador == 0):
                                        fin = cad[0:aux] + ficha.type() +\
                                              cad[aux+1:i] + colorCasilla(i)+\
                                              cad[i+1:64] + '0'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            agregarGrafo(origen, taux,\
                                            origen.tablero[aux].score)
                                        break
                                    else:
                                        fin = cad[0:aux] + ficha.type() +\
                                              cad[aux+1:i] + colorCasilla(i) +\
                                              cad[i+1:64] + '0'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            agregarGrafo(origen, taux, 0)
                                else:
                                    break
                            elif (origen.strTab[64] == '0'):
                                if (posicion.jugador != 0):
                                    if (posicion.jugador == 0):
                                        fin = cad[0:aux] + ficha.type() +\
                                              cad[aux+1:i] + colorCasilla(i) +\
                                              cad[i+1:64] + '1'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            blancas.append(fin)
                                        break
                                    else:
                                        fin = cad[0:aux] + ficha.type() + \
                                              cad[aux+1:i] + colorCasilla(i) +\
                                              cad[i+1:64] + '1'
                                        taux = chess.Tablero(fin)
                                        if (jaque(taux) == 0):
                                            blancas.append(fin)
                                else:
                                    break
            elif (cad[i] == 'P'):
                auxc = i + 7
                if (auxc/8 - 1 == i/8 and auxc < 64 and \
                origen.tablero[auxc].jugador == 0):
                    if (auxc < 56):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + \
                            ficha.type() + cad[auxc+1:64] + '0'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            agregarGrafo(origen, taux, \
                            origen.tablero[auxc].score)
                    else:
                        arr = ['C', 'A', 'T', 'R']
                        for j in range(len(arr)):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] \
                                + arr[j] + cad[auxc+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                agregarGrafo(origen, taux, \
                                taux.tablero[auxc].score + \
                                origen.tablero[auxc].score)
                auxc = i + 9
                if (auxc/8 - 1 == i/8 and auxc < 64 and \
                origen.tablero[auxc].jugador == 0):
                    if (auxc < 56):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + \
                              ficha.type() + cad[auxc+1:64] + '0'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            agregarGrafo(origen, taux, \
                            origen.tablero[auxc].score)
                    else:
                        arr = ['C', 'A', 'T', 'R']
                        for j in range(len(arr)):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc]\
                                  + arr[j] + cad[auxc+1:64] + '0'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                agregarGrafo(origen, taux, \
                                taux.tablero[auxc].score + \
                                origen.tablero[auxc].score)
                auxc = i + 8
                if (auxc < 56 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + \
                          ficha.type() + cad[auxc+1:64] + '0'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 0):
                        agregarGrafo(origen, taux, 0)
                if (auxc > 55 and auxc < 64 and \
                origen.tablero[auxc].jugador == "n"):
                    arr = ['C', 'A', 'T', 'R']
                    for j in range(len(arr)):
                        fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxc] + \
                              arr[j] + cad[auxc+1:64] + '0'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            agregarGrafo(origen, taux, taux.tablero[auxc].score)
                auxd = i + 16
                if (i > 7 and i < 16 and origen.tablero[auxd].jugador == "n" \
                and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:i] + colorCasilla(i) + cad[i+1:auxd] + \
                          ficha.type() + cad[auxd+1:64] + '0'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 0):
                        agregarGrafo(origen, taux, 0)
            elif (cad[i] == 'p'):
                auxc = i - 7
                if (auxc/8 + 1 == i/8 and auxc >= 0 and \
                origen.tablero[auxc].jugador == 1):
                    if (auxc > 7):
                        fin = cad [0:auxc] + ficha.type() + cad[auxc+1:i] + \
                              colorCasilla(i) + cad[i+1:64] + '1'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            blancas.append(fin)
                    else:
                        arr = ['c', 'a', 't', 'r']
                        for j in range(len(arr)):
                            fin = cad [0:auxc] + arr[j] + cad[auxc+1:i] + \
                                  colorCasilla(i) + cad[i+1:64] + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                blancas.append(fin)
                auxc = i - 9
                if (auxc/8 + 1 == i/8 and auxc >= 0 and \
                origen.tablero[auxc].jugador == 1):
                    if (auxc > 7):
                        fin = cad [0:auxc] + ficha.type() + cad[auxc+1:i] + \
                              colorCasilla(i) + cad[i+1:64] + '1'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            blancas.append(fin)
                    else:
                        arr = ['c', 'a', 't', 'r']
                        for j in range(len(arr)):
                            fin = cad [0:auxc] + arr[j] + cad[auxc+1:i] + \
                                  colorCasilla(i) + cad[i+1:64] + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                blancas.append(fin)
                auxc = i - 8
                if (auxc >= 0 and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:auxc] + ficha.type() + cad[auxc+1:i] + \
                          colorCasilla(i) + cad[i+1:64] + '1'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 0):
                        blancas.append(fin)
                if (auxc >= 0 and auxc < 8 and \
                origen.tablero[auxc].jugador == "n"):
                    arr = ['C', 'A', 'T', 'R']
                    for j in range(len(arr)):
                        fin = cad [0:auxc] + arr[j] + cad[auxc+1:i] + \
                              colorCasilla(i) + cad[i+1:64] + '1'
                        taux = chess.Tablero(fin)
                        if (jaque(taux) == 0):
                            blancas.append(fin)
                auxd = i - 16
                if (i > 47 and i < 56 and origen.tablero[auxd].jugador == "n" \
                and origen.tablero[auxc].jugador == "n"):
                    fin = cad [0:auxd] + ficha.type() + cad[auxd+1:i] + \
                            colorCasilla(i) + cad[i+1:64] + '1'
                    taux = chess.Tablero(fin)
                    if (jaque(taux) == 0):
                        blancas.append(fin)
            elif (cad[i] == 'C' or cad[i] == 'c'):
                    def compar(aux, mi):
                        if (aux/8 - mi == i/8 and aux < 64 and \
                        origen.tablero[aux].jugador == "n"):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + \
                                  ficha.type() + cad[aux+1:64]
                            if (origen.strTab[64] == '1'):
                                fin = fin + '0'
                            else:
                                fin = fin + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                if (origen.strTab[64] == '1'):
                                    agregarGrafo(origen, taux, 0)
                                else:
                                    blancas.append(fin)
                        elif (aux/8 - mi == i/8 and aux < 64 and \
                        origen.tablero[aux].jugador == op):
                            fin = cad [0:i] + colorCasilla(i) + cad[i+1:aux] + \
                                  ficha.type() + cad[aux+1:64]
                            if (origen.strTab[64] == '1'):
                                fin = fin + '0'
                            else:
                                fin = fin + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                if (origen.strTab[64] == '1'):
                                    agregarGrafo(origen, taux, \
                                    origen.tablero[aux].score)
                                else:
                                    blancas.append(fin)
                    def commin(aux, mi):
                        if (aux/8 + mi == i/8 and aux >= 0 and \
                        origen.tablero[aux].jugador == "n"):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + \
                                  colorCasilla(i) + cad[i+1:64]
                            if (origen.strTab[64] == '1'):
                                fin = fin + '0'
                            else:
                                fin = fin + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                if (origen.strTab[64] == '1'):
                                    agregarGrafo(origen, taux, 0)
                                else:
                                    blancas.append(fin)
                        if (aux/8 + mi == i/8 and aux >= 0 and \
                        origen.tablero[aux].jugador == op):
                            fin = cad [0:aux] + ficha.type() + cad[aux+1:i] + \
                                  colorCasilla(i) + cad[i+1:64]
                            if (origen.strTab[64] == '1'):
                                fin = fin + '0'
                            else:
                                fin = fin + '1'
                            taux = chess.Tablero(fin)
                            if (jaque(taux) == 0):
                                if (origen.strTab[64] == '1'):
                                    agregarGrafo(origen, taux, \
                                    origen.tablero[aux].score)
                                else:
                                    blancas.append(fin)
                    aux = i + 15
                    compar(aux, 2)
                    aux = i + 17
                    compar(aux,2)
                    aux = i + 10
                    compar(aux,1)
                    aux = i + 6
                    compar(aux,1)
                    aux = i - 10
                    commin(aux, 1)
                    aux = i - 6
                    commin(aux, 1)
                    aux = i - 17
                    commin(aux, 2)
                    aux = i - 15
                    commin(aux, 2)
