# Dict comprehensions
# Создайте словарь с помощью генератора словарей,
# так чтобы его ключами были числа от 1 до 20, а значениями кубы этих чисел.


dict_ = {elem: elem ** 3 for elem in range(1, 21)}
print(dict_)
