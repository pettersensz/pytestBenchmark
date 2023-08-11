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

## Handy tips
- Can pass in arguments to the function under test: `result = benchmark(my_function, 1234)`
- Can use `--benchmark-autosave` flag to save the current run to a json file
- Can use `--benchmark-compare=0001` to compare with previously saved run (with specified run number)
- Can use `--benchmark-columns="mean, max"` to specify which columns to show in results table
- There's also a "pedantic" mode available, allows for even more customization:
    - list of args or kwargs to pass to target function
    - call a setup function before calling the target function
    - specify number of rounds, iterations and warmup_rounds
    - `benchmark.pedantic(stuff, args=(1, 2, 3), kwargs={'foo': 'bar'}, iterations=10, rounds=100)`