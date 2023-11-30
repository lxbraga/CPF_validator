# CPF_validator

This app is meant to validate CPF numbers. The documentation is available at [https://lxbraga.github.io/CPF_validator](https://lxbraga.github.io/CPF_validator), built with [MkDocs](https://www.mkdocs.org/).

The group members are:

- [Dávila Meireles](https://github.com/davilameireles)
- [Eduardo Adame Salles](https://github.com/adamesalles)
- [Lucas Braga](https://github.com/lxbraga)
- [William Sena](https://github.com/wllsena)

## Installation

We recommend you to use poetry to install the dependencies.

```bash
poetry install
```

And then you might want to run the app with:

```bash
poetry run python app/main.py
```

If you want to run the tests, you can do it with:

```bash
poetry run coverage run -m pytest
poetry run coverage report -m
```

If you're not using poetry, you can install the dependencies from the [`requirements.txt`](requirements.txt) file.

## Tests coverage

```
❯ poetry run coverage run -m pytest
=========================================================================== test session starts ===========================================================================
platform linux -- Python 3.11.6, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/adame/Documents/Git/CPF_validator
collected 8 items                                                                                                                                                         

tests/test_cpf_validator.py ........                                                                                                                                [100%]

============================================================================ 8 passed in 0.03s ============================================================================
❯ poetry run coverage report -m
Name                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------
app/__init__.py                   0      0   100%
app/cpf_validator.py             36      0   100%
tests/__init__.py                 0      0   100%
tests/test_cpf_validator.py      39      0   100%
-----------------------------------------------------------
TOTAL                            75      0   100%

```

## Build MkDocs

You can build the MkDocs documentation with:

```bash
poetry run mkdocs build
```

Or just run the server with:

```bash
poetry run mkdocs serve
```
