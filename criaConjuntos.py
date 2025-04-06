import random

def cria_conjuntos(tamanho, conjunto):
    num_pouco_repetidos = int(tamanho * 0.1)  
    if conjunto == 1:
        base = list(range(1, tamanho + 1))
        valores_repetidos = random.sample(base, num_pouco_repetidos) 
        array_a = base + valores_repetidos
        array_a.sort()
        return array_a
    elif conjunto == 2:
        base = list(range(1, tamanho + 1))
        valores_repetidos = random.sample(base, num_pouco_repetidos)  
        array_b = base + valores_repetidos
        array_b.sort(reverse=True)
        return array_b
    elif conjunto == 3:
        base = list(range(1, tamanho + 1))
        valores_repetidos = random.sample(base, num_pouco_repetidos) 
        array_c = base + valores_repetidos
        random.shuffle(array_c)
        return array_c
    elif conjunto == 4:
        quantidade_unicos = tamanho // 10
        num_unicos = list(range(quantidade_unicos))
        array_d = num_unicos * 9
        array_d.extend(random.sample(range(quantidade_unicos, tamanho), quantidade_unicos)) 
        random.shuffle(array_d)
        return array_d