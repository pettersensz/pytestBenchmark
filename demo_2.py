import pytest
import time

def fast_function():
    time.sleep(0.001)
    return True

def test_fast_function():
    result = fast_function()
    assert result == True

def setup_function():
    print("Setting up some stuff..")
    time.sleep(0.2)

def test_benchmark_fast(benchmark):
    result = benchmark.pedantic(fast_function, setup=setup_function, rounds=3)
    assert result == True

def kwargs_function(named_arg_1, named_arg_2):
    print(named_arg_1)
    print(named_arg_2)
    time.sleep(0.005)

def test_benchmark_kwargs(benchmark):
    benchmark.pedantic(kwargs_function, 
                       kwargs={"named_arg_1": "Fizz", "named_arg_2": "Buzz"},
                       rounds=2)