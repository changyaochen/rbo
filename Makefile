.PHONY: lint test publish

lint:
	poetry run pylint --rcfile=pylintrc ./tests ./rbo

test:
	poetry run pytest ./tests/*

publish:
	poetry publish --build
