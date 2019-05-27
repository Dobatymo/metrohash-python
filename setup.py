import sys
from io import open
from setuptools import setup, Extension

try:
	from Cython.Build import cythonize
	USE_CYTHON = True
except ImportError:
	USE_CYTHON = False

EXT_SOURCES = [
	"MetroHash/src/metrohash64.cpp",
	"MetroHash/src/metrohash128.cpp",
]

if USE_CYTHON:
	INT_SOURCES = [
		"metrohash.pyx"
	]
else:
	INT_SOURCES = [
		"metrohash.cpp"
	]

if sys.platform == "win32":
	cflags = []
else:
	cflags = ["-msse4.2"]

extensions = [Extension(
	"metrohash",
	sources=EXT_SOURCES + INT_SOURCES,
	extra_compile_args=cflags,
	include_dirs=["MetroHash/src"],
	language="c++"
)]

if USE_CYTHON:
	extensions = cythonize(extensions)

with open("README.md", "r", encoding="utf-8") as fr:
	long_description = fr.read()

setup(
	author="Dobatymo",
	name="metrohash-python",
	version="1.1.3.post1",
	url="https://github.com/Dobatymo/metrohash-python",
	ext_modules=extensions,
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
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
		"Topic :: Internet",
		"Topic :: Scientific/Engineering",
		"Topic :: Utilities"
	]
)
