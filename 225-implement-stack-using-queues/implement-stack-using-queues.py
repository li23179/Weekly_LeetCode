class MyStack:

    def __init__(self):
        # we are only using the popleft and append
        # queue should keep track of the elments
        # queue: [1, 2, 3] push(4) => [1, 2, 3, 4]
        # stack: [1, 2, 3] push(4) => [4, 1, 2, 3]
        self.queue = deque([])

    def push(self, x: int) -> None:
        # normal on stack, we do stack.push() [1, 2, 3, 4] <- [5, 1, 2, 3, 4]
        # push(5): [1, 2, 3, 4] => [1, 2, 3, 4, 5] 
        # loop the entire queue until we met the last elem
        # our result should be [5, 1, 2, 3, 4]
        # [1, 2, 3, 4, 5] => [2, 3, 4, 5] => append(1) [2, 3, 4, 5, 1]
        self.queue.append(x)
        for i in range(len(self.queue)-1):
            elem = self.queue.popleft()
            self.queue.append(elem)

    def pop(self) -> int:
        # stack: [1, 2, 3, 4, 5] => [1, 2, 3, 4] return 5
        # [1, 2, 3, 4, 5] => [2, 3, 4, 5, 1] => []
        return self.queue.popleft()

    def top(self) -> int:
        # stack: [1, 2, 3, 4, 5] => top() => 5
        # queue: [1, 2, 3, 4, 5]
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()