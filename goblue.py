def so_vai():
    import time
    frase = 'Não sabe mais o que fazer para se tornar um verdadeiro Dev?'
    for i in frase:
        print(i, end='')
        time.sleep(0.2)
    print(f'\n')
    time.sleep(2)
    for i in range(1, 10+1):
        g = 'Go BLUE!'
        print(g)
        time.sleep(1)


so_vai()