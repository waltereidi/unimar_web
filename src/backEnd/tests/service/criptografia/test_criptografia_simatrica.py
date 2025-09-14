import pytest
from backEnd.service.criptografia.criptografia_simetrica import CriptografiaSimetrica  # Substitua pelo caminho correto do seu arquivo

def test_criptografia_descriptografia():
    mensagem = "123"

    # Cria uma instância da classe
    cript = CriptografiaSimetrica()

    # Criptografa a mensagem
    criptografado = cript.criptografar(mensagem)
    print(criptografado)
    # Verifica se a mensagem criptografada é diferente do original
    assert criptografado != mensagem.encode('utf-8')

    # Descriptografa a mensagem
    original = cript.descriptografar('criptografado')

    # Verifica se a descriptografia retorna a mensagem original
    assert original == mensagem

