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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
import re
import os
import sys

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.abspath("extensions"))

on_rtd = os.environ.get("READTHEDOCS") == "True"
project = "Wavelink"
copyright = "2023, PythonistaGuild, EvieePy"
author = "PythonistaGuild, EvieePy"

# The full version, including alpha/beta/rc tags
release = ''
with open('../wavelink/__init__.py') as f:
    release = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

version = release
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.napoleon",
    "sphinxcontrib.asyncio",
    "sphinx.ext.intersphinx",
    "attributetable",
    "sphinxext.opengraph"
]

# OpenGraph Meta Tags
ogp_image = "https://raw.githubusercontent.com/PythonistaGuild/Wavelink/master/logo.png"
ogp_description = "Documentation for Wavelink, the Powerful Lavalink wrapper for discord.py."
ogp_site_url = "https://wavelink.dev/"
ogp_custom_meta_tags = [
    '<meta property="og:description" content="A robust and powerful Lavalink wrapper for Discord.py. Wavelink features a fully asynchronous API that\'s intuitive and easy to use with built in Spotify Support and Node Pool Balancing." />',
    '<meta property="og:title" content="Wavelink Documentation" />'
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# html_logo = "logo.png"

html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo.png",
    "dark_logo": "wl_dark.png"
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# These folders are copied to the documentation's HTML output
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ["styles/furo.css"]
html_js_files = ["js/custom.js"]

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
autodoc_member_order = "groupwise"

rst_prolog = """
.. |coro| replace:: This function is a |corourl|_.
.. |maybecoro| replace:: This function *could be a* |corourl|_.
.. |corourl| replace:: *coroutine*
.. _corourl: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. |deco| replace:: This function is a **decorator**.
"""

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "dpy": ("https://discordpy.readthedocs.io/en/stable/", None)
}

extlinks = {
    'wlissue': ('https://github.com/PythonistaGuild/Wavelink/issues/%s', 'GH-%s'),
    'ddocs': ('https://discord.com/developers/docs/%s', None),
}

pygments_style = "sphinx"
pygments_dark_style = "monokai"