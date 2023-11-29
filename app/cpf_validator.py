import re


class CPF:
    """
    Representa um CPF brasileiro (Cadastro de Pessoas Físicas).
    Lida com a formatação e validação do CPF.
    """

    def __init__(self, cpf_string, formatter, validator):
        """
        Inicializa o objeto CPF com uma string bruta de CPF, um formatador
        e um validador.
        """
        self.raw_cpf = cpf_string
        self.formatter = formatter
        self.validator = validator
        self.cpf = self.formatter.format(cpf_string)

    def is_valid(self):
        """Verifica se o CPF é válido usando o validador fornecido."""
        return self.validator.validate(self.cpf)


class CPFFormatter:
    """Lida com a formatação de strings de CPF."""

    @staticmethod
    def format(cpf_string):
        """Formata a string do CPF removendo caracteres não numéricos."""
        return re.sub(r"[^\d]", "", cpf_string)


class CPFValidator:
    """
    Valida um CPF usando uma série de regras.
    """

    def __init__(self):
        """Inicializa com uma lista de regras de validação."""
        self.rules = [FormatRule(), DigitRule()]

    def validate(self, cpf):
        """
        Valida o CPF aplicando todas as regras.
        Retorna True se todas as regras forem cumpridas.
        """
        return all(rule.validate(cpf) for rule in self.rules)


class FormatRule:
    """Valida o formato do CPF."""

    @staticmethod
    def validate(cpf):
        """Verifica o comprimento e a repetição de caracteres no CPF."""
        if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
            return False
        return True


class DigitRule:
    """Valida os dígitos do CPF."""

    @staticmethod
    def calculate_digit(cpf, factor):
        """
        Calcula um dígito do CPF usando um fator dado.
        """
        sum_digits = sum(int(digit) * factor for digit, factor in zip(cpf, range(factor, 1, -1)))
        return (sum_digits * 10) % 11

    @staticmethod
    def validate(cpf):
        """Valida os dígitos do CPF."""
        digit1 = DigitRule.calculate_digit(cpf, 10)
        digit1 = 0 if digit1 == 10 else digit1

        digit2 = DigitRule.calculate_digit(cpf[:9] + str(digit1), 11)
        digit2 = 0 if digit2 == 10 else digit2

        return str(digit1) == cpf[9] and str(digit2) == cpf[10]


def main():
    """Entrada do usuário para CPF e verificação de validade."""
    cpf_input = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf = CPF(cpf_input, CPFFormatter(), CPFValidator())
    if cpf.is_valid():
        print("CPF é válido")
    else:
        print("CPF inválido")


if __name__ == "__main__":
    main()
