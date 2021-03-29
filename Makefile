.PHONY: lint test

lint:
	poetry run pylint --rcfile=pylintrc ./tests ./rbo

test:
	poetry run pytest ./tests/*
