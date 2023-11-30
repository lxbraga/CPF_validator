import re

class CPFFormatter:
    """
    Handles CPF string formatting.
    
    Static Methods:
        format: Formats the CPF string by removing non-numeric characters.
    """

    @staticmethod
    def format(cpf_string: str) -> str:
        """Formats the CPF string by removing non-numeric characters.

        Args:
            cpf_string (str): The CPF string to be formatted.

        Returns:
            str: The formatted CPF string with only numeric characters.
        """
        return re.sub(r"[^\d]", "", cpf_string)


class FormatRule:
    """
    Validates the CPF format.
    
    Static Methods:
        validate: Checks the length and character repetition in the CPF.
    """

    @staticmethod
    def validate(cpf: str) -> bool:
        """Checks the length and character repetition in the CPF.

        Args:
            cpf (str): The CPF to be validated.

        Returns:
            bool: True if the CPF format is valid, False otherwise.
        """
        if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
            return False
        return True


class DigitRule:
    """
    Validates the CPF digits.
    
    Static Methods:
        calculate_digit: Calculates a CPF digit using a given factor.
        validate: Validates the CPF digits.
    """

    @staticmethod
    def calculate_digit(cpf: str, factor: int) -> int:
        """
        Calculates a CPF digit using a given factor.

        Args:
            cpf (str): The CPF number.
            factor (int): The factor used in the calculation.

        Returns:
            int: The calculated CPF digit.
        """
        sum_digits = sum(
            int(digit) * factor for digit, factor in zip(cpf, range(factor, 1, -1))
        )
        return (sum_digits * 10) % 11

    @staticmethod
    def validate(cpf: str) -> bool:
        """
        Validates the CPF digits.

        Args:
            cpf (str): The CPF number.

        Returns:
            bool: True if the CPF digits are valid, False otherwise.
        """
        digit1 = DigitRule.calculate_digit(cpf, 10)
        digit1 = 0 if digit1 == 10 else digit1

        digit2 = DigitRule.calculate_digit(cpf[:9] + str(digit1), 11)
        digit2 = 0 if digit2 == 10 else digit2

        return str(digit1) == cpf[9] and str(digit2) == cpf[10]


class CPFValidator:
    """
    Validates a CPF using a set of rules.

    Attributes:
        rules (list): A list of validation rules to be applied.
        
    Methods:
        validate: Validates the CPF by applying all the rules.
    """

    def __init__(self):
        """Initializes with a list of validation rules."""
        self.rules = [FormatRule(), DigitRule()]

    def validate(self, cpf: str) -> bool:
        """
        Validates the CPF by applying all the rules.

        Args:
            cpf (str): The CPF to be validated.

        Returns:
            bool: True if all rules are satisfied, False otherwise.
        """
        return all(rule.validate(cpf) for rule in self.rules)


class CPF:
    """
    Represents a Brazilian CPF (Cadastro de Pessoas Físicas).
    Handles CPF formatting and validation.
    
    Attributes:
        raw_cpf (str): The raw CPF string.
        formatter (CPFFormatter): The formatter object responsible for CPF formatting.
        validator (CPFValidator): The validator object responsible for CPF validation.
        cpf (str): The formatted CPF string.
        
    Methods:
        is_valid: Checks if the CPF is valid using the provided validator.
    """

    def __init__(
        self, cpf_string: str, formatter: CPFFormatter, validator: CPFValidator
    ):
        """
        Initializes the CPF object with a raw CPF string, a formatter,
        and a validator.

        Args:
            cpf_string (str): The raw CPF string.
            formatter (CPFFormatter): The formatter object responsible for CPF formatting.
            validator (CPFValidator): The validator object responsible for CPF validation.
        """
        self.raw_cpf = cpf_string
        self.formatter = formatter
        self.validator = validator
        self.cpf = self.formatter.format(cpf_string)

    def is_valid(self) -> bool:
        """
        Checks if the CPF is valid using the provided validator.

        Returns:
            bool: True if the CPF is valid, False otherwise.
        """
        return self.validator.validate(self.cpf)