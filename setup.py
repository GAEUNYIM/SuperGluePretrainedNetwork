from setuptools import setup, find_packages

with open('requirements.txt') as f:
requirements = f.read().splitlines()

with open("README.md", "r") as fh:
long_description = fh.read()

setuptools.setup(
name="supergluepretrainednetwork", 
version="0.0.1",

packages=setuptools.find_packages(),

python_requires='>=3.6',
install_requires=requirements,
)
