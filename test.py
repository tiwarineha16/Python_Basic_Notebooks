import os
import pandas as pd
import numpy as np
import sklearn as sklearn


class Greeting: 
    def greet(self):
        print("Hi")
        
def hello_world():
    message= "Hello, World!"
    greeter=Greeting()
    greet_function=getattr(greeter, "greet")
    greet_function()
    
if __name__ == "__main__":
    hello_world()