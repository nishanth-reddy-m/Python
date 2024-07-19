from user_input import user_input as ui

class NotSorted(Exception):
    def __init__(self):
        super().__init__('Please provide a sorted List')

class binary_input(ui):
    def search_input(self):
        List,key = super().search_input()
        if List == sorted(List):
            return List,key
        else:
            raise NotSorted

def binary(List,key):
    def find(low,high):
        if low <= high:
            mid = (low + high) // 2
            if List[mid] == key:
                return f'{key} found at index {mid} in {List}'
            elif List[mid] < key:
                return find(mid+1,high)
            else:
                return find(low,mid-1)
        else:
            return f'{key} is not in {List}'
    return find(0,len(List) - 1)

binput = binary_input()
try:
    print(binary(*binput.search_input()))
except NotSorted as e:
    print(e.__str__())