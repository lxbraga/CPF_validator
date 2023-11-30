# Welcome to CPF Validator

The CPF Validator is a simple app to validate CPF numbers.

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

If you're not using poetry, you can install the dependencies from the [`requirements.txt`](../requirements.txt) file.


## Project layout

```
app # The app folder
    cpf_validator.py # The CPF validator module
    main.py # The main module
docs
    about.md # The about page
    index.md # The index page
mkdocs.yml # The mkdocs configuration file
poetry.lock # The poetry lock file
pyproject.toml # The poetry configuration file
README.md # The README file
requirements.txt # The requirements file
tests # The tests folder
    test_cpf_validator.py # The tests for the CPF validator module
```

## API Reference

::: app.cpf_validator

## Tests Reference

::: tests.test_cpf_validator
