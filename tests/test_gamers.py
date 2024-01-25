import pytest
from gamers import Gamer

def test_gamer_has_attributes():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'name'), "Класс 'Gamer' не содержит атрибут 'name'"
    assert hasattr(gamer, 'age'), "Класс 'Gamer' не содержит атрибут 'age'"

def test_gamer_has_attributes_nickaname():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'nickaname'), "Класс 'Gamer' не содержит атрибут 'nickaname'"


def test_gamer_has_attribute_email():
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    assert hasattr(gamer, 'email'), "Класс 'Gamer' не содержит атрибут 'email'"

def test_introduce(capsys):
    gamer = Gamer("Иван", 14, "John", "john@gmail.com")
    gamer.introduce()
    captured = capsys.readouterr()
    expected_output = "Привет, меня зовут Иван, мне 14 лет. Всегда на связи по john@gmail.com. Ищи меня в игре по нику John"
    assert expected_output in captured.out, f"Метод 'introduce' выводит неверный результат. Ожидаемый: {expected_output}, Фактический: {captured.out}"

if __name__ == "__main__":
    pytest.main(["-v"])
