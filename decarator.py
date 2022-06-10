'''
Decorator is a function which accept the function name as a parameter and
it has an inner function which collect the values passed to the
called function.
'''
import time
def calc_time(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        res=func(*args, **kwargs)
        end=time.time()
        print(func.__name__+" func took ", str((end-start)*1000)+' milli seconds')
        return res
    return wrapper

@calc_time
def squareit(nums):
    result=[]
    for x in nums:
        result.append(x**2)
    return result

@calc_time
def cubeit(nums):
    result=[]
    for x in nums:
        result.append(x**3)
    return result

x=list(range(1,1000001))
squareit(x)
cubeit(x)