#开发人  ：
#开发时间：2022/12/28 16:48
import queue


class Node():
    def __init__(self,data,leftChild = None, rightChild = None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild

class Tree():
    def __init__(self):
        self.root = None
        self.ls = []
        self.total=0

    def add(self,data):
        node = Node(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
            self.total = self.total + 1
            test=self.ls[0]
        else:
            lastNode = self.ls[int((self.total+1) / 2 )-1]
            if lastNode.leftChild == None:
                lastNode.leftChild = node
                self.ls.append(lastNode.leftChild)
                self.total =self.total + 1
            elif lastNode.rightChild == None:
                lastNode.rightChild = node
                self.ls.append(lastNode.rightChild)
                self.total = self.total + 1

    def showTree(self):
        node=self.root
        qu=queue.Queue()
        while(node!=None):
            if(node.leftChild!=None):
                print("print:",node.data,"  left child：",node.leftChild.data)
            if (node.rightChild != None):
                print("print:", node.data, "  right child：", node.rightChild.data)
            qu.put(node.leftChild)
            qu.put(node.rightChild)
            node=qu.get()

    def findFather(self,index):
        node=self.ls[int((index+1)/2)-1]
        if(index==0):
            print("This node is a root node and has no parent node！")
        else:
            print("The data value of the parent node is：",node.data)

    def findLeftChild(self,index):
        node=self.ls[index]
        node=node.leftChild
        if(node==None):
            print("This node has no left child！")
        else:
            print("Left child data value is：",node.data)

    def findRightChild(self,index):
        node=self.ls[index]
        node=node.rightChild
        if (node == None):
            print("This node has no right child！")
        else:
            print("The right child data value is：",node.data)


def insert(tree,data):
    tree.add(data)
    adjust(tree)

def adjust(tree):
    i=tree.total
    f=int(tree.total/2)
    while(f>0 and tree.ls[i-1].data<tree.ls[f-1].data ):
        temp=tree.ls[i-1].data
        tree.ls[i - 1].data = tree.ls[f - 1].data
        tree.ls[f - 1].data = temp
        i=f
        f=int(f/2)

def delMin(tree):
    delete=tree.root
    last=tree.ls[tree.total-1]
    delete.data=last.data
    if(tree.total%2==0):
        tree.ls[int(tree.total/2)-1].leftChild=None
    else:
        tree.ls[int(tree.total / 2) - 1].rightChild = None
    tree.ls.pop()
    tree.total = tree.total-1
    delAdjust(tree)

def delAdjust(tree):
    i=1
    while(True):
        min=i
        if(2*i<=tree.total and tree.ls[min-1].data>tree.ls[2*i-1].data):
            min=2*i
        if (2*i+1<=tree.total != None and tree.ls[min-1].data > tree.ls[2 * i].data):
            min = 2 * i+1
        if(i==min):
            break
        temp=tree.ls[i-1].data
        tree.ls[i-1].data=tree.ls[min-1].data
        tree.ls[min-1].data=temp
        i=min

if __name__ == '__main__':
    tree = Tree()
    for i in range(1,11):
        tree.add(i)

    print("The tree structure of the first question is：")
    tree.showTree()
    print("Please enter an index（The current index range is：0-", tree.total-1 , "）：")
    index=input()
    index=int(index)
    if(tree.root==None):
        print("The tree is an empty tree！")
    elif(index<0 or index>tree.total-1):
        print("Invalid index value entered")
    else:
        tree.findFather(index)
        tree.findLeftChild(index)
        tree.findRightChild(index)

    print()
    print("Start building the minimum priority queue!")
    num=input("Please enter how many vertices the constructed tree has：")
    num=int(num)
    minTree=Tree()
    for i in range(0,num):
        print("Please enter No.",i+1,"Data value of vertices：")
        da=int(input())
        insert(minTree,da)
    print("The tree structure of the second question is：")
    minTree.showTree()
    print("The structure of the tree after deleting one minimum node is as follows：")
    delMin(minTree)
    minTree.showTree()
    print("The structure of the tree after deleting two minimum node is as follows：")
    delMin(minTree)
    minTree.showTree()