import setuptools

# this is only necessary when not using setuptools/distribute
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}


with open("README.md", "r") as fh:
    long_description = fh.read()

name = 'homework'
version = '0.3'

setuptools.setup(
    name=name,
    version=version,
    author="Martin Váňa",
    author_email="vana1martin@gmail.com",
    description="An example pip package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vanam/example_pip_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'Sphinx',
    ],
    cmdclass=cmdclass,
    # these are optional and override conf.py settings
    command_options={
        'build_sphinx': {
            'project': ('setup.py', name),
            'version': ('setup.py', version)
        }
    },
)
