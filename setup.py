import platform
import sys

from Cython.Build import cythonize
from setuptools import Extension, setup

EXT_SOURCES = [
    "MetroHash/src/metrohash64.cpp",
    "MetroHash/src/metrohash128.cpp",
]

INT_SOURCES = ["metrohash.pyx"]

if sys.platform == "win32":
    cflags = ["/O2", "/arch:AVX2"]
else:
    if platform.machine().lower() in ("x86_64", "amd64"):
        cflags = ["-O3", "-msse4.2"]
    else:
        cflags = ["-O3", "-march=native"]

extensions = [
    Extension(
        "metrohash",
        sources=EXT_SOURCES + INT_SOURCES,
        extra_compile_args=cflags,
        include_dirs=["MetroHash/src"],
        language="c++",
    )
]

with open("README.md", encoding="utf-8") as fr:
    long_description = fr.read()

setup(
    author="Dobatymo",
    name="metrohash-python",
    version="1.1.3.3",
    url="https://github.com/Dobatymo/metrohash-python",
    description="Python bindings for MetroHash",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: C++",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
    ],
    ext_modules=cythonize(extensions),
    python_requires=">=3.6",
    use_2to3=False,
    zip_safe=False,
)
