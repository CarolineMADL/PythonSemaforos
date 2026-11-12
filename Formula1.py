import multiprocessing
import time
import random

semap = None
semeq =  None

def init(semp,seme):
    global semap
    global semeq
    semap = semp
    semeq = seme

def car(id,ide):
    global semap
    global semeq

    box(id,ide)
    
    with semeq[ide-1]:
        with semap:
            pista(id,ide)

    carf(id,ide)

def box(id,ide):
    tr : int = 0
    t:float = 0.0

    tr = random.randint(100,600)
    t = tr/1000.0
    time.sleep(t)
    print('Carro #',id, '(Equipe',ide,') aguardando a libereção para a pista')

def pista(id,ide):
    vol : int = 0
    tr : int = 0
    t: float = 0.0

    print(f'>>> Carro #{id} (Equipe {ide}) ENTROU na pista <<<')

    for vol in range(1, 4, 1):
        tr = random.randint(500, 1500)
        t = tr / 1000
        time.sleep(t)
        print(f'<<< Carro #{id} (Equipe {ide}) - Volta {vol}/3 | Tempo {t:.3f}s')

    print(f'<<< Carro #{id} (Equipe {ide}) saiu da pista >>>')


def carf(id,ide):
    print(f'Carro #{id} (Equipe {ide}) encerrou o treino e retornou à garagem')


def main():
    parametros = [0] * 14
    semp = None
    seme = None
    i : int = 0
    id: int = 0
    ide : int = 0

    for i in range (0,14,1):
        id = i + 1
        ide = (i // 2) + 1
        parametros[i] = id, ide

    with multiprocessing.Manager() as gerenciador:
        semp = gerenciador.Semaphore(5)
        seme = [gerenciador.Semaphore(1) for _ in range(7)]

        with multiprocessing.Pool(processes=14, initializer=init, initargs=(semp, seme)) as pool:
            pool.starmap(car, parametros)

if __name__ == '__main__':
    main()