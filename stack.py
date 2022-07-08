class Stack:
    def __init__(self):
        self._data= []
    def push(self,item):
        self._data.append(item)
    def pop(self):
        return self._data.pop()
    def get_size(self):
        return len(self._data)

class TestStack:
    def setup(self):
        self.stack = Stack()

    def match(self,data):
        for c in data:
            if c == "{":
                self.stack.push(c)
                for c in data:
                    if  c == "}":
                        self.stack.pop()
            if c == "[":
                self.stack.push(c)
                for c in data:
                    if  c == "]":
                        self.stack.pop()
            if c == "（":
                self.stack.push(c)
                for c in data:
                    if  c == "）":
                        self.stack.pop()
        return self.stack.get_size() == 0

    def test_match(self):
        #test_data="{}xxxxx[dddddddd(xxxxx{ddddd}dfsfe)dfsefe]xxxx"
        test_data = "}xxxx[ddddd）xxxx{"
        assert self.match(test_data) == True
