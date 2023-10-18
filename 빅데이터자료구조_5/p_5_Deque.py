MAX_QUEUE_SIZE = 10

class Deque:
    def __init__(self):
        self.queue = [None for _ in range(MAX_QUEUE_SIZE)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % MAX_QUEUE_SIZE == self.front

    def add_front(self, item):
        if self.is_full():
            print("Deque이 꽉 찼습니다.")
            return
        self.front = (self.front - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE
        self.queue[self.front] = item

    def delete_front(self):
        if self.is_empty():
            print("Deque이 비었습니다.")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % MAX_QUEUE_SIZE
        return item

    def get_front(self):
        if self.is_empty():
            print("Deque이 비었습니다.")
            return None
        return self.queue[self.front]

    def add_rear(self, item):
        if self.is_full():
            print("Deque이 꽉 찼습니다.")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % MAX_QUEUE_SIZE

    def delete_rear(self):
        if self.is_empty():
            print("Deque이 비었습니다.")
            return None
        self.rear = (self.rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE
        return self.queue[self.rear]

    def get_rear(self):
        if self.is_empty():
            print("Deque이 비었습니다.")
            return None
        return self.queue[(self.rear - 1 + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE]

    def size(self):
        return (self.rear - self.front + MAX_QUEUE_SIZE) % MAX_QUEUE_SIZE

def menu():
    dq = Deque()

    while True:
        operation = input("앞쪽에서 삽입(I)/앞쪽에서 추출(D)/앞쪽에서 확인(P)/뒤쪽에서 삽입(E)/뒤쪽에서 추출(R)/뒤쪽에서 확인(G)/크기(S)/종료(Q) 중 하나를 선택 ==> ").upper()

        if operation == 'I':
            item = int(input("앞쪽에 입력할 데이터 ==> "))
            dq.add_front(item)
            
        elif operation == 'D':
            dq.delete_front()
            
        elif operation == 'P':
            print(dq.get_front())
            
        elif operation == 'E':
            item = int(input("뒤쪽에 입력할 데이터 ==> "))
            dq.add_rear(item)
            
        elif operation == 'R':
            dq.delete_rear()
            
        elif operation == 'G':
            print(dq.get_rear())
            
        elif operation == 'S':
            print(dq.size())
            
        elif operation == 'Q':
            break
        else:
            print("입력이 잘못됨")

if __name__ == "__main__":
    menu()