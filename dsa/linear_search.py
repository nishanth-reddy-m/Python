from user_input import user_input
def linear(List,key):
    i = 0
    while(i < len(List)):
        if List[i] == key:
            return f'{key} found at index {i} in {List}'
        i += 1
    return f'{key} is not in {List}'
ui = user_input()
print(linear(*ui.search_input()))