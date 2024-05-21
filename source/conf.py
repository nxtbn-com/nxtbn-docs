project = 'nxtbn'
copyright = '2024,bytenyx limited'
author = 'bytenyx limited'


version = ''

release = ''


extensions = [
    'sphinx.ext.viewcode',
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_sitemap'
]

html_baseurl = 'https://docs.nxtbn.com' # 'sphinx_sitemap' specfic


templates_path = ["_templates"]



source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}


master_doc = 'index'


language = 'en'


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
    "announcement": "We will launch the stable version on July 1st, 2024. We are seeking your feedback",
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
