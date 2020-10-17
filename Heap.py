from typing import List, Tuple, TypeVar
Value = TypeVar("Value")
Key = TypeVar("Key")
class heap:
    
    def __init__(self, l: List[Tuple[Value, Key]] = []):
        
        self._h = l[:]
        self._d = dict()
        for i in range(len(self._h)):
            self._d[self._h[i][1]] = i
            
        self.heapify()
        
    def heapify(self):
        for i in range(self.parent(len(self._h)), -1, -1):
            self.siftdown(i)
            
    def siftdown(self, i: int):
        curr = i
        
        # keep sifting as long as the current node 
        # is greater tha one of the children
        while (self.left(curr) < len(self._h) and \
               self._h[curr][0] > self.leftval(curr)[0]) or \
              (self.right(curr) < len(self._h) and \
               self._h[curr][0] > self.rightval(curr)[0]):

            child = self.left(curr)
            
            # if we have a right is it smaller than the left?
            if child < len(self._h) - 1 and \
                self.rightval(curr) < self.leftval(curr):
                child = child + 1
                
            # child refers to the smaller of the children
            
            # swap the current node with the smaller child
            (self._h[child], self._h[curr]) = (self._h[curr], self._h[child])
            
            # patch up the dictionary values
            self._d[self._h[child][1]] = child
            self._d[self._h[curr][1]]  = curr
            curr = child
            
    def siftup(self, i: int) -> None:
        curr = i 
        
        while curr > 0 and self._h[curr] < self.parentval(curr):
            (self._h[curr], self._h[self.parent(curr)]) =  \
                (self._h[self.parent(curr)], self._h[curr]) 
            
            self._d[self._h[curr][1]] = curr
            self._d[self._h[self.parent(curr)][1]] = self.parent(curr)
            
            curr = self.parent(curr)
            
    def insert(self, k: Key, v: Value) -> None:
        self._h.append((v,k))
        self._d[k] = len(self._h) - 1
        self.siftup(len(self._h) - 1)
        
    def delete_root(self) -> Tuple[Value,Key]:
        """
        Delete the root (and return it) node by moving the last item to the root
        and then pushing it down the heap to its proper place
        """
        t = self.min()
        if len(self._h) == 1:
            v,k = self._h.pop()
            self._d.pop(k)
            return t

        self._d.pop(self._h[0][1])
        self._h[0] = self._h.pop()
        self._d[self._h[0][1]] = 0
        self.siftdown(0)
        return t
    
    def decrease_key(self, v: Key, d: Value):
        self._h[self._d[v]] = (d, v)  # replace value in heap
        self.siftup(self._d[v])       # sift it up, look up index in dictionary

    def min(self):
        return self._h[0]

    def parent(self, i:int) -> int:
        return (i - 1)//2
    
    def left(self, i: int) -> int:
        return 2 * i + 1
    
    def right(self, i: int) -> int:
        return 2 * i + 2
    
    def leftval(self, i: int) -> Tuple[Value,Key]:
        return self._h[self.left(i)]
    
    def rightval(self, i: int) -> Tuple[Value,Key]:
        return self._h[self.right(i)]
    
    def parentval(self, i: int) -> Tuple[Value,Key]:
        return self._h[self.parent(i)]
        