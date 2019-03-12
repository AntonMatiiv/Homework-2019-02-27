def range_via_generator(start, end, step):
    current = start 
    while current <= end - 1:
        yield current
        current += step

#for i in range_via_generator(1, 15, 3):
    #print(i)
