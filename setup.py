from setuptools import setup, find_packages

setup(
    name='podcasts',
    version='0.0.1',
    url='https://github.com/dalepotter/podcasts',
    author='Dale Potter',
    author_email='dalepotter@gmail.com',
    description='Unofficial podcass RSS feeds for a selection of audio content found online.',
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4==4.10.0",
        "podgen==1.1.0",
        "requests==2.27.1"
    ]
)
