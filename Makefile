init:
	echo "init"

install:
	virtualenv ./.venv
	./.venv/bin/pip install -r requirements.txt

unittest:
	./.venv/bin/python -m unittest discover tests

coverage:
	./.venv/bin/coverage run -m unittest discover tests
	./.venv/bin/coverage html
	./.venv/bin/coverage report

build:
	echo "build"

deploy:
	echo "deploy"