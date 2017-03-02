
import os
from setuptools import setup, find_packages
import sys

sys.path.insert( 0, os.path.abspath( '.' ) )
import {{ cookiecutter.python_import_path }}

setup(
    name = {{ cookiecutter.python_import_path }}.__title__,
    version = {{ cookiecutter.python_import_path }}.__version__,
    description = {{ cookiecutter.python_import_path }}.__description__,
    author = {{ cookiecutter.python_import_path }}.__author__,
    author_email = {{ cookiecutter.python_import_path }}.__author_email__,
    license = {{ cookiecutter.python_import_path }}.__copyright__,
    packages = find_packages( exclude = [ 'sphinx', 'tests' ] ),
    namespace_packages = [ {{ cookiecutter.python_import_path }}.__namespace__ ]
)

