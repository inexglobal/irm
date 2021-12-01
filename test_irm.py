import gc
gc.collect()
from IRM import *
from microbit import pin12
pin12.set_pull(pin12.PULL_UP)
d = IRM()
while True:
    key=d.get(pin12)
    if(key!=-1):
        print(key)