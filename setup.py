from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

VERSION = '1.0.3'
DESCRIPTION = 'CLI tool to know the amount of disk space PyPi packages are occupying.'

setup(
    name="pydisk",
    version=VERSION,
    author="Karishma Shukla",
    author_email="karishmashuklaa@gmail.com",
    url="https://github.com/karishmashuklaa/pydisk",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= readme(),
    py_modules=["pydisk/pkgsize"],
    keywords=['diskspace', 'dependencies', 'pypi', 'cli', 'pydisk', 'memory', 'modules', 'packages'],
    entry_points={
        'console_scripts': [
            'pydisk=pkgsize:get_package_size',
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