from api import run as r1
from apiC import run as r2
from apiI import run as r3

def run(start, end):
    print("start collection between", start, "and", end)
    r1(start, end)
    r2(start, end)
    r3(start, end)
