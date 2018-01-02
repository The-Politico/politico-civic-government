test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd government/staticapp/

database:
	dropdb government --if-exists
	createdb government
