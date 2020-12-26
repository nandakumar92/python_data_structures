class maxheap:
    def __init__(self):
        self.heap=[]

    def insert(self,val):
        self.heap.append(val)  
        self.heapify_up(len(self.heap)-1)

    def getmax(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def removemax(self):
        if len(self.heap)>1:
            max=self.heap[0]
            self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
            self.heap.pop()
            self.heapify_down(0)
            return max
        elif len(self.heap)==1:
            max=self.heap[0]
            self.heap.pop(0)
            return max
        else:
            return None

    def heapify_up(self,index):
        parent=(index-1)//2
        if index<=0:
            return
        elif self.heap[parent]<self.heap[index]:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self.heapify_up(parent)

    def isleaf(self,index):
        if index>=len(self.heap)//2 and index<=len(self.heap):
            return True
        else:
            return False

    def heapify_down(self,index):
        left=(index*2)+1
        right=(index*2)+2
        largest=index
        while not self.isleaf(largest):
            if len(self.heap) > right and self.heap[largest]<self.heap[right]:
                largest=right
            if len(self.heap) > left and self.heap[largest]<self.heap[left]:
                largest=left
            if largest!=index:
                self.heap[largest],self.heap[index]=self.heap[index],self.heap[largest]
            self.heapify_down(largest)

    def buildheap(self,arr):
        self.heap=arr
        for i in range(len(arr)-1,-1,-1):
            self.heapify_up(i)

heap=maxheap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
print(heap.getmax())
heap.removemax()
print(heap.getmax())
