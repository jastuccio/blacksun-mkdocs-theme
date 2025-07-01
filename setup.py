from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="blacksun-mkdocs-theme",
    version="0.1.0",  # It's simpler to manage the version here for now
    author='jastuccio',
    author_email='joe@astucc.io',
    url='https://github.com/jastuccio/blacksun-mkdocs-theme',
    description="A dark, Dracula-inspired theme for MkDocs, named Black Sun.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'mkdocs>=1.4.3'
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=False,
    entry_points={
        'mkdocs.themes': [
            'blacksun = mkdocs_blacksun_theme',
        ]
    },
)
