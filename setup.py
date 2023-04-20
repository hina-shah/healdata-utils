from setuptools import setup, find_namespace_packages

setup(
    name='healdata_utils',
    version='0.0.2',
    author='Michael Kranz',
    author_email='kranz-michael@norc.org',
    description='Data packaging tools for the HEAL data ecosystem',
    #TODO: change url to HEAL once migrated.
    url='https://github.com/norc-heal/healdata-utils/src/healdata-utils',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    install_requires=[
        'petl',
        'jsonschema',
        'requests',
        'pyyaml',
        'frictionless==4.40.8',
        'pyreadstat',
        #'dataforge[redcap] @ git+https://gitlab.com/mbkranz/data-forge.git@0afa429d6b7d1f1ec04ff8c4ee127291b3b058d4',
        #NOTE: temporarily taking out dataforge[redcap] as the xml transformations are WIP and to reduce external dependencies for POC
        'dataforge@ git+https://gitlab.com/mbkranz/data-forge.git@0afa429d6b7d1f1ec04ff8c4ee127291b3b058d4',
        'xmltodict', #NOTE:used until schemas put into dataforge,
        'charset_normalizer==2.1'
    ],
    entry_points='''
        [console_scripts]
        vlmd=healdata_utils.cli:main
    ''',

)
