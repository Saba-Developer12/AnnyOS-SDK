PYTHON ?= python3

.PHONY: all build

all: build

build:
	$(PYTHON) tools/build_samples.py
