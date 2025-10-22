PYTHON=python3

VENV_PATH=.venv
BIN_PATH=$(VENV_PATH)/bin
REQUIREMENTS_PATH=requirements.txt


init: clean
	$(PYTHON) -m venv $(VENV_PATH)
	$(BIN_PATH)/pip install -r $(REQUIREMENTS_PATH)

test:
	pytest

clean:
	rm -rf $(VENV_PATH)