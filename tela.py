import tkinter as tk
import perceptron

peso1Numero = None
peso2Numero = None
peso3Numero = None
caixaDeTextoSaida = None
def exibirJanela():
    janela = tk.Tk()
    janela.title("Inteligencia Artifical - Perceptron")
    entradas(janela)
    pesos(janela)
    saida(janela)
    treino(janela)
    janela.mainloop()


def entradas(janela):
    entradasFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    entradasFrame.grid(column=0, row=0, padx=10, pady=10)
    titulo = tk.Label(entradasFrame, text="ENTRADAS", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    entrada1Nome = tk.Label(entradasFrame, text="Placa mãe ou processador intermédiario ou avançado?", font=("Arial", 10))
    entrada1Nome.grid(column=0, row=1, padx=10, pady=10)

    entrada1Input = tk.Entry(entradasFrame, width=20)
    entrada1Input.grid(column=0, row=2, padx=20, pady=5)

    entrada2Nome = tk.Label(entradasFrame, text="Possui SSD NVme M.2?", font=("Arial", 10))
    entrada2Nome.grid(column=0, row=3, padx=10, pady=10)

    entrada2Input = tk.Entry(entradasFrame, width=20)
    entrada2Input.grid(column=0, row=4, padx=20, pady=5)

    entrada3Nome = tk.Label(entradasFrame, text="Possui 8GB ou mais de Mémoria Ram?", font=("Arial", 10))
    entrada3Nome.grid(column=0, row=5, padx=10, pady=10)

    entrada3Input = tk.Entry(entradasFrame, width=20)
    entrada3Input.grid(column=0, row=6, padx=20, pady=5)

    botaoEntrada = tk.Button(entradasFrame, text="Processar",command=lambda: processar(entrada1Input, entrada2Input, entrada3Input))
    botaoEntrada.grid(column=0, row=7, padx=10, pady=10)


def pesos(janela):
    global peso1Numero, peso2Numero, peso3Numero
    pesosframe = tk.Frame(janela, borderwidth=4, relief="ridge")
    pesosframe.grid(column=1, row=0, padx=10, pady=10)
    titulo = tk.Label(pesosframe, text="PESOS", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

    peso1 = tk.Label(pesosframe, text="Placa mãe ou processador intermediário ou avançado", font=("Arial", 10))
    peso1.grid(column=1, row=1, padx=10, pady=10)

    peso1Numero = tk.Label(pesosframe, text=perceptron.pesos[perceptron.PLACAVIDEOPROC], font=("Arial", 10))
    peso1Numero.grid(column=1, row=2, padx=1, pady=1)

    peso2 = tk.Label(pesosframe, text="Possui SSD NVme M.2", font=("Arial", 10))
    peso2.grid(column=1, row=3, padx=10, pady=10)

    peso2Numero = tk.Label(pesosframe, text=perceptron.pesos[perceptron.SSD], font=("Arial", 10))
    peso2Numero.grid(column=1, row=4, padx=1, pady=1)

    peso3 = tk.Label(pesosframe, text="Possui 8GB ou mais de Mémoria Ram", font=("Arial", 10))
    peso3.grid(column=1, row=5, padx=10, pady=10)

    peso3Numero = tk.Label(pesosframe, text=perceptron.pesos[perceptron.MEMORIARAM], font=("Arial", 10))
    peso3Numero.grid(column=1, row=6, padx=1, pady=1)

    botaoResetPesos = tk.Button(pesosframe, text="Resetar", command=lambda: resetPesos())
    botaoResetPesos.grid(column=1, row=7, columnspan=2, padx=10, pady=10)


def resetPesos():
    global peso1Numero, peso2Numero, peso3Numero
    perceptron.iniciarPesos()
    peso1Numero.config(text=perceptron.pesos[perceptron.PLACAVIDEOPROC])
    peso2Numero.config(text=perceptron.pesos[perceptron.SSD])
    peso3Numero.config(text=perceptron.pesos[perceptron.MEMORIARAM])


def saida(janela):
    global caixaDeTextoSaida
    saidaFrame = tk.Frame(janela, borderwidth=4, relief="ridge")
    saidaFrame.grid(column=2, row=0, padx=10, pady=10)
    titulo = tk.Label(saidaFrame, text="SAÍDA", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=2, row=0, padx=10, pady=10, columnspan=2)

    caixaDeTextoSaida = tk.Text(saidaFrame, width=40, height=8)
    caixaDeTextoSaida.grid(row=2, column=2, padx=10, pady=10, rowspan=6)


def treino(janela):
    treinoframe = tk.Frame(janela, borderwidth=4, relief="ridge")
    treinoframe.grid(column=1, row=1, padx=10, pady=10)
    titulo = tk.Label(treinoframe, text="TREINAMENTO", font=("Arial", 12, "bold"), justify="center")
    titulo.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

    botaoResetTreino = tk.Button(treinoframe, text="Treinar",command=lambda: treinar(errosQuantidade, ciclosQuantidade, caixaDeTextoErros))
    botaoResetTreino.grid(column=0, row=1, padx=10, pady=10)

    erros = tk.Label(treinoframe, text="Quantidade de Erros: ", font=("Arial", 10))
    erros.grid(column=1, row=1, padx=10, pady=10)

    errosQuantidade = tk.Label(treinoframe, text=perceptron.pesos[perceptron.PLACAVIDEOPROC], font=("Arial", 10))
    errosQuantidade.grid(column=2, row=1, padx=10, pady=10)
    errosQuantidade.config(text=perceptron.erros)

    ciclos = tk.Label(treinoframe, text="Quantidade de Ciclos: ", font=("Arial", 10))
    ciclos.grid(column=1, row=2, padx=10, pady=10)

    ciclosQuantidade = tk.Label(treinoframe, text=perceptron.pesos[perceptron.PLACAVIDEOPROC], font=("Arial", 10))
    ciclosQuantidade.grid(column=2, row=2, padx=10, pady=10)
    ciclosQuantidade.config(text=perceptron.ciclos)

    errosPorCiclo = tk.Label(treinoframe, text="Erros por ciclo:", font=("Arial", 10))
    errosPorCiclo.grid(column=0, row=3)

    caixaDeTextoErros = tk.Text(treinoframe, width=40, height=8)
    caixaDeTextoErros.grid(row=4, column=0, padx=10, pady=10, rowspan=2, columnspan=2)


def treinar(errosQuantidade, ciclosQuantidade, caixaDeTextoErros):
    perceptron.erros = 0
    perceptron.ciclos = 0
    resultado = perceptron.treinarPerceptron()
    errosQuantidade.config(text=perceptron.erros)
    ciclosQuantidade.config(text=perceptron.ciclos)
    peso1Numero.config(text=perceptron.pesos[perceptron.PLACAVIDEOPROC])
    peso2Numero.config(text=perceptron.pesos[perceptron.SSD])
    peso3Numero.config(text=perceptron.pesos[perceptron.MEMORIARAM])
    caixaDeTextoErros.delete(1.0, tk.END)
    caixaDeTextoErros.insert(tk.END, resultado)


def processar(entrada1Input, entrada2Input, entrada3Input):
    global caixaDeTextoSaida
    perceptron.lerEntradas(float(entrada1Input.get()), float(entrada2Input.get()), float(entrada3Input.get()))
    resultado = perceptron.processarEntradas()
    caixaDeTextoSaida.delete(1.0, tk.END)
    caixaDeTextoSaida.insert(tk.END, 'Resultado: '+ resultado)


