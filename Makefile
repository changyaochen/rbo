.PHONY: lint test

lint:
	poetry run pylint --rcfile=pylintrc ./tests

test:
	poetry run pytest ./tests/*
