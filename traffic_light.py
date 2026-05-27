import time

while True:
    contador = 25
    for tempo in range(contador):

        if tempo == 0:
            time.sleep(1)
            print('\033[0;31mVermelho')

        elif tempo == 11:
            time.sleep(1)
            print('\033[0;33mAmarelo')

        elif tempo == 14:
            time.sleep(1)
            print('\033[0;32mVerde')
            
        print(tempo)
        tempo += 1
        time.sleep(1)
