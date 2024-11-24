import setuptools


setuptools.setup(
    name="akinator",
    version="0.25",
    license="MIT License",
    author="lanowde",
    packages=setuptools.find_packages(),
    install_requires=["idna", "httpx", "anyio", "sniffio", "h11"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
