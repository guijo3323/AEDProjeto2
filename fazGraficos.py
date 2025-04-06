import numpy as np
import matplotlib.pyplot as plt

#https://stackoverflow.com/questions/29885408/how-plot-polyfit-n-log-n-with-python


def fazGraficos(tamanhos, tempos,titulo):
    conjuntos = ['Conjunto A', 'Conjunto B', 'Conjunto C', 'Conjunto D']
    cores = ['blue', 'orange', 'green', 'red']

    plt.figure(figsize=(10, 6))

    for i in range(4):
        x = np.array(tamanhos)
        y = np.array(tempos[i])
        if titulo=='Árvore Binária':
            regressao = np.polyfit(x, y, 1)
        else:
            x_log = np.log(x)
            regressao = np.polyfit(x_log, y, 1)
           
        poly1d_fn = np.poly1d(regressao)
        
        plt.plot(x, y, 'o', color=cores[i], label=f'{conjuntos[i]} (real)')
        if titulo=='Árvore Binária':
            plt.plot(x, poly1d_fn(x), '-', color=cores[i], label=f'{conjuntos[i]} (regressÃ£o)')
        else:
            plt.plot(x, poly1d_fn(x_log), '-', color=cores[i], label=f'{conjuntos[i]} (regressÃ£o)')


    plt.title(titulo)
    plt.xlabel('Tamanho do array')
    plt.ylabel('Tempo (ms)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



tamanhos=[200000,400000,600000,800000,1000000]
a = [2100.2681255340576, 4550.326347351074, 7085.793495178223, 10220.324516296387, 12482.826709747314]
b = [2089.9572372436523, 4539.559364318848, 7267.8163051605225, 9643.519639968872, 12242.817401885986]
c = [2593.2579040527344, 6163.938999176025, 10371.896028518677, 13863.500833511353, 18255.626440048218]
d = [587.6302719116211, 1380.3467750549316, 2210.3352546691895, 3136.399745941162, 4159.404516220093]






tempos=[a,b,c,d]

fazGraficos(tamanhos, tempos,'Árvore AVL')