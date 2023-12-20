# generate_secret_key.py

from django.core.management.utils import get_random_secret_key


def generate_secret_key():
    key = get_random_secret_key()
    return f"SECRET_KEY = 'django-insecure-{key}'\n"


def update_settings(secret_key):
    with open('config/settings/base.py', 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('SECRET_KEY'):
            lines[i] = secret_key
            break

    with open('config/settings/base.py', 'w') as f:
        f.writelines(lines)


if __name__ == "__main__":
    new_secret_key = generate_secret_key()
    update_settings(new_secret_key)
    print(f"New Secret Key generated and updated in settings: {new_secret_key.strip()}")
