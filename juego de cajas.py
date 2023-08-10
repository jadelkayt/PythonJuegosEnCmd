import random as rm
from tqdm import tqdm
import os
import time as tm



def Animacion():
    total_iterations = 100

    for _ in tqdm(range(total_iterations), desc="Progreso", ncols=100):
    # Simula algún trabajo
        
        os.system('cls')
        

def Madera():
    #Animacion()
    
    premios = {
        1: "10 de oro",
        2: "30 de oro",
        3: "arma normal",
        4: "arma mitica"
    }
    probabilidades_premios = {
        1: 0.24,
        2: 0.34,
        3: 0.44,
        4: 0.1
    }

    lut = rm.choices(list(probabilidades_premios.keys()), list(probabilidades_premios.values()))[0]

    print(f"Su premio es: {premios[lut]}")

    input("Presione Enter Para Continuar\n")


def Bronce():
    premios = {
        1: "100 de oro",
        2: "30 de oro",
        3: "arma normal",
        4: "arma mitica"
    }
    probabilidades_premios = {
        1: 0.29,
        2: 0.39,
        3: 1.4,
        4: 0.2
    }

    lut = rm.choices(list(probabilidades_premios.keys()), list(probabilidades_premios.values()))[0]

    print(f"Su premio es: {premios[lut]}")

    input("Presione Enter Para Continuar\n")

def Plata():
    premios = {
        1: "200 de oro",
        2: "100 de oro",
        3: "arma normal",
        4: "arma mitica"
    }
    probabilidades_premios = {
        1: 0.70,
        2: 0.80,
        3: 0.20,
        4: 0.3
    }

    lut = rm.choices(list(probabilidades_premios.keys()), list(probabilidades_premios.values()))[0]

    print(f"Su premio es: {premios[lut]}")

    input("Presione Enter Para Continuar\n")

def Oro():
    premios = {
        1: "300 de oro",
        2: "200 de oro",
        3: "arma normal",
        4: "arma oro"
    }
    probabilidades_premios = {
        1: 0.70,
        2: 0.80,
        3: 0.20,
        4: 0.4
    }

    lut = rm.choices(list(probabilidades_premios.keys()), list(probabilidades_premios.values()))[0]

    print(f"Su premio es: {premios[lut]}")

    input("Presione Enter Para Continuar\n")

def Diamante():
    premios = {
        1: "1000 de oro",
        2: "800 de oro",
        3: "arma plata",
        4: "arma Diamante"
    }
    probabilidades_premios = {
        1: 0.50,
        2: 0.20,
        3: 0.30,
        4: 0.9
    }

    lut = rm.choices(list(probabilidades_premios.keys()), list(probabilidades_premios.values()))[0]

    print(f"Su premio es: {premios[lut]}")

    input("Presione Enter Para Continuar\n")

def inicio():


    print("""   CAJAS DISPONIBLES
                1) Madera
                2) Bronce
                3) Plata
                4) Oro
                5) Diamante
        """)
    opc = int(input("Opcion De Caja: "))
    os.system('cls')
    tm.sleep(1)
    if opc == 1:
        Madera()
    if opc == 2:
        Bronce()
    if opc == 3:
        Plata()
    if opc == 4:
        Oro()
    if opc == 5:
        Diamante()


#llamdado inmediato
while True:
    inicio()
    os.system('cls')
