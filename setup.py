"""
* Install with pip (recommended):
    pip3 install .
* Install with setuptools:
    python3 setup.py install
* Run tests:
    python3 setup.py pytest
"""
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pywebdoc',
    version='0.0.1',
    description="""
    CLI application to quickly open web documentation about Python""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Quentin Deschamps',
    author_email='quentindeschamps18@gmail.com',
    url='https://github.com/Quentin18/pywebdoc',
    packages=['pywebdoc'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation'
    ],
    license='MIT',
    keywords='documentation cli click url pypi',
    project_urls={
        'Documentation':
        'https://pywebdoc.readthedocs.io/en/latest/',
        'Travis':
        'https://travis-ci.org/github/Quentin18/pywebdoc/',
        'Source Code': 'https://github.com/Quentin18/pywebdoc/',
    },
    platforms=['any'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['click', 'jinja2', 'colorlog', 'tqdm', 'requests'],
    entry_points='''
        [console_scripts]
        pywebdoc=pywebdoc.cli:cli
    ''',
    python_requires='>=3',
    setup_requires=['pytest-runner'],
    tests_require='pytest'
)
