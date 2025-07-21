from setuptools import setup, find_packages

setup(
    name="ai-career-assistant",
    version="0.0.8",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",  # or whatever dependencies you have
        "requests",
    ],
    python_requires=">=3.8",
)