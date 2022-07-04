
init:
	pip install pipenv
	pipenv install --dev

test: init
	pipenv run test

run: init
	pipenv run server
