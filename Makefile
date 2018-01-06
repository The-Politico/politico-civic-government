test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

database:
	dropdb government --if-exists
	createdb government
