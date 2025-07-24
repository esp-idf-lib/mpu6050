# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess

subprocess.call('%s build-doxygen' % os.getenv("MAKE"), shell=True)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = os.getenv("PROJECT_NAME")
copyright = os.getenv("PROJECT_COPYRIGHT")
author = os.getenv("PROJECT_AUTHORS")
release = os.getenv("PROJECT_RELEASE")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.autosectionlabel',
        'sphinx.ext.todo',
        'sphinx.ext.coverage',
        'sphinx.ext.viewcode',
        'breathe',
        'sphinx_rtd_theme'
        ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
highlight_language = "c"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
#html_static_path = ['_static']
breathe_projects = {os.getenv("PROJECT_NAME"): '_docs/xml/'}
breathe_default_project = os.getenv("PROJECT_NAME")
breathe_default_members = ('members', 'undoc-members')
