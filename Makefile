run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

createadmin:
	python manage.py createsuperuser

# linters

pre_commit:
	pre-commit install

# DB
run_dev_db:
	docker-compose up dev_db

run_prod_db:
	docker-compose up prod_db
