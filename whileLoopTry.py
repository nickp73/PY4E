largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        fnum = int(num)
    except ValueError:
        print("You must enter a valid number!")
        continue
    if largest is None or fnum > largest:
        largest = fnum
    if smallest is None or fnum < smallest:
        smallest = fnum
print('Maximum is', largest)
print('Minimum is', smallest)