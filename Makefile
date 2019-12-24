init:
	pip install -r requirements.txt

test:
	nosetests tests

coverage:
	coverage run -m tests.test_mod
	coverage run -m tests.test_mod2
	coverage html
	coverage report

build:
	echo "build"

deploy:
	echo "deply"