# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Urbanalize'
copyright = '2025, Filippo Bissi'
author = 'Filippo Bissi'
release = '1.0.0.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
sys.path.insert(0, os.path.abspath(r'C:\Users\andre\OneDrive\Documenti\Filippo\Università\24_Corsi\061938_Geospatial_processing\Project\Library\urbanalize.py'))  # Path alla tua libreria

# Tema Read the Docs
html_theme = 'sphinx_rtd_theme'
