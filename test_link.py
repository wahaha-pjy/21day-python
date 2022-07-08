class LinkNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None

    def append(self,data=None):
        """链表尾部追加"""
        item=self
        while item.next is not None:
            item=item.next

        item.next=LinkNode(data)
        return self

    def travel(self):
        """遍历链表"""
        item=self
        while item is not None:
            yield item
            item=item.next

    def search(self,data):
        """查找数据的位置"""
        item=self
        index=0
        while item is not None:
            if item.data == data:
                return index
            else:
                index +=1
                item = item.next
        return -1

    def insert(self,pos,data):
        item=self
        index=0
        while item is not None:
            if index == (pos-1):
                break
            index +=1
            item=item.next

        node=LinkNode(data)
        node.next=item.next
        item.next=node

    def order(self,data):
        pre=self
        for item in self.travel():
            if data < item.data:
                break
            pre=item

        node_new=LinkNode(data)
        node_new.next=pre.next
        pre.next=node_new
        return self


class TestLinkNode:
    def setup(self):
        self.link=LinkNode(0)
        self.link.append("a")
        self.link.append(2).append(3).append(4)
        self.link.travel()

    def test_search(self):
        print(self.link.search("a"))

    def test_insert(self):
        self.link.insert(3,"aa")
        self.link.travel()

    def test_order(self):
        self.link =LinkNode(1)
        self.link.order(4).order(2).order(5).order(3)
        self.link=[item.data for item in self.link.travel()]
        assert self.link==[1,2,3,4,5]