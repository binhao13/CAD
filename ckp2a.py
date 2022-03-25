from cmath import pi
import math

n = float(input("Digite o seu numero de chamada: "))
z = n + 12
df = (n+8)*1.6
if n >= 1 and n<= 10:
    m = 4
    dp = m*z
elif n >= 11 and n <= 20:
    m = 3.25
    dp = m*z
elif n >= 21 and n <= 2.5:
    m = 2.5
    dp = m*z
elif n >= 30:
    m = 2
    dp = m*z
p = m*pi
a = m
b = 1.167*m
s = p/2
t = 14.5
db = dp*math.cos(math.radians(t))
q = float(input("Escolha um número entre 6 a 20 para o calculo do comprimento do dente: "))
l = q*m
print(f"Seu valor de Z e {z:.2f}")
f = float(input("Digite o valor de f baseado no seu valor de Z e da tabela: "))
f1 = float(input("Digite o valor de f' baseado no seu valor de Z e da tabela: "))
r = f*m
r2 = f1*m
g = p/2
r1 = 0.17*m
de = 2*m+dp
di = dp - 2*b
print(f"Z = {z:.2f} ; df = {df:.2f} ; dp = {dp:.2f} ; p = {p:.2f} ; a = {a:.2f} ; b = {b:.2f} ; s = {s:.2f} ; db = {db:.2f} ; l = {l:.2f} ; R = {r:.2f} ; r = {r2:.2f} ; G = {g:.2f} ; r1 = {r1:.2f} ; de = {de:.2f} ; di = {di:.2f} ;")
