from setuptools import setup, find_packages

setup(
	name='tmail-py',
	version='0.1.0',
	description='Python wrapper for TMail API',
	packages=find_packages(exclude=("tests",)),
	install_requires=[
		'requests>=2.28'
	],
	include_package_data=True,
	entry_points={
		'console_scripts': [
			'tmail-cli=tmail_api.cli:main'
		]
	},
)
