
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
os.environ['PATH'] += ":."
if 'PYTHONPATH' in os.environ:
    os.environ['PYTHONPATH'] += (":" + os.path.abspath('..'))
else:
    os.environ['PYTHONPATH'] = os.path.abspath('..')
# -- Project information -----------------------------------------------------

project = 'snakeobjects'
copyright = '2020, Ivan Iossifov, Boris Yamrom'
author = 'Ivan Iossifov, Boris Yamrom'

# The full version, including alpha/beta/rc tags
release = '1.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autodoc', 'sphinx_autorun' ]
autodoc_mock_imports = ["yaml", "re"]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False 


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def createTgz(dname):
    cmd = "for d in `find "+dname+" -name __pycache__`; do rm -r $d; done"
    os.system(cmd)
    cmd = "for d in `find "+dname+" -name objects`; do rm -r $d; done"
    os.system(cmd)
    cmd = "tar czf "+dname+".tgz "+dname
    os.system(cmd)
    
createTgz('helloWorld')
createTgz('snakeobjectsTutorial')
createTgz('snakeobjectsPaperExample')
createTgz('snakemakeTutorialExample')
