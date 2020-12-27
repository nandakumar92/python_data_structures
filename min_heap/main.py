class min_heap:
    def __init__(self):
        self.heap=[]

    def getmin(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def insert(self,val):
        self.heap.append(val)
        self.heapifyup(len(self.heap)-1)

    def heapifyup(self,index):
        parent=(index-1)//2
        if index<=0:
            return
        elif self.heap[parent]>self.heap[index]:
            self.heap[parent],self.heap[index]=self.heap[index],self.heap[parent]
            self.heapifyup(parent)

    def removemin(self):
        if len(self.heap)==1:
            max=self.heap[0]
            self.heap.pop(0)
            return max
        elif len(self.heap)>1:
            max=self.heap[0]
            self.heap[0],self.heap[-1]=self.heap[-1],self.heap[0]
            self.heap.pop()
            self.heapifydown(0)
            return max
        else:
            return None

    def isleaf(self,index):
        if index>=len(self.heap)//2 and index<=len(self.heap):
            return True
        else:
            return False

    def heapifydown(self,index):
        left=(2*index) +1
        right=(2*index)+2
        smallest=index
        if len(self.heap)>left and self.heap[smallest]>self.heap[left]:
            smallest=left
        if len(self.heap)>right and self.heap[smallest]>self.heap[right]:
            smallest=right
        if smallest!=index:
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            self.heapifydown(smallest)

    def buildheap(self,arr):
        for i in range(len(arr)):
            self.insert(arr[i])

heap=min_heap()
heap.insert(12)
heap.insert(10)
heap.insert(-10)
heap.insert(100)
print(heap.getmin())
heap.insert(-20)
print(heap.getmin())
heap.removemin()
print(heap.getmin())


            
            
        




