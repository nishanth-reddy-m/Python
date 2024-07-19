from user_input import user_input
def bubble(List):
    def sort(length):
        if length == 1:
            return List
        i = 0
        while(i < length):
            if List[i] > List[i+1]:
                List[i],List[i+1] = List[i+1],List[i]
            i += 1
        return sort(length-1)
    return sort(len(List)-1)
ui = user_input()
print(bubble(ui.sort_input()))