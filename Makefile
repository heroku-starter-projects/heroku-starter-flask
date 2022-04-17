## Variables ##

main_package := app
test_package := test
server := server.py

ifndef PIPENV_IN_DOCKER
pyrun := pipenv run
venv := .venv
else
pyrun :=
venv :=
endif

run: install
	$(pyrun) python $(server)

watch: install
	 FLASK_DEBUG=1 $(pyrun) python $(server)

test: install
	$(pyrun) python -m unittest discover

coverage: install
	$(pyrun) coverage run --source=$(main_package) -m unittest discover
	$(pyrun) coverage report -m

coverage-report: coverage
	$(pyrun) coverage html
	open htmlcov/index.html

## Install

install: $(venv)
$(venv): $(venv)/bin/activate
$(venv)/bin/activate: Pipfile.lock
	$(call log, "Installing dependencies ...")
	pipenv --version &> /dev/null || pip install pipenv
	PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
	touch $(venv)/bin/activate
	$(call log, "Installing dependencies Done")

## Misc

db-upgrade: install
	$(pyrun) alembic upgrade head

db-downgrade: install
	$(pyrun) alembic downgrade base

lint: install
	$(call log, "Running linter ...")
	find $(main_package) -iname "*.py" | xargs $(pyrun) flake8
	find $(test_package) -iname "*.py" | xargs $(pyrun) flake8
	$(call log, "Running linter Done")

format: install
	$(call log, "Running formatter ...")
	$(pyrun) autopep8 $(main_package) $(test_package) -r -i
	$(call log, "Running formatter Done")

clean:
	$(call log, "Cleaning ...")
	find . -name \*.pyc -delete -o -name \*.pyo -delete -o -name __pycache__ -delete
	rm -f .coverage
	rm -rf htmlcov
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	$(call log, "Cleaning Done")

fclean:
	$(call log, "Deep cleaning ...")
	$(MAKE) clean > /dev/null
	rm -rf .venv
	rm -rf .git/hooks/pre-commit
	$(call log, "Deep cleaning Done")

## Makefile ##

rules :=	all					\
			run					\
			test				\
			coverage			\
			coverage-report		\
			db-upgrade			\
			lint				\
			format				\
			install-git-hooks	\
			clean fclean		\


.PHONY: $(rules)
.SILENT: $(rules) $(venv)/bin/activate
