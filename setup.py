from setuptools import setup, find_namespace_packages
from pathlib import Path

def generate_long_description():
    return Path("README.md").read_text()

def get_install_requirements():
    return Path("requirements.txt").read_text()


setup(
    name='healdata_utils',
    version='0.1.1-alpha',
    author='Michael Kranz',
    author_email='kranz-michael@norc.org',
    long_description=generate_long_description(),
    long_description_content_type="text/markdown",    
    description='Data packaging tools for the HEAL data ecosystem',
    #TODO: change url to HEAL once migrated.
    url='https://github.com/norc-heal/healdata-utils',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    install_requires=get_install_requirements(),
    entry_points='''
        [console_scripts]
        vlmd=healdata_utils.cli:main
    '''

)
