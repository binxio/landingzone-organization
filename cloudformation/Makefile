SHELL = /bin/bash -c
VIRTUAL_ENV = $(shell poetry env info --path)
export BASH_ENV=$(VIRTUAL_ENV)/bin/activate
VERSION=$(shell poetry version -s)

.DEFAULT_GOAL:=help
.PHONY: help
help:  ## Display this help
	awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

../dist/landing-zone-$(VERSION).tar.gz:
	poetry build

.PHONY: build
build: ../dist/landing-zone-$(VERSION).tar.gz ## Build the lambda functions locally
	sam build

.PHONY: deploy
deploy: build ## Deploy the template
	sam deploy

$(VERBOSE).SILENT: