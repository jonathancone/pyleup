import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Pyleup",
    version = "0.1",
    author = "Jonathan Cone",
    author_email = "jonathan.t.cone@gmail.com",
    description = ("Subversion (SVN) revision statistics library written in Python"),
    license = "Apache Software License",
    keywords = "Subversion SVN statistics",
    url = "https://github.com/jonathancone/pyleup",
    packages=['pyleup', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Version Control"
    ],    
)