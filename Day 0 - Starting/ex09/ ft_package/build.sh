python -m pip install --upgrade pip
python -m pip install setuptools wheel twine
python setup.py sdist bdist_wheel
twine upload --skip-existing dist/*

