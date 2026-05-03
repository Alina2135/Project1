from Pr1_Biriuk import calculate

print("\n" + "="*50)
print("ЗАПУСК ASSERT ТЕСТІВ")
print("="*50)

# Тест 1: додавання
def test_add():
    assert calculate("2+3") == 5

# Тест 2: віднімання
def test_sub():
    assert calculate("10-5") == 5

# Тест 3: множення
def test_mul():
    assert calculate("3*4") == 12

# Тест 4: ділення
def test_div():
    assert calculate("8/2") == 4

print("\nУСІ  ASSERT-ТЕСТИ ПРОЙДЕНО!")