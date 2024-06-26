
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Topsis",
    version="1.0.0",
    author="Aryaman",
    author_email="aagarwal6_be21@thapar.com",
    description="Calculates Topsis Score and Rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/Aryaman1A/Assignment-1-Topsis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["Topsis_Aryaman_102116057"],
    include_package_data=True,
    install_requires='pandas',
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Aryaman_102116057.topsis:main",
        ]
    },
)
