from functools import lru_cache
import cProfile

def simple_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return simple_fibonacci(n-1) + simple_fibonacci(n-2)

@lru_cache(maxsize=None)
def memorized_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memorized_fibonacci(n-1) + memorized_fibonacci(n-2)

if __name__ == '__main__':
    '''
        following result :
         331160284 function calls (4 primitive calls) in 140.165 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  140.165  140.165 <string>:1(<module>)
331160281/1  140.165    0.000  140.165  140.165 lru_cache.py:4(simple_fibonacci)
        1    0.000    0.000  140.165  140.165 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         44 function calls (4 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     41/1    0.000    0.000    0.000    0.000 lru_cache.py:11(memorized_fibonacci)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
    N = 40
    cProfile.run('simple_fibonacci(N)')
    cProfile.run('memorized_fibonacci(N)')
    #print(memorized_fibonacci.cache_info())
