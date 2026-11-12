import multiprocessing
import random
import time

chegada:int = 0
saida: int = 0
semaforo = None

def init(c,s,sema):
    global chegada
    global saida
    global semaforo
    chegada = c
    saida = s
    semaforo = sema

def pessoa(id):
    global semaforo
    pessoa_caminhando(id)
    with semaforo:
        cruzar_porta(id)
    pessoa_saiu(id)


def pessoa_caminhando(id):
    global chegada
    dp : int = 0
    df : int = 0
    des : int = 0
    tempo : float = 0.0

    df = 200
    tempo =  1.0

    while (dp < df):
        dp = dp + des
        des = random.randint(4,6)

        if( dp > df):
            dp = df

        time.sleep(tempo)
        print(f'Pessoa #{id} andou {dp} metros')

    chegada.value = chegada.value + 1
    print(f'Pessoa #{id} foi a {chegada.value}º a chegar na porta')

def cruzar_porta(id):
    global saida
    print(f'Pessoa #{id} está abrindo a porta')

    tempo_rand : int = 0.0
    tempo_porta : int = 0.0

    tempo_rand = random.randint(1000,2000)
    tempo_porta = tempo_rand / 1000.0
    time.sleep(tempo_porta)
    saida.value = saida.value + 1
    print(f'Pessoa #{id} cruzou a porta e foi a {saida.value}º a passar')

def pessoa_saiu(id):
    print(f'Pessoa #{id} seguiu seu caminho após cruzar a porta')

def main():
    posc: int = 0
    poss: int = 0
    paramentros : int = [0]*4
    i:int = 0
    sem = None

    posc = multiprocessing.Value('i',0)
    poss = multiprocessing.Value('i',0)

    for i in range(0,4,1):
        paramentros[i] = i+1

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(posc,poss,sem)) as pool:
            pool.map(pessoa,paramentros)


if __name__ == '__main__':
    main()