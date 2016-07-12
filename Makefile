help:
	@echo "test - run unit tests"
	@echo "lint - check python lint"

test:
	python manage.py test

lint:
	flake8 app *.py
