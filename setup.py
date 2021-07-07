import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="krispy",
    version="0.1.0",
    author="HUSS4IN7",
    author_email="huss4in7@outlook.com",
    description="A package that completes Krispy Kreme Survey and retrieves the code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HUSS4IN7/krispy-bot",
    project_urls={
        "Bug Tracker": "https://github.com/HUSS4IN7/krispy-bot/issues",
    },
    classifiers=[
        "Programming Language:: Python:: 3.9+",
        "License:: OSI Approved:: MIT License",
        "Operating System:: OS Independent"
        "Framework:: selenium",
    ],
    install_requires=[
        'selenium==4.0.0.b4',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)
