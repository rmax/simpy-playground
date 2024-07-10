# Load version from auto-generated _version.py or else from installed package
# metadata, if available.
try:
    from simpy_playground._version import __version__
except ImportError:
    from importlib.metadata import PackageNotFoundError, version

    try:
        __version__ = version("simpy_playground")
    except PackageNotFoundError:
        __version__ = "0.0.0"
