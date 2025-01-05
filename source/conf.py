# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Urbanalize'
copyright = '2025, Filippo Bissi'
author = 'Filippo Bissi'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Tema Read the Docs
html_static_path = ['_static']

# Adding the path to the Library folder
import os
import sys
sys.path.insert(0, os.path.abspath(r'../../Library/urbanalize.py'))  # Percorso relativo alla cartella "Library"
