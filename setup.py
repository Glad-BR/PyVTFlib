from setuptools import setup, Extension
import subprocess
import os

from pathlib import Path

# Build C++ app before Python package
def build_cpp():
    cpp_dir = (Path(__file__).parent  / "cpp" / "MareTF")
    # Run CMake, make, etc.
    subprocess.run(["cmake", ".", "-B", "build"], cwd=cpp_dir, check=True)
    subprocess.run(["cmake", "--build", "build"], cwd=cpp_dir, check=True)

setup(
    name="mywrapper",
    version="0.1.0",
    package_dir={"": "src"},
    packages=["mywrapper"],
    # ... other setup args
)