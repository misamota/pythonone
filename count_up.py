def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    if start < stop:
        count = stop - start + 1
        for i in range(count):
            print(start)
            start += 1
    else:
        print("enter valid numbers")


count_up(5, 7)        
