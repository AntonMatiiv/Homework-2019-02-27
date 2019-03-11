def range_via_generator(start, end, step):
    while start <= end - 1:
        yield start
        start += step

#for i in range_via_generator(1, 15, 3):
    #print(i)
