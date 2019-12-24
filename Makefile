init:
	pip install -r requirements.txt

test:
	nosetests tests 

unittest:
	python -m unittest discover tests

coverage:
	coverage run -m unittest discover tests
	coverage html
	coverage report

build:
	echo "build"

deploy:
	echo "deploy"