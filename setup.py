from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='',
    version='0.1.01',
    author='Fred Pires',
    author_email='fredapires@gmail.com',
    description='',
    long_description='file: README.md',
    long_description_content_type="text/markdown",
    url='https://github.com/fredapires/',
    packages=find_packages(),
    install_requires=[
        'build',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'missingno',
        'pandas-profiling',
        'ydata-profiling',
        'dataprep',
        'jupyter-helpers',
        'win10toast',
        'jaro_winkler',
        'openpyxl',
        'pyarrow',
        'pyodbc',
        'pyautogui',
        'faker',
        'pytest'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
