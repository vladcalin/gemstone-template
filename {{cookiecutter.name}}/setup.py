from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.name}}",
    version="{{cookiecutter.version}}",

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        "gemstone"
    ],

    entry_points={
        "console_scripts": [
            "{{cookiecutter.name}} = {{cookiecutter.name}}.service:start_service"
        ]
    }
)
