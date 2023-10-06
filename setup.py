# MLU (McLevey Lab Utilities)
from setuptools import setup, find_packages

setup(
	name='mlu', 
	version="0.0.1",
	packages=find_packages(),
	install_requires=[
		'pandas'
	],
	author='John McLevey, University of Waterloo',
	description='A collection of utility functions for various computational social science research projects.',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown'
)