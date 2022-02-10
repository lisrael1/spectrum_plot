import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spectrum_plot",
    version="0.1.0",
    author="Lior Israeli",
    author_email="israelilior@gmail.com",
    description="Interactive spectrum plot. Update FFT plot on every new sampled data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lisrael1/spectrum_plot",
    project_urls={
        "Bug Tracker": "https://github.com/lisrael1/spectrum_plot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=[
          'matplotlib', 'freq_note_converter',
    ],
    packages=setuptools.find_packages(where="src", exclude=['*_tests', '*_examples'],),
    python_requires=">=3.6",
)
