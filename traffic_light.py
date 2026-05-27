import time

while True:
    contador = 25
    
    for tempo in range(contador):

        if tempo == 0:
            print('\033[0;31mRed')
            time.sleep(1)

        elif tempo == 11:
            print('\033[0;33mYellow')
            time.sleep(1)

        elif tempo == 14:
            print('\033[0;32mGreen')
            time.sleep(1)
            
        print(tempo)
        tempo += 1
        time.sleep(1)