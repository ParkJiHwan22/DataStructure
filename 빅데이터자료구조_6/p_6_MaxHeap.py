import random

class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0)

    def size(self) : return len(self.heap) - 1
    def isEmpty(self) : return self.size() == 0
    def Parent(self, i) : return self.heap[i//2]
    def Left(self, i) : return self.heap[i*2]
    def Right(self, i) : return self.heap[i*2+1]
    def display(self, msg = '힙 트리: '):
        print(msg, self.heap[1:])


    def insert(self, n):
        self.heap.append(n)                     # 맨 마지막 노드로 일단 삽입
        i = self.size()                         # 노드 n의 위치
        while(i != 1 and n > self.Parent(i)):   # 부모보다 큰 동안 계속 업힘
            self.heap[i] = self.Parent(i)       # 부모를 끌어내림
            i = i // 2                          # i를 부모의 인덱스로 올림
        self.heap[i] = n                        # 마지막 위치에 n 삽입


    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]                # 삭제할 루트를 복사해 둠
            last = self.heap[self.size()]       # 마지막 노드
            while (child <= self.size()):       # 마지막 노드 이전까지
                # 만약 오른쪽 노드가 더 크면 child를 1증가 (기본은 왼쪽 노드)
                if  child<self.size() and self.Left(parent)<self.Right(parent):
                    child += 1
                if last >= self.heap[child]:
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot
        
    
heap = MaxHeap()                            # MaxHeap 객체 생성
data = [random.randrange(1, 100) for _ in range(50)]    # 힙에 삽입할 데이터, 랜덤 함수로 생성
print("[삽입 연산] : " + str(data))
for elem in data:                           # 모든 데이터를
    heap.insert(elem)                       # 힙에 삽입
heap.display("[ 삽입 후 ]: ")               # 현재 힙 트리를 출력
heap.delete()                               # 한 번의 삭제연산
heap.display("[ 삭제 후 ]: ")               # 현재 힙 트리를 출력
heap.delete()                               # 또 한번의 삭제연산
heap.display("[ 삭제 후 ]: ")               # 현재 힙 트리를 출력