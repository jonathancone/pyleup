import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Pyleup",
    version = "0.1",
    author = "Jonathan Cone",
    author_email = "jonathan.t.cone@gmail.com",
    description = ("SVN log parser for Python"),
    license = "Apache 2",
    keywords = "SVN log parser",
    url = "https://github.com/jonathancone/pyleup",
    packages=['pyleup', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
)