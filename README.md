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

## Step 3: Activate Poetry shell

```bash
    poetry shell
```

## Step 4: Initialize a Poetry Project with Django

```bash
    poetry init --no-interaction --dependency django
```

## Step 5: Add Additional Packages

```bash
    poetry add <package_name>
```

## Step 6: Create a Django App

```bash
    python manage.py startapp <app_name>
```
