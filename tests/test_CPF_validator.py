"""
This module contains the tests for the cpf_validator module.
"""

import random
# import pytest
import app.cpf_validator as cpf_validator

# Função para gerar um CPF aleatório sem sequências de números repetidos
def generate_random_cpf() -> str:
    """
    Generate a random CPF (Cadastro de Pessoas Físicas) number.

    Returns:
        str: A randomly generated CPF number.
    """
    return str(random.randint(int(10E10), int(10E11) - 1))


# Função para formatar um CPF
def format_cpf(cpf) -> str:
    """
    Formats a CPF (Brazilian identification number) by adding dots and dashes.

    Args:
        cpf (str): The CPF to be formatted.

    Returns:
        str: The formatted CPF with dots and dashes.

    """
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


# Teste para verificar a formatação do CPF
def test_cpf_formatting():
    """
    Test the formatting of a CPF number.

    This function generates a random CPF number using the `generate_random_cpf` function,
    formats it using the `format_cpf` function, and then checks if the formatted CPF matches
    the expected format.

    The expected format of a CPF is "XXX.XXX.XXX-XX", where each X represents a digit of the CPF.

    Raises:
        AssertionError: If the formatted CPF does not match the expected format.
    """
    random_cpf = generate_random_cpf()
    formatted_cpf = format_cpf(random_cpf)

    assert formatted_cpf == f"{random_cpf[:3]}.{random_cpf[3:6]}.{random_cpf[6:9]}-{random_cpf[9:]}"


# Teste para verificar a validação de CPF válido
def test_valid_cpf_validation():
    """
    Test case to validate a valid CPF.

    This test case creates a CPF object with a valid CPF number and checks if it is considered valid.
    
    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    valid_cpf = cpf_validator.CPF("123.456.789-09", cpf_validator.CPFFormatter(),cpf_validator.CPFValidator())

    assert valid_cpf.is_valid() is True


# Teste para verificar a validação de CPF inválido
def test_invalid_cpf_validation():
    """
    Test case to validate the behavior of the CPF class when an invalid CPF is provided.
    
    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    invalid_cpf = cpf_validator.CPF("123.456.789-00", cpf_validator.CPFFormatter(),cpf_validator.CPFValidator())
    invalid_cpf.cpf = invalid_cpf.cpf[:-1]

    assert invalid_cpf.is_valid() is False


# Teste para verificar a validação de CPF com comprimento válido
def test_valid_length_cpf_validation():
    """
    Test case to verify the validation of a CPF with a valid length.
    
    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    valid_length_cpf = cpf_validator.CPF("123.456.789-09", cpf_validator.CPFFormatter(),cpf_validator.CPFValidator())

    assert valid_length_cpf.is_valid() is True


# Teste para verificar a validação de CPF com comprimento inválido
def test_invalid_length_cpf_validation():
    """
    Test case to validate the behavior of CPF validation when the CPF has an invalid length.
    
    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    # random_cpf = generate_random_cpf()
    # formatted_cpf = format_cpf(random_cpf)
    invalid_length_cpf = cpf_validator.CPF("123.456.789-00", cpf_validator.CPFFormatter(),cpf_validator.CPFValidator())
    invalid_length_cpf.cpf = invalid_length_cpf.cpf[:-1]

    assert invalid_length_cpf.is_valid() is False


# Teste para verificar se a regra de formato está sendo aplicada corretamente
def test_format_rule():
    """
    Test the FormatRule class of the cpf_validator module.

    This function tests the validate() method of the FormatRule class
    by providing valid and invalid CPF numbers as input and asserting
    the expected results.

    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    format_rule = cpf_validator.FormatRule()

    # Teste com CPF válido
    assert format_rule.validate("12345678909") is True

    # Teste com CPF inválido (comprimento errado)
    assert format_rule.validate("1234567890") is False


# Teste para verificar se a regra de dígito está sendo aplicada corretamente
def test_digit_rule():
    """
    Test the DigitRule class of the cpf_validator module.

    This function tests the validate() method of the DigitRule class
    by providing valid and invalid CPF numbers and asserting the expected results.

    Raises:
        AssertionError: If the CPF object is not considered valid.
    """
    digit_rule = cpf_validator.DigitRule()

    # Teste com CPF válido
    assert digit_rule.validate("12345678909") is True

    # Teste com CPF inválido (dígitos errados)
    assert digit_rule.validate("12345678900") is False

