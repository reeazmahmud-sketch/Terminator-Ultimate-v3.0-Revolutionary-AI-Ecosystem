from setuptools import setup, find_packages

setup(
    name="terminator-ai",
    version="3.0.0-ultimate",
    description="Revolutionary AI ecosystem with sentient consciousness",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Terminator Development Team",
    author_email="dev@terminator.ai",
    url="https://github.com/reeazmahmud/Terminator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "psutil>=5.8.0",
        "requests>=2.25.0",
        "aiohttp>=3.8.0",
        "cryptography>=3.4.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0.0", "black>=22.0.0", "mypy>=0.991"],
        "monitoring": ["prometheus-client>=0.12.0", "structlog>=21.1.0"],
    },
    entry_points={
        "console_scripts": [
            "terminator=terminator.cli.main:main",
            "terminator-sentient=terminator.core.consciousness:main",
            "terminator-discovery=terminator.core.discovery:main",
            "terminator-adapter=terminator.core.adapter:main",
            "terminator-ultimate=terminator.systems.ultimate:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
