
class TestSort:

    def setup(self):
        self.data=[3,9,2,5,4]
        self.except_data=[2,3,4,5,9]
        self.except_data_dasc=[9,5,4,3,2]

    def bubble_sort(self, data:list):
        """冒泡算法"""
        size=len(data)
        for i in range(size):
            for j in range(size-i-1):
                if data[j] > data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data
    def bubble_sort_dasc(self,data:list):
        size=len(data)
        for i in range(size):
            for j in range(size-i-1):
                if data[j] < data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
        return data



    def test_bubble(self):
        assert self.except_data == self.bubble_sort(self.data)
        assert self.except_data_dasc == self.bubble_sort_dasc(self.data)

    def selection_sort(self,data:list):
        """选择算法"""
        size=len(data)
        for i in range(size):
            min_id=i
            for j in range(i+1,size):
                if data[min_id] > data[j]:
                    min_id = j
                data[i],data[min_id]=data[min_id],data[i]
        return data

    def test_selection(self):
        assert self.except_data == self.selection_sort(self.data)

