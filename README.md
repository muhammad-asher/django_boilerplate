# django_boilerplate

# Django Project Setup with Poetry

This guide will walk you through setting up a new Django project using Poetry for dependency management.

## Step 1: Create a Virtual Environment

```bash
    py -m venv venv
    .\venv\Scripts\activate
```
## Step 2: Install Poetry

```bash
    pip install poetry
```


## Step 3: Initialize a Poetry Project to create pyproject.toml file

```bash
    poetry init --no-interaction
```

## Step 4: Activate Poetry shell

```bash
    poetry shell
```

## Step 5: Install django

```bash
    poetry add django
```

## Step 6: Add Additional Packages

```bash
    poetry add <package_name>
```

## Step 7: Generate Secret Key to store it in django

```bash
    python generate_secret_key.py
```

## Step 8: Create a Django App

```bash
    python manage.py startapp <app_name>
```
