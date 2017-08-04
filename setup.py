from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='genutil',
    version='0.0.1',
    description='A collection of convenient utility functions/objects',
    long_description=readme,
    author='Zhe Feng',
    author_email='zhe.feng0018@gmail.com',
    url='https://github.com/zf109/genutils',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
