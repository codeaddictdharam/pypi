from setuptools import setup, find_packages
import os


VERSION = '0.0.1'
DESCRIPTION = 'Automatic EDA and Data Analysis'
LONG_DESCRIPTION = 'A package that allows to do Data Analysis and Basic EDA to some extent.'

# Setting up
setup(
    name="autodataanalysisandeda",
    version=VERSION,
    author="Sachin Mishra",
    author_email="<sachin19566@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'pandas profiling'],
    keywords=['python', 'pandas', 'numpy', 'autoeda', 'pandas profiling', 'EDA'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
