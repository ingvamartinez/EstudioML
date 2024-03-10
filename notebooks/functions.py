import os
from pathlib import Path

P='a'
def pathfile():
    global P
    root=Path(".").resolve().parent
    fn=input("Ingrese el nombre del archivo: ")
    P=os.path.join(root,'data','raw',fn)
    print(P)
    return P
