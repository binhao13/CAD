from ctypes.wintypes import HPALETTE
from msvcrt import kbhit


n = float(input("Digite seu número de chamada: "))
d1 = 0.0133*(n**2)-0.015*n+9.9852
e = -0.5*n + 29.5
c = 0
k = 1
while c != k:
    t = float(input("Escolha um valor de hp: "))
    h = 2*e - 8 + t 
    if t < h:
        c = k
dp = ((e+d1)/1.5)+((n + 8)/3)
print(f"d1: {d1:.2f} || e: {e:.2f} || h: {h:.2f} || {1.2*d1:.2f}<= d2 <= {1.8*d1:.2f} || dp: {dp:.2f} ")

