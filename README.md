# My First Scrapy

A simple example using a scrapy framework.

The main objective are create any files contains a body about some pages HTML.


## Running (development)

To run application in development time:

```
a) Clone this project in your machine


b) IMPORTANT: Set your version of Python to 3.12.0


c) Run setup command:

- Make setup

OBS:

If not create a virtualenv using the correct version of Python, you can create it manually: 

- poetry env use 3.12
- poetry shell (show the complete path of virtualenv)
- source <path_to_virtualenv>/bin/activate (If name of virtualenv is not in prompt use the command)


d) Install dependencies:

- make install


e) Run ALL tests:

- make test

OBS: 

You can also generate the COVERAGE report of tests:

- make test-cov-rep


f) To list crawlers available:

- scrapy list


g) To execute crawler that go generate the files:

- scrapy crawl quotes

```

## Project Structure

Project structure (considering folder start in `my-first-scrapy`):

```
├── my-first-scrapy
│   ├── tests
│   │   ├── tutorial
│   │   │    ├── spiders
│   │   │    │    ├── __init__.py
│   │   │    │    ├── test_quotes_spider.py
│   │   │    ├── __init__.py
│   │   ├── __init__.py
│   │   ├── conftest.py
│   ├── tutorial
│   │   ├── spiders
│   │   │    ├── __init__.py
│   │   │    ├── quotes_spider.py
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
├── .gitignore
├── .pylintrc
├── LICENSE
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── scrapy.cfg
```

### Main folders

* `my-first-scrapy` - "Main" folder of project.
* `tutorial` - project's Python module, you'll import your code from here.
* `tutorial/spiders` - a directory where you'll later put your spiders.
* `tests` - All tests of application.

### Files

* `.gitignore` - Lists files and directories which should not be added to git repository.
* `.pylintrc` - Define configurations of pylint.
* `LICENCE` - Definitions of licence.
* `Makefile` - Make commands available.
* `poetry.lock` - Define specific versions of dependencies.
* `pyproject.toml` - Some configurations of project.
* `README.md` - Instructions and information to run this project locally.
* `totorial/items.py` - Project items definition file (automatically created by Scrapy).
* `totorial/middlewares.py` - Project middlewares file (automatically created by Scrapy).
* `totorial/pipelines.py` - Project pipelines file (automatically created by Scrapy).
* `totorial/settings.py` - Project settings file (automatically created by Scrapy).
* `scrapy.cfg` -Deploy configuration file (automatically created by Scrapy).

## LINTERS

This project has a some LINTERs to mantain the quality of code.

### Pylint

[Pylint](https://www.pylint.org/) check if the code contains errors of syntax and logical.

```
make pylint
```

### Black

Formats the code according to [PEP-8](https://peps.python.org/pep-0008/) standards.

```
poetry run black --check . (displays which files need adjustments in code formatting);
poetry run black --check --diff <path_to_file> (displays the necessary code formmating changes in a SPECIFIC file - manual adjust);
poetry run black . (performs code formatting "automatically" in ALL files);
poetry run black <path_to_file> (performs code formatting "automatically" in a SPECIFIC file);
```

### Isort

Performs adjustments in "imports" of project - [ISORT](https://pycqa.github.io/isort/).

```
poetry run isort --check . (displays wich files need adjustments in imports);
poetry run isort --check --diff <path_to_file> (displays the necessary adjustments in imports in a SPECIFIC file - manual adjust);
poetry run isort . (performs adjustments in imports "automatically" in ALL files);
poetry run isort <path_to_file> (performs adjustments in imports "automatically" in a SPECIFIC file);
```

### Coverage

To check the COVERAGE of tests of project, is possible execute the follow command:

```
make test-cov
```

To view more details about the COVERAGE, just run the command:

```
make test-cov-rep
```

This will create a folder 'htmlcov' and one file '.coverage' (they should be included in '.gitignore' file). Inside of folder 'htmlcov', just open the 'index.html' file in your browser to view details about the COVERAGE.

To delete the folder and file created, just run command:

```
make clean
```
