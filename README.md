# Commands for setup

- `git clone https://github.com/gyarab/2023_wa_sz_svacek_gaflix.git`
- `py -3 -m venv venv`
- `source ./venv/Scripts/activate`
- `pip install -r requirements.txt`

## Alias

- `python manage.py runserver` (`nano ~/.bashrc`; `alias behej='python manage.py runserver'`; `source ~/.bashrc`)

## Migrations and superuser

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

