# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

## Python Decorator Function

import time

current_time = time.time()
# print(current_time)

def speed_calc_decorator(function):
    def run_time():
        start_time = time.time()
        function()
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"{function.__name__} run speed: {time_taken}")
    return run_time


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
