from importlib import metadata

try:
    # This will read the version from the installed package's metadata
    __version__ = metadata.version("blacksun-mkdocs-theme")
except metadata.PackageNotFoundError:
    # This is a fallback for when the package is not installed, e.g., during development
    __version__ = "0.0.0"

# The author and license information is managed in setup.py and the LICENSE file.
# There is no need to duplicate it here.
