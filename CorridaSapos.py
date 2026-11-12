import multiprocessing
import time
import random

posição = None
semaforo = None

def init(pos, sema):
    global posição
    global semaforo
    posição = pos
    semaforo = sema

def sapo(id,dm):
    global posição
    global semaforo
    dp=0
    tmp = 5
    print(f"Sapo {id} largou!")
    while dp < dm:
        pulo = random.randint(1,tmp)
        dp += pulo
        print(f"Sapo {id} deu um salto de {pulo} cm ")
        print(f"Distancia percorrida: {dp} cm | Distancia maxima: {dm} cm")
        time.sleep(0.2)
    print(f"O sapo {id} cruzou a linha de chegada!")
    with semaforo:
        posição.value += 1
        print(f"Sapo {id} foi o {posição.value}º a cruzar a linha de chegada!")

def main():
    dm=20
    sapo1,sapo2,sapo3,sapo4,sapo5= 1,2,3,4,5
    posição = multiprocessing.Value('i',0)
    print("Iniciando corrida de sapos!")
    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=5, initializer=init, initargs=(posição, sem)) as pool:
            pool.starmap(sapo,[(sapo1,dm),(sapo2,dm),(sapo3,dm),(sapo4,dm),(sapo5,dm)])

    print("Corrida finalizada!")

if __name__ == "__main__":
    main()
    
