from setuptools import setup

__version__ = '0.1.0.0'
setup(
    name='drremote',
    version=__version__,
    packages=['drremote'],
    url='',
    license='MIT',
    author='Dieter Stockhausen',
    author_email='dieter@schwingenhausen.at',
    description='',
    entry_points={
        "console_scripts": [
            'drremote = drremote:run_main'
        ]
    }
)
