<h1 align="center">Django Chat</h1>
<p align="center">Simple chat app with Django, channels and Redis</p>
<hr>

### Prerequisites:
- Installed docker and docker-compose.<br>

### Installation:
- Clone project code and cd into the created folder:
    ```
    git clone https://github.com/OneHandedPirate/DjangoChat.git
    cd DjangoChat
    ```
- If you use `poetry`:
    + Install project dependencies:
      ```
      poetry install
      ```
    + Activate poetry virtual environment:
      ```
      poetry shell
      ```
- If you not use `poetry`: 
    + Create virtual environment:
      ```
      virtualenv venv
      ```
    + Activate newly created venv:
      ```
      source venv/bin/activate
      ```
    + Install dependencies:
      ```
      pip install -r requirements.txt
      ```
- Create `.env` file in the root folder with the following set of variables:
  ```
    DJANGO_SK - Django Secret Key
    POSTGRES_USER - username for postgres
    POSTGRES_PASSWORD - password for postgres
    POSTGRES_DB=postgres - database name for postgres
    POSTGRES_HOST - host for postgres
    POSTGRES_PORT - port for postgres
    
    REDIS_HOST - redis host
    REDIS_PORT - redis port 
  ```
- Bring up docker-compose stack with the following command (in root folder):
  ```
  make up
  ```
  * This command brings up docker-compose stack with postgres (with "db" volume) and redis (both alpine). 
<br><br>
- To down docker-compose stack use `make down` command.
- Run migrations to newly created database:
  ```
  python manage.py migrate
  ```
- Create superuser:
  ```
  python manage.py createsuperuser
  ```
- Start server:
  ```
  python manage.py runserver
  ```
- In the admin tab create room(s) (password for rooms is optional).


### Paths:
`/singup` - registration form.<br>
`/login` - login form for registered users.<br>
`/rooms` - list of chat rooms available.<br>
`/rooms/<slug>` - path to the selected room.