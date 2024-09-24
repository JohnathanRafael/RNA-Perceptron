import random

erros = 0
ciclos = 0
pesos = {}
entradas = {}
saidasEsperadas = {}

PLACAVIDEOPROC = 'placaVideoProc'
SSD = 'SSD'
MEMORIARAM = 'memoriaRam'
RESULTADO = 'resultado'

def iniciarPesos():
    global pesos
    pesos[PLACAVIDEOPROC] = random.choice([0, 1])
    pesos[SSD] = random.choice([0, 1])
    pesos[MEMORIARAM] = random.choice([0, 1])


def iniciarTabelaTeste():
    global saidasEsperadas
    saidasEsperadas = {
        PLACAVIDEOPROC: (1, 1, 0, 0),
        SSD:            (0, 1, 1, 0),
        MEMORIARAM:     (1, 1, 0, 1),
        RESULTADO:      (1, 1, 0, 0)

    }

def lerEntradas(entradas):
    entradas[PLACAVIDEOPROC] = input("A placa de vídeo e o processador são intermediários/avançados?")
    entradas[SSD] = input("Possui SSD NVme M.2 ?")
    entradas[MEMORIARAM] = input("Possui 8Gb ou mais de mémoria RAM ?")


def treinarPerceptron():
    global erros, ciclos
    errosPorCiclo = ""
    erro = 1
    while (erro > 0):
        ciclos += 1
        erro = 0;
        for i in range(len(saidasEsperadas[RESULTADO])):
            soma = saidasEsperadas[PLACAVIDEOPROC][i] * pesos[PLACAVIDEOPROC] + saidasEsperadas[SSD][i] * pesos[SSD] + saidasEsperadas[MEMORIARAM][i] * pesos[MEMORIARAM]
            if (soma > 0):
                soma = 1
            else:
                soma = 0

            if (saidasEsperadas[RESULTADO][i] != soma and soma == 0):
                erro += 1
                erros += 1
                pesos[PLACAVIDEOPROC] += saidasEsperadas[PLACAVIDEOPROC][i]
                pesos[SSD] += saidasEsperadas[SSD][i]
                pesos[MEMORIARAM] += saidasEsperadas[MEMORIARAM][i]
            if (saidasEsperadas[RESULTADO][i] != soma and soma == 1):
                erro += 1
                erros += 1
                pesos[PLACAVIDEOPROC] -= saidasEsperadas[PLACAVIDEOPROC][i]
                pesos[SSD] -= saidasEsperadas[SSD][i]
                pesos[MEMORIARAM] -= saidasEsperadas[MEMORIARAM][i]
        errosPorCiclo += f"Ciclo {str(ciclos)}: {str(erro)}\n"
    return errosPorCiclo




def lerEntradas(entrada1, entrada2, entrada3):
    entradas[PLACAVIDEOPROC] = entrada1
    entradas[SSD] = entrada2
    entradas[MEMORIARAM] = entrada3


def processarEntradas():
    soma = entradas[PLACAVIDEOPROC] * pesos[PLACAVIDEOPROC] + entradas[SSD] * pesos[SSD] + entradas[MEMORIARAM] * pesos[MEMORIARAM]
    if(soma > 0):
        return "Computador gamer"
    else:
        return "Computador de escritório"

iniciarTabelaTeste()
iniciarPesos()
# treinarPerceptron()
# lerEntradas(entradas)
#
# print("SAIDA: ", )
