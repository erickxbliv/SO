import threading
import time
import random

numero_de_caixas = 3
clientes = 30
semaforo = threading.Semaphore(numero_de_caixas)
lock = threading.Lock()

teste = [False,False,False]
nomes = ["Joana","Jose","Felipe"]
execucoes = [0,0,0]
atendimento = [30]

def recurso():

    semaforo.acquire()

    lock.acquire()

    guardar = 0;

    for i in range(3):
      if teste[i] == False:
        teste[i] = True
        guardar = i
        break

    print(nomes[guardar] + " atendeu: ", threading.current_thread().name)
    execucoes[i] = threading.current_thread().ident

    lock.release()

    #print(threading.current_thread().name)
    time.sleep(random.randint(3,10))

    for i in range(3):
      if execucoes[i] == threading.current_thread().ident:
        teste[i] = False
        break
 
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
