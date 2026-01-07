from setuptools import setup, find_packages

setup(
	name='tmailpy',
	version='0.0.2.1',
	description='Python wrapper for TMail API',
	packages=find_packages(exclude=("tests",)),
	install_requires=[
		'requests>=2.28'
	],
	include_package_data=True,
    url='https://github.com/nxyyhaha/tmail-wrapper',
	entry_points={
		'console_scripts': [
			'tmail-cli=tmailpy.cli:main'
		]
	},
)
