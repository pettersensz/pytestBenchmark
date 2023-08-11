# Quick Intro to pytest-benchmark

`pytest` is one of the most popular testing frameworks for python
`pytest-benchmark` is a pytest fixture ("add-on") for benchmarking code

[pytest-benchmark documentation](https://pytest-benchmark.readthedocs.io/en/latest/index.html)

## Prerequisites
Python env with `pytest` and `pytest-benchmark` installed (available via pip install)

## Quick-start
- Clone this repo
- Ensure env with required libraries is activates
- In terminal, at repo root: `pytest demo.py -v`


## How does it work?
### Regular pytest:
    def my_function():
        do_time_consuming_stuff()
        return True
        
    def test_my_function():
        assert my_function() == True

### Benchmark test:
    def my_function():
        do_time_consuming_stuff()
        return True
        
    def test_my_function(benchmark):
        result = benchmark(my_function)
        assert result == True
