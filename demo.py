import pytest
import pytest_benchmark
import time

def fast_function():
    time.sleep(0.001)
    return True

def slow_function(how_slow = 0.15):
    time_to_sleep = how_slow * 1
    time.sleep(time_to_sleep)
    return True

def test_fast_function():
    result = fast_function()
    assert result == True

def test_slow_function():
    result = slow_function()
    assert result == True

def test_benchmark_fast(benchmark):
    result = benchmark(fast_function)
    assert result == True

def test_benchmark_slow(benchmark):
    result = benchmark(slow_function)
    assert result == True

def test_benchmark_slow_input(benchmark):
    result = benchmark(slow_function, 0.8)
    assert result == True