from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

VERSION = '1.0.0'
DESCRIPTION = 'CLI tool to know the amount of disk space PyPi packages are occupying.'

setup(
    name="pypidisk",
    version=VERSION,
    author="Karishma Shukla",
    author_email="karishmashuklaa@gmail.com",
    url="https://github.com/karishmashuklaa/pypidisk",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= readme(),
    packages=find_packages(),
    keywords=['diskspace', 'dependencies', 'pypi', 'cli', 'pydisk', 'memory', 'modules', 'packages'],
    entry_points={
        'console_scripts': [
            'pypidisk=pypidisk.__init__.py:get_package_size',
        ]
    },
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)