install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	pytest --nbval descriptive_statistics.ipynb
format:	
	black *.py 

lint:
	ruff *.py

all: install lint test format
