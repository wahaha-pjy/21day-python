import pytest

def fun(x):
    return x+1

class TestFun:

    @pytest.mark.success
    @pytest.mark.parametrize("input,expect",[
        (1,2),
        (3,4)
    ])
    def test_anw(self,input,expect):
        print("anw")
        assert fun(input) == expect

    @pytest.mark.fail
    @pytest.mark.parametrize("input,expect", [
        (1, 3),
        (3, 3)
    ])
    def test_anw2(self,input,expect):
        print("test anw2")
        assert fun(input) == expect


