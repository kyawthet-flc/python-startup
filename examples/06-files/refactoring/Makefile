# Simple makefile for processfile development

CURRENT_DIR = $(shell pwd)

all: pep8 test

test:
	@echo "Running tests..."
	PYTHONPATH=$(CURRENT_DIR) py.test
	@echo "Done."

doc:
	@echo "Building documentation..."
	@cd docs && PYTHONPATH=$(CURRENT_DIR) make SPHINXOPTS=-j4 html && cd ..
	@echo "Done."
	@echo "Open docs/_build/html/index.html with your favourite browser "docs/build/html/index.html
	@echo
	@echo "sensible-browser docs/build/html/index.html &"
	@echo

doc-pdf:
	@echo "Building documentation (pdf)..."
	@cd docs && PYTHONPATH=$(CURRENT_DIR) make SPHINXOPTS=-j4 latextpdf && cd ..
	@echo "Done."
	@echo "Open docs/_build/latexpdf/ with your favourite PDF reader"

pep8:
	@echo "Cheking PEP8 coding style..."
	@pep8 . --exclude="docs,test*" --max-line-length=90 --ignore=E127,E265
	@echo "Done."

clean: clean-bytecode clean-doc clean-egg clean-build

clean-bytecode:
	@echo "Cleaning byte code..."
	@find -name \*.py[co] -exec rm {} \;
	@echo "Done."

clean-doc:
	@echo "Cleaning doc..."
	@make -C docs clean
	@echo "Done."

clean-egg:
	@echo "Cleaning egg..."
	@rm -rf *.egg-info
	@echo "Done."

clean-build:
	@echo "Cleaning build..."
	@ rm -rf build
	@ rm -rf dist
	@echo "Done."
