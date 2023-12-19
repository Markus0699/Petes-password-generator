from project import get_int
from project import ask_if_satisfied
from project import give_tip


def test_get_int(monkeypatch):
    # Test if the function returns the correct value
    monkeypatch.setattr('builtins.input', lambda _: "1") #
    result = get_int("placeholder")
    assert result == 1

    monkeypatch.setattr('builtins.input', lambda _: "15")
    result = get_int("placeholder")
    assert result == 15

    monkeypatch.setattr('builtins.input', lambda _: "20")
    result = get_int("placeholder")
    assert result == 20


def test_ask_if_satisfied(monkeypatch):
    # Test if yes is reginized correctly
    monkeypatch.setattr('builtins.input', lambda _: "y")
    result = ask_if_satisfied()
    assert result == True

    monkeypatch.setattr('builtins.input', lambda _: "yes")
    result = ask_if_satisfied()
    assert result == True

    monkeypatch.setattr('builtins.input', lambda _: "YES")
    result = ask_if_satisfied()
    assert result == True

    # Test if no is reginized correctly
    monkeypatch.setattr('builtins.input', lambda _: "n")
    result = ask_if_satisfied()
    assert result == False

    monkeypatch.setattr('builtins.input', lambda _: "no")
    result = ask_if_satisfied()
    assert result == False

    monkeypatch.setattr('builtins.input', lambda _: "NO")
    result = ask_if_satisfied()
    assert result == False


def test_give_tip(monkeypatch):
    # Test if feedback for longer password is given
    monkeypatch.setattr('builtins.input', lambda _: "y")
    result = give_tip(1, 1, 1)
    assert result == "Try to make your password longer. A password with 10 or more characters is considered strong."

    monkeypatch.setattr('builtins.input', lambda _: "YES")
    result = give_tip(7, 1, 1)
    assert result == "Try to make your password longer. A password with 10 or more characters is considered strong."

    # Test if feedback for more numbers and special characters is given
    monkeypatch.setattr('builtins.input', lambda _: "YeS")
    result = give_tip(10, 2, 2)
    assert result == "Try to add more numbers and/or special characters to your password. A password with more than 3 characters of each categorie is considered strong."

    monkeypatch.setattr('builtins.input', lambda _: "Y")
    result = give_tip(10, 5, 1)
    assert result == "Try to add more numbers and/or special characters to your password. A password with more than 3 characters of each categorie is considered strong."

    monkeypatch.setattr('builtins.input', lambda _: "y")
    result = give_tip(10, 1, 5)
    assert result == "Try to add more numbers and/or special characters to your password. A password with more than 3 characters of each categorie is considered strong."

    # Test if feedback for a strong password is given
    monkeypatch.setattr('builtins.input', lambda _: "y")
    result = give_tip(4, 3, 3)
    assert result == "Keep up the good work! Your password is quite strong, but you can always make it stronger by making it longer."

    # Test if no feedback is given
    monkeypatch.setattr('builtins.input', lambda _: "n")
    result = give_tip(4, 3, 3)
    assert result == None

    monkeypatch.setattr('builtins.input', lambda _: "NO")
    result = give_tip(10, 1, 3)
    assert result == None

