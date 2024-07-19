def test(min,max):
    try:    
        x = int(input("Enter a number: "))
        assert x>=min and x<=max
        print(f'The number is: {x}')
    except ValueError:
        print('Error: wrong input')
        print('Try again')
        test(min,max)
    except AssertionError:
        print(f'Error: the value is not within permitted range ({min}..{max})')
        print('Try again')
        test(min,max)
    except KeyboardInterrupt:
        print('\nProgram ended')

def main():
    try:
        min,max = int(input('Enter the min range: ')),int(input('Enter the max range: '))
        test(min,max)
    except ValueError:
        print('Invalid Input,Please try again')
        main()
    except KeyboardInterrupt:
        print('\nProgram ended')

main()