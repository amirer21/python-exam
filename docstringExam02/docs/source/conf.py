# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
#sys.path.insert(0, os.path.abspath('../path/to/your/python/file'))
#docstring으로 작성할 코드의 절대 경로 D:\python_workspace\python-exam\docstringExam02\test_code
sys.path.insert(0, os.path.abspath('D:/python_workspace/python-exam/docstringExam02'))

project = 'doc_exam'
copyright = '2023, amirer'
author = 'amirer'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = []
extensions = [
    'sphinx.ext.autodoc',
    # ... other extensions
]

templates_path = ['_templates']
#exclude_patterns = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
