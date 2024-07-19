from user_input import user_input

def selection(List):
    for i in range(len(List)):
        mini = i
        for j in range(i+1,len(List)):
            if List[j] < List[mini]:
                mini = j
        List[i],List[mini] = List[mini],List[i]
    return List
ui = user_input()
print(selection(ui.sort_input()))