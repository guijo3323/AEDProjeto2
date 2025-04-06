import time 
from criaConjuntos import cria_conjuntos
from fazGraficos import fazGraficos



#https://www.geeksforgeeks.org/print-level-order-traversal-line-line/


class Node:
    def __init__(self,num):
        self.num= num
        self.left=None
        self.right=None
        
    
       
    def insert(self, elem):
        queue = [self]
        while queue:
            current = queue.pop(0)
            if current.num==elem:
                return
            if not current.left:
                current.left = Node(elem)
                return
            else:
                queue.append(current.left)
            if not current.right:
                current.right = Node(elem)
                return
            else:
                queue.append(current.right)
                
   
def tree1(arr):
    root = Node(arr[0])
    for i in arr[1:]:
        root.insert(i)

            
            
def main():
    tamanhos=[20000,40000,60000,80000,100000]
    tempos_a=[]
    tempos_b=[]
    tempos_c=[]
    tempos_d=[]
    
    for j in tamanhos:
        print('Tamanho do array:' ,j)
        for i in range(4):
            start = time.time()
            arr = cria_conjuntos(j, i+1)
            tree1(arr)
            tempo =time.time() - start
            print('Conjunto ',i+1,': ', tempo*1000, 's')
            if i==0:
                tempos_a.append(tempo)
            elif i==1:
                tempos_b.append(tempo)
            elif i==2:
                tempos_c.append(tempo)
            else:
                tempos_d.append(tempo)
         
    tempos=[tempos_a,tempos_b,tempos_c,tempos_d]
    
    fazGraficos(tamanhos,tempos,'Árvore Binária')              

if __name__ == '__main__':
    main()