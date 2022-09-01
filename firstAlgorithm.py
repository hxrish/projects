def square(tosquare):
    running_total = 0
    for i in range(tosquare):
        running_total += tosquare
        
    return running_total

tosquare = int(input('> '))
result = square(tosquare)
print(f'The square of {tosquare} is {result}')
