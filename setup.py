import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="krispy-bot",
    version="0.1.0",
    author="HUSS4IN7",
    author_email="huss4in7@outlook.com",
    description="A Package to Automate Krispy Kreme Survey using Selenium.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=(url := "https://github.com/HUSS4IN7/krispy-bot"),
    project_urls={
        "Bug Tracker": f"{url}/issues",
    },
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.9",
        "Operating System:: OS Independent"
    ],
    install_requires=[
        'selenium==4.0.0.b4',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
