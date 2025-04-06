import time
from criaConjuntos import cria_conjuntos
import random
from fazGraficos import fazGraficos

#https://gist.github.com/irachex/3922705


class Node:
    def __init__(self, key, data):
        self.key = key
        self.ran = random.random()
        self.size = 1
        self.cnt = 1
        self.data = data
        self.left = None
        self.right = None

    def left_rotate(self):
        global rotation
        rotation+=1
        a = self
        b = a.right
        a.right = b.left
        b.left = a
        a = b
        b = a.left
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def right_rotate(self):
        global rotation
        rotation+=1
        a = self
        b = a.left
        a.left = b.right
        b.right = a
        a = b
        b = a.right
        b.size = b.left_size() + b.right_size() + b.cnt
        a.size = a.left_size() + a.right_size() + a.cnt
        return a

    def left_size(self):
        return 0 if self.left is None else self.left.size

    def right_size(self):
        return 0 if self.right is None else self.right.size
    


class Treap(object):
    def __init__(self):
        self.root = None

    def _insert(self, node, key, data=None):
        if node is None:
            node = Node(key, data)
            return node
        node.size += 1
        if key < node.key:
            node.left = self._insert(node.left, key, data)
            if node.left and node.left.ran < node.ran:
                node = node.right_rotate()
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, data)
            else:
                node.right = self._insert(node.right, key, data)
            if node.right and node.right.ran < node.ran:
                node = node.left_rotate()
        else:
            return
        #else:
        #    node.cnt += 1
        return node

    def insert(self, key, data=None):
        self.root = self._insert(self.root, key, data)
    



def ArvoreTREAP(arr):
	global rotation
	rotation =0
	t = Treap()
	for i in arr:
		t.insert(i)


def main():
    tamanhos=[200000,400000,600000,800000,1000000]
    tempos_a=[]
    tempos_b=[]
    tempos_c=[]
    tempos_d=[]
    for j in tamanhos:
        print('Tamanho do array:' ,j)
        for i in range(4):
            start = time.time()
            arr = cria_conjuntos(j, i+1)
            ArvoreTREAP(arr)
            tempo=time.time() - start
            print('Conjunto ',i+1,': ', (tempo)*1000, 'rotações:',(rotation))
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            elif i==2:
                tempos_c.append(tempo)
            else:
                tempos_d.append(tempo)
                
    tempos=[tempos_a,tempos_b,tempos_c,tempos_d]
    
    fazGraficos(tamanhos,tempos,'Árvore TREAP')

if __name__ == '__main__':
    main()