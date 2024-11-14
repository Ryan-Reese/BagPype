import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bagpype", # Replace with your own username
    version="1.0",
    author="Ben Amor, Francesca Vianello, Florian Song",
    author_email="florian.song@gmail.com",
    description="Biomolecular, atomistic graph construction software in Python for proteins, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://floriansong.github.io/BagPype/",
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    install_requires=(
        'numpy',
        'scipy',
        'networkx',
        'pandas',
        'PyCifRW',
        'requests'
    ),
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"bagpype": ["dependencies/*", "dependencies/mmcif/*"]},
    include_package_data=True,
    exclude_package_data={"bagpype": ["AUX.cif"]},
    python_requires=">=3.6",
)
