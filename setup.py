import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='homework',
    version='0.1',
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
    ],
)
