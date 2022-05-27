.PHONY: help deps

help: 			## Show this help
	@echo "usage: make [target] ..."
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

deps:       ## install dependencies
	pip install pip-tools
	pip-sync requirements.dev.txt
	pre-commit install
