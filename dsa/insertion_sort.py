from user_input import user_input

def insertion(List):
    for i in range(1,len(List)):
        key = List[i]
        j = i - 1
        while j>=0 and List[j] > key:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = key
    return List

ui = user_input()
print(insertion(ui.sort_input()))