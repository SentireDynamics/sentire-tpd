#!/usr/bin/env python3
"""
Setup configuration for TPD - Théorie Polyvagale Digitale
=========================================================

Package de distribution pour l'architecture neuro-inspirée TPD.
Permet l'installation et la distribution du framework de résilience.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Lecture du README pour la description longue
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Lecture de la version depuis le module principal
version = {}
with open("tpd/__init__.py") as fp:
    exec(fp.read(), version)

setup(
    name="sentire-tpd",
    version=version.get("__version__", "0.1.0"),
    author="Sentire Dynamics",
    author_email="contact@sentiredynamics.org",
    description="Architecture neuro-inspirée pour la résilience des systèmes complexes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SentireDynamics/sentire-tpd",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: French",
    ],
    keywords="resilience polyvagal architecture neuroscience systems sovereignty",
    python_requires=">=3.8",
    install_requires=[
        # Aucune dépendance externe - principe de souveraineté
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.950",
        ],
        "demo": [
            "matplotlib>=3.5",
            "numpy>=1.20",
        ],
        "documentation": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tpd-demo=demo_tpd:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/SentireDynamics/sentire-tpd/issues",
        "Source": "https://github.com/SentireDynamics/sentire-tpd",
        "Documentation": "https://sentire-tpd.readthedocs.io/",
        "Funding": "https://github.com/sponsors/SentireDynamics",
    },
    include_package_data=True,
    zip_safe=False,
    
    # Métadonnées TPD spécifiques
    **{
        "doctrine": "TPD - Théorie Polyvagale Digitale",
        "architecture": "Guardian/Predator",
        "paradigme": "Résilience Neuro-Inspirée",
        "tripartition": "VENTRAL/SYMPATHETIC/DORSAL",
        "souverainete": "Numérique",
    }
)