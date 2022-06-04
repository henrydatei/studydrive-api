import setuptools
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setuptools.setup(
    name = "studydrive",                     # This is the name of the package
    version = "0.1.1",                        # The initial release version
    author = "Henry Haustein",                     # Full name of the author
    description = "A Python Wrapper for the (unofficial) Studydrive API",
    packages = setuptools.find_packages(),    # List of all python modules to be installed
    python_requires = '>=3.6',                # Minimum version requirement of the package
    install_requires=["requests", "datetime"],
    url = "https://github.com/henrydatei/studydrive-api",
    long_description=README,
    long_description_content_type="text/markdown",
)