.PHONY: help deps

help: 			## Show this help
	@echo "usage: make [target] ..."
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

virtualenv:		## Create virtualenv and activate it
	python -m .venv

deps:			## install dependencies
	pip install pip-tools
	pip-sync requirements.dev.txt
	pip install -e .
	pre-commit install

run: 			## Run the application
	python -m rad_task