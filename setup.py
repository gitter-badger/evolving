
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evolving",
    version="0.1.3",
    author="Lorenzo",
    author_email="zetatez@icloud.com",
    description="trading api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zetatez/darwin',
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
    "Programming Language :: Python :: 3.8",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)