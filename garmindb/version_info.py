"""Version information for the application."""

__author__ = "Tom Goetz"
__copyright__ = "Copyright Tom Goetz"
__license__ = "GPL"


python_required = (3, 0, 0)
python_tested = (3, 11, 4)
version_info = (3, 5, 1)
prerelease = False


def version_string():
    """Return a version string for a version tuple."""
    return '.'.join(str(digit) for digit in version_info)
