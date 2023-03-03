import time

def timed(repetitions):                                                                                                   # sceleton 1 - this is the outter shell that is getting function argumenrs
    from time import perf_counter
    def decorator_function(original_fn):                                                                                   # sceleton 2 - the decorator_function itself.
        def wrapper_function(*args, **kwargs):                                                                              # sceleton 3 - the wrapper_function
            total_elapsed = 0
            for i in range(repetitions):
                start = perf_counter()
                result = original_fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / repetitions
            print("function: {} ran {} time, avarage_timing: {} ".format(original_fn.__name__, repetitions, avg_elapsed))
            return result
        return wrapper_function
    return decorator_function

@timed(5)
def print_out(number, number2):
    print(number + number2)
    time.sleep(2)

print_out(10,7)