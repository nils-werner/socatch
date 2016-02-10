import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name='socatch',
        version='0.1',
        description='Automatically open exceptions on StackOverflow',
        author='Nils Werner',
        author_email='nils.werner@gmail.com',
        url='https://github.com/nils-werner/socatch',
        license='MIT',
        py_modules=['socatch'],
        extras_require={
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'pytest-mock',
                'tox',
            ],
        },
        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'pytest-mock',
            'tox',
        ],
    )
