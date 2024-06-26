import os
import sys
sys.path.insert(0, os.path.abspath('.')) # to import my own plugin

project = 'nxtbn'
copyright = '2024,bytenyx limited'
author = 'bytenyx limited'


version = ''

release = ''


extensions = [
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_copybutton',
    'sphinxext.opengraph',
    'sphinxcontrib.googleanalytics',
    'sphinx_sitemap',
    'sitemap_postprocess', # to remove .html extesion in sitemap
    'sphinxcontrib.redoc',
]

redoc = [
    {
        'name': 'nxtbn - Storefront API in redoc',
        'page': 'api/redoc/storefront',
        'spec': '_static/redoc/storefront.yml',
        'embed': True,
    },
    {
        'name': 'nxtbn - Dashboard API in redoc',
        'page': 'api/redoc/dashboard',
        'spec': '_static/redoc/dashboard.yml',
        'embed': True,
        # 'opts': {
        #     'lazy': False,
        #     'nowarnings': False,
        #     'nohostname': False,
        #     'required-props-first': True,
        #     'expand-responses': ["200", "201"],
        # }
    },
]

html_baseurl = 'https://docs.nxtbn.com' # 'sphinx_sitemap' specfic


html_extra_path = ['robots.txt']

html_favicon = '_static/favicon.ico'

googleanalytics_id = 'G-GGJRLNZ2DL'


ogp_site_url = "https://docs.nxtbn.com/"
ogp_site_name = "nxtbn | Next Billion Native Commerce - docs"

templates_path = ["_templates"]



source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


master_doc = 'index'


language = None


exclude_patterns = []


pygments_style = "sphinx"
pygments_dark_style = "monokai"


html_theme = "furo"




html_static_path = ['_static']


htmlhelp_basename = 'nxtbndoc'

html_theme_options = {
    "light_logo": "logo.png",
    "dark_logo": "darklogo.png",
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
    "top_of_page_buttons": ["view", "edit"],
    "announcement": "This project is not yet production-grade. Please wait for the final announcement.",
    "source_repository": "https://github.com/nxtbn-com/nxtbn-docs",
    "source_branch": "main",
    "source_directory": "source",
}

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'nxtbn.tex', 'nxtbn Documentation',
     'anamul \\& bytenyx limited team', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nxtbn', 'nxtbn Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'nxtbn', 'nxtbn Documentation',
     author, 'nxtbn', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------
