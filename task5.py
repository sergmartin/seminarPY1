"""Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
in
- 3
- 6
- 2
- 1

out
5.099"""

aX = int(input("Введите точку А(x): "))
aY = int(input("Введите точку А(y): "))
bX = int(input("Введите точку B(х): "))
bY = int(input("Введите точку B(y): "))

n = ((bX-aX)**2 + (bY-aY)**2)**0.5
print((int(n * 1000))/1000)