import multiprocessing
import time
import random

semaforo= None

def init(sema):
    global semaforo
    semaforo = sema

def carro(id):
    global semaforo

    carro_andando(id)
    with semaforo:
        cruzamento(id)
    carro_saindo(id)

def carro_andando(id):
    tempo: float = 0.0
    tempo_rand: float = 0.0
    tempo_rand= random.randint(100,500)
    tempo=tempo_rand/1000
    time.sleep(tempo)
    print(f'Carro #{id} chegou no cruzamento')

def cruzamento(id):
    sent: str = ''
    tempo_rand: float = 0.0
    tempo_passagem: float = 0.0

    if(id == 1):
        sent = 'Norte ---> Sul(Baixo)'
    elif(id == 2):
        sent = 'Oeste ---> Leste(Direita)'
    elif(id == 3):
        sent = 'Leste ---> Oeste(Esquerda)'
    elif(id == 4):
        sent = 'Sul ---> Norte(Cima)'

    print(f'Carro #{id} está atravessando o cruzamento no sentido {sent}')
    tempo_rand= random.randint(100,500)
    tempo_passagem=tempo_rand/1000
    time.sleep(tempo_passagem)

def carro_saindo(id):
    print(f'Carro #{id} saiu do cruzamento')

def main():
    paramentros : int = [0]*4
    i:int = 0
    sem = None

    for i in range(0,4,1):
        paramentros[i] = i+1
    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem,)) as pool:
            pool.map(carro, paramentros)


if __name__ == '__main__':
    main()
