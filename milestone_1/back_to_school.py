eq = input("Р’РІРµРґС–С‚СЊ РєРІР°РґСЂР°С‚РЅРµ СЂС–РІРЅСЏРЅРЅСЏ РІ С„РѕСЂРјР°С‚С–: ax^2 + bx + c = 0: ").replace(" ", "")
pos_x2 = eq.find("x^2")
a = int(eq[:pos_x2])

pos_x = eq.find("x", pos_x2 + 3)
b = int(eq[pos_x2 + 3:pos_x])

pos_eq = eq.find("=")
c = int(eq[pos_x + 1:pos_eq])

dis = (b - 4 * a * c)**0.5


x1 = (-b + dis) / (2 * a)
x2 = (-b - dis) / (2 * a)

print(x1, x2)