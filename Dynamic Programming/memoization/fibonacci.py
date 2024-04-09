import time
from functools import cache
def main():
    def fib(n,table):
        if(n<2):
            return n
        if(table.get(n)!=None):
            return table[n]
        return table[n]=fib(n-1,table)+fib(n-2,table)     
    table=dict()
    start=time.time()
    print(fib(30,table))
    end=time.time()
    print(f"time taken: {end-start}")
main()    
    