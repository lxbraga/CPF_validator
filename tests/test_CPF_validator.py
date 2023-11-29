import pytest
import random
import app.CPF_validator as CPF_validator

"""
Layout de função para teste
def test_function():
    variables

    try:
        assert function() == True
    except AssertionError as e:
        raise AssertionError(f"Erro na function: {e}")

"""

# Função para gerar um CPF aleatório sem sequências de números repetidos
def generate_random_cpf()->str:
    return str(random.randint(10000000000, 99999999999))


# Função para formatar um CPF
def format_cpf(cpf)->str:
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


# Teste para verificar a formatação do CPF
def test_cpf_formatting():
    random_cpf = generate_random_cpf()
    formatted_cpf = format_cpf(random_cpf)

    assert formatted_cpf == f"{random_cpf[:3]}.{random_cpf[3:6]}.{random_cpf[6:9]}-{random_cpf[9:]}"


# Teste para verificar a validação de CPF válido
def test_valid_cpf_validation():
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    valid_cpf = CPF_validator.CPF("123.456.789-09", CPF_validator.CPFFormatter(),CPF_validator.CPFValidator())

    assert valid_cpf.is_valid() == True


# Teste para verificar a validação de CPF inválido
def test_invalid_cpf_validation():
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    invalid_cpf = CPF_validator.CPF("123.456.789-00", CPF_validator.CPFFormatter(),CPF_validator.CPFValidator())
    invalid_cpf.cpf = invalid_cpf.cpf[:-1]

    assert invalid_cpf.is_valid() == False


# Teste para verificar a validação de CPF com comprimento válido
def test_valid_length_cpf_validation():
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    valid_length_cpf = CPF_validator.CPF("123.456.789-09", CPF_validator.CPFFormatter(),CPF_validator.CPFValidator())

    assert valid_length_cpf.is_valid() == True


# Teste para verificar a validação de CPF com comprimento inválido
def test_invalid_length_cpf_validation():
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    invalid_length_cpf = CPF_validator.CPF("123.456.789-00", CPF_validator.CPFFormatter(),CPF_validator.CPFValidator())
    invalid_length_cpf.cpf = invalid_length_cpf.cpf[:-1]
    
    assert invalid_length_cpf.is_valid() == False


# Teste para verificar se a regra de formato está sendo aplicada corretamente
def test_format_rule():
    format_rule = CPF_validator.FormatRule()

    # Teste com CPF válido
    assert format_rule.validate("12345678909") == True

    # Teste com CPF inválido (comprimento errado)
    assert format_rule.validate("1234567890") == False


# Teste para verificar se a regra de dígito está sendo aplicada corretamente
def test_digit_rule():
    digit_rule = CPF_validator.DigitRule()

    # Teste com CPF válido
    assert digit_rule.validate("12345678909") == True

    # Teste com CPF inválido (dígitos errados)
    assert digit_rule.validate("12345678900") == False

