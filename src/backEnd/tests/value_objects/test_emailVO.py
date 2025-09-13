import pytest
from backEnd.value_objects.emailVO  import EmailVO  # supondo que seu arquivo chama email_vo.py

def test_cria_email_valido():
    email = EmailVO("usuario@dominio.com")
    assert str(email) == "usuario@dominio.com"

def test_email_invalido_dispara_excecao():
    with pytest.raises(ValueError) as exc_info:
        EmailVO("usuario@@dominio.com")
    assert "Email inválido" in str(exc_info.value)

def test_emails_iguais_sao_iguais():
    e1 = EmailVO("teste@dominio.com")
    e2 = EmailVO("teste@dominio.com")
    assert e1 == e2

def test_emails_diferentes_nao_sao_iguais():
    e1 = EmailVO("teste1@dominio.com")
    e2 = EmailVO("teste2@dominio.com")
    
    assert e2.value == 'teste2@dominio.com'
    assert e1 != e2
