# MrSwats' health Django App

This is my preferred way of writing a health check endpoint in django.

## Virtual Environment

Create a virtual Environment

```
virtualenv .venv -p pytthon 3.14
source .venv/bin/activate
```

## Tests

Using pytest for Tests

```
python -m pytest
```

## Formatting and Linting

Using pre-commit for linting and formatting

```
pre-commit install
pre-commit run --all-files
```
