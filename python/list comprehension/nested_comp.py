

def example_1():
    non_flat = [ [1,2,3], [4,5,6], [7,8]]
                # outter loop
                                         # inner loop
    print([num for sub_list in non_flat for num in sub_list])


def example_2():
    nums = [1, 2, 3, 4]
    fruits = ['peach', 'apple', 'pears', 'orange']

                        # outter for loop
                                        # inner for loop
    print([(num, fruit) for num in nums for fruit in fruits])




example_2()
example_1()