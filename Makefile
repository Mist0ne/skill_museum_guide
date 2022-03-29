.PHONY: \
	all install run

all: .make-install

install: .make-install

.make-install-pipenv:
	@if ! which pipenv &> /dev/null; then \
		pip install pipenv; \
	fi
	@touch $@

.make-install: Pipfile .make-install-pipenv
	pipenv install -d
	@touch $@

run: .make-install
	uvicorn src.skill_museum_guide.application:app --reload

flake:
	flake8 src/skill_museum_guide
	flake8 src/tests

mypy:
	mypy src/skill_museum_guide

isort:
	isort setup.py
	isort src/skill_museum_guide
	isort src/tests

test:
	pytest -q src/tests
