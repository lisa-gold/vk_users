install:
	poetry install

dev:
	poetry run flask --app vk_users:app run

lint:
	poetry run flake8 vk_users/app.py

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) vk_users:app

build:
	./build.sh
