from criaConjuntos import cria_conjuntos
import time
from fazGraficos import fazGraficos

#https://www.geeksforgeeks.org/insertion-in-an-avl-tree/

rotation=0

class Node:
    def __init__(self,elem):
        self.left=None
        self.right=None
        self.elem=elem
        self.altura=1

class AVL:
    def __init__(self):
        self.node = None

    def insert(self, node, elem):
        if node is None:
            return Node(elem)
        if elem < node.elem:
            node.left = self.insert(node.left, elem)
        elif elem > node.elem:
            node.right = self.insert(node.right, elem)

        node.altura = 1+ max(self.get_altura(node.left), self.get_altura(node.right))

        fe = self.fator_equilibrio(node)

        if fe > 1:
            if elem < node.left.elem:
                return self.right_rotate(node)
            if elem > node.left.elem:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        elif fe < -1:
            if elem > node.right.elem:
                return self.left_rotate(node)
            if elem < node.right.elem:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node

    def right_rotate(self, node):
        global rotation
        rotation += 1

        A = node.left
        Y = A.right

        A.right = node
        node.left = Y

        node.altura = 1 + max(self.get_altura(node.left), self.get_altura(node.right))
        A.altura = 1 + max(self.get_altura(A.left), self.get_altura(A.right))

        return A

    def left_rotate(self, node):
        global rotation
        rotation += 1

        B = node.right
        Y = B.left

        B.left = node
        node.right = Y

        node.altura = 1 + max(self.get_altura(node.left), self.get_altura(node.right))
        B.altura = 1 + max(self.get_altura(B.left), self.get_altura(B.right))

        return B

    def get_altura(self, node):
        if node is None:
            return 0
        return node.altura

    def fator_equilibrio(self, node):
        if node is None:
            return 0
        return self.get_altura(node.left) - self.get_altura(node.right)
    
    def search(self, key):
        x = self.node	
        while x is not None and key != x.elem:
            if key < x.elem:
                x = x.left
            else:
                x = x.right
        return x
    

def AVLTree(arr):
    global rotation
    rotation =0
    avl = AVL()
    for i in arr:
        if avl.search(i)==None:
        	avl.node = avl.insert(avl.node, i)

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
            arr = cria_conjuntos(j,i+1)
            AVLTree(arr)
            tempo = time.time() - start
            print('Conjunto ',i+1,': ', tempo*1000, 'rotações:',(rotation))
            
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            elif i==2:
                tempos_c.append(tempo)
            else:
                tempos_d.append(tempo)
            
        
    tempos=[tempos_a,tempos_b,tempos_c,tempos_d]
    
    fazGraficos(tamanhos,tempos,'Árvore AVL')       

if __name__ == '__main__':
    main()