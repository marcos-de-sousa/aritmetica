from setuptools import setup

setup(
    name='aritmetica',
    version='0.1',
    packages=['aritmetica'],
    url='https://github.com/marcos-de-sousa',
    license='MIT License',
    author='Marcos Paulo Alves de Sousa',
    author_email='msousa@museu-goeldi.br',
    description='Pacote python para operações aritméticas'
)

from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='aritmetica',
    version='0.0.1',
    url='https://github.com/marcos-de-sousa/aritmetica',
    license='MIT License',
    author='Marcos Paulo Alves de Sousa',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='desousa.mpa@gmail.com',
    keywords='Pacote',
    description=u'Exemplo de pacote PyPI',
    packages=['aritmetica'],
    install_requires=['python3.6'],)
