from Pr1_Biriuk import calculate

print("\n" + "="*50)
print("ЗАПУСК ASSERT ТЕСТІВ")
print("="*50)

# Тест 1: додавання
assert calculate("2+3") == 5
print("✓ Тест 1 пройдено: 2+3 = 5")

# Тест 2: віднімання
assert calculate("10-5") == 5
print("✓ Тест 2 пройдено: 10-5 = 5")

# Тест 3: множення
assert calculate("3*4") == 12
print("✓ Тест 3 пройдено: 3*4 = 12")

# Тест 4: ділення
assert calculate("8/2") == 4
print("✓ Тест 4 пройдено: 8/2 = 4")

print("\nУСІ  ASSERT-ТЕСТИ ПРОЙДЕНО!")