nc = float(input("Digite seu número de chamada: "))

if nc >= 1 and nc <= 10:
    m = 4
    beta = 20
elif nc >= 11 and nc <= 20:
    m = 3.25
    beta = 30
elif nc >= 21 and nc <= 30:
    m = 2.5
    beta = 40
elif nc >= 31:
    m = 2
    beta = 50
    
z = nc + 12
teta = 14.5
df = (nc + 8)*1.6

if nc % 2 == 0:
    h = "hélice direita"
else:
    h = "hélice esquerda"
print(f"Nc = {nc} // M = {m} // Beta = {beta:.2f}° // Z = {z} // Teta = {teta:.2f}° // df = {df:.2f} mm // {h}")
