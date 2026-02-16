import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MonetizationFramework",
    version="1.0.0",
    author="AI Architect",
    description="A dynamic AI-driven monetization framework for market adaptation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evolution-ai/monetization-framework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "logging==0.11.0",
        "numpy==1.24.3",
        "torch==2.0.0",
        "transformers==4.25.1",
        "knowledge-base-connector>=1.0.0",
        "risk-assessment-module>=1.0.0",
        "market-data-feeder>=1.0.0"
    ],
)