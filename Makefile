.PHONY: install test upload docs


install: clean
	pip install -e .[docs,test]

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

test:
	py.test

retest:
	py.test -vvv --lf

coverage:
	py.test --cov=django_rangepaginator --cov-report=term-missing --cov-report=html

lint:
	flake8 src/ tests/
	isort --recursive --check-only --diff src tests


docs:
	$(MAKE) -C docs html

release:
	rm -rf dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*
