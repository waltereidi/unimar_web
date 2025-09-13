import pytest
from backEnd.value_objects.passwordVO import PasswordVO  # supondo que seu arquivo chama password_vo.py

def test_password_vo():
    assert PasswordVO("Abcdefg1").validate()["valid"] is True
    res = PasswordVO("").validate()
    
    print(res['missing'][0])
    print(res['missing'])
    
    assert res["valid"] is False
    assert "uppercase" in res["reasons"]

    res2 = PasswordVO("ABCDEFGH").validate()
    assert "digit" in res2["reasons"]
    assert "length" not in res2["reasons"]  # tem 8 caracteres