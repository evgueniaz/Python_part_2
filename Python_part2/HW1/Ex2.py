# Треугольник существует только тогда, когда сумма любых двух его сторон
# больше третьей. Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли
# треугольник разносторонним, равнобедренным или равносторонним.


a = float(input("Enter a length of the first side:  "))
b = float(input("Enter a length of the second side:  "))
c = float(input("Enter a length of the third side:  "))
if a + b < c or a + c < b or b + c < a:
    print('A triangle with the given sides does not exist.')
elif a == b == c:
    print("It is an equilateral triangle.")
elif a != b and a != c and c != b:
    print("It is a scalene triangle.")
else:
    print("It is an isosceles triangle.")


