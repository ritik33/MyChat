
# MyChat
Real time chat web app. Make friends and chat with them.

## Tech Stack

- Python
- JavaScript
- Django
- Django Channels
- Bootstrap
- PostgreSQL

## Run Locally

Clone the project

```bash
git clone https://github.com/ritik33/MyChat.git

```

Setup a PostgreSQL instance with the following data

```
DB NAME: 'MyChat',
USER: 'postgres',
PASSWORD: 'postgres',
HOST: 'localhost',
PORT': '5432'
```
OR update `settings.py` file with the following PostgreSQL configuration

```
DB_NAME = "your postgres db name"
DB_USER = "your postgres db user"
DB_PASSWORD = "your postgres db password"
DB_HOST = "your postgres db host"
DB_PORT = "your postgres port"
```

Create a virtual environment

```bash
pip install virtualenv

virtualenv venv
```

Activate the virtual environment

```bash
venv\scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```
python manage.py makemigrations

python manage.py migrate
```

Start the server

```bash
python manage.py runserver
```

> ⚠ Development server will start [here](http://127.0.0.1:8000/)
## Screenshots


![register](https://user-images.githubusercontent.com/54118809/217245066-be95937e-d470-42f5-8fb5-4ae1fa8f42df.png) | ![login](https://user-images.githubusercontent.com/54118809/217245299-8fa785ae-1c55-49be-9a41-2e9f8226e596.png)
:-:|:-:
![profile](https://user-images.githubusercontent.com/54118809/217245308-e9663ca4-855c-4e8c-a53e-f5e37d7939bd.png) | ![friend_requests](https://user-images.githubusercontent.com/54118809/217245334-6c8c2f62-1c57-4b50-89f8-58ca00547bce.png)
![users](https://user-images.githubusercontent.com/54118809/217245342-c67d3c3d-0bdf-4a6c-8d41-c2b134dbeb81.png) | ![chatroom](https://user-images.githubusercontent.com/54118809/217245353-af24475a-86c7-4a32-bed6-618543ec46f8.png)
