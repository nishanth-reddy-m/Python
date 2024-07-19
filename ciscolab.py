def read_int(prompt, min, max):
    try:
        x = int(input(prompt))
        assert x>=-10 and x<=10
        return x
    except ValueError:
        print('Error: wrong input')
        return read_int(prompt, min, max)
    except AssertionError:
        print(f'Error: the value is not within permitted range ({min}..{max})')
        return read_int(prompt, min, max)

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)