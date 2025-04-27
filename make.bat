@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 2.0.0
REM

IF "%1" == "all" (
	uv run black zapish_logger\
	uv run black tests\
	uv run pylint zapish_logger\
	uv run pytest --cov --cov-report=html -vvv
	uv run bandit -c pyproject.toml -r .
	uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%1" == "build" (
    uv build --wheel --sdist
    GOTO END
)

IF "%1" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "format" (
	uv run black zapish_logger\
	uv run black tests\
    GOTO END
)

IF "%1" == "pylint" (
    uv run pylint zapish_logger\
    GOTO END
)

IF "%1" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%1" == "check-security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%1" == "pip-export" (
	uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

IF "%1" == "pdf" (
    uv run sphinx-build -b rinoh ./docs ./docs/_build/pdf
    GOTO END
)

@ECHO make options
@ECHO     all                   To run all tasks
@ECHO     build                 To build
@ECHO     coverage              To run coverage and display ASCII and output to htmlcov
@ECHO     format                To run black
@ECHO     pylint                To run pylint
@ECHO     pytest                To run pytest with verbose option
@ECHO     check-security        To run bandit
@ECHO     pip-export            To export requirements.txt and requirements-dev.txt
@ECHO     pdf                   To create PDF Docs


:END
