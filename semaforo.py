import threading
import time
import random


numero_de_caixas = 3
semaforo = threading.Semaphore(numero_de_caixas)


def recurso():

    semaforo.acquire()

    #print(threading.current_thread().name)
    time.sleep(random.randint(3,10))
 
    semaforo.release()
    

if __name__=="__main__":

    linhas = []

    for i in range(30):
      thread = threading.Thread(target=recurso)
      linhas.append(thread)


    for thread in linhas:
      thread.start()

    for thread in linhas:
      thread.join()
