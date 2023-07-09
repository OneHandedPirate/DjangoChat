import os

from dotenv import load_dotenv


load_dotenv()

DJANGO_SK = os.getenv("DJANGO_SK", 'notsecureddjangokey')

POSTGRES_USER = os.getenv("POSTGRES_USER", 'postgres')
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", 'postgres')
POSTGRES_DB = os.getenv("POSTGRES_DB", 'postgres')
POSTGRES_HOST = os.getenv("POSTGRES_HOST", 'localhost')
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

REDIS_HOST = os.getenv("REDIS_HOST", 'localhost')
REDIS_PORT = os.getenv("REDIS_PORT", '6379')
