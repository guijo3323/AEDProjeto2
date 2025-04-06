import time
from criaConjuntos import cria_conjuntos
from fazGraficos import fazGraficos


#https://www.geeksforgeeks.org/red-black-tree-in-python/

class Node:
    def __init__(self, num, cor = 'red'):
        self.num = num
        self.left = None
        self.right = None
        self.cor = cor 
        self.parent= None
        
    def grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent
    
    def sibling(self):
        if self.parent is None:
            return None
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left
        
    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.sibling()
    
    
class RedBlackTree:
    # Constructor
    def __init__(self):
        self.root = None

    # Function to fix the Red Black Tree properties after insertion
    def insert_fix(self, new_node):
        # While there are two continuous red nodes, we need to fix the RB tree
        while new_node.parent and new_node.parent.cor == 'red':
            # Verifica se o novo nó tem um avô 
            grandparent = new_node.grandparent()
            # If the parent is left child of grandparent
            if grandparent and new_node.parent == new_node.grandparent().left:
                uncle = new_node.uncle()
                if uncle and uncle.cor == 'red':
                    new_node.parent.cor = 'black'
                    uncle.cor = 'black'
                    new_node.grandparent().cor = 'red'
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.cor = 'black'
                    new_node.grandparent().cor = 'red'
                    self.rotate_right(new_node.grandparent())
            # If the parent is right child of grandparent
            else:
                uncle = new_node.uncle()
                if uncle and uncle.cor == 'red':
                    new_node.parent.cor = 'black'
                    uncle.cor = 'black'
                    new_node.grandparent().cor = 'red'
                    new_node = new_node.grandparent()
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.cor = 'black'
                    new_node.grandparent().cor = 'red'
                    self.rotate_left(new_node.grandparent())
        self.root.cor = 'black'

    # function to insert a node similar to BST insertion
    def insert(self, value):
        # Regular BST insert
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                # If the node is in the left subtree
                if value < curr_node.num:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.left
                # If the node is in the right subtree
                elif value > curr_node.num:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.right
                else:
                    return
        self.insert_fix(new_node)
        
        
        
    def rotate_left(self, node):
        global rotation
        rotation+=1
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child
        
        
    def rotate_right(self, node):
        global rotation
        rotation+=1
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child
        
            


def VPTree(arr):
	global rotation
	rotation =0
	t = RedBlackTree()
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
            VPTree(arr)
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
    
    fazGraficos(tamanhos,tempos,'Árvore VP')

if __name__ == '__main__':
    main()