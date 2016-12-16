
from setuptools import setup

setup(
    name = '{{ cookiecutter.debian_package_name }}',
    version = '0.0.1',
    description = '{{ cookiecutter.debian_package_short_description }}',
    author = 'GetWellNetwork',
    author_email = 'plc-dev@getwellnetwork.com',
    license = 'Copyright 2016 GetWellNetwork, Inc., BSD copyright and disclaimer apply',
    packages = [ 'gwn', 'gwn.{{ cookiecutter.python_subpackage_name }}' ],
    namespace_packages = [ 'gwn' ],
    entry_points = {
        'console_scripts': [
            '{{ cookiecutter.service_executable }} = {{ cookiecutter.python_import_path }}.cli:main'
        ]
    }
)
