#!/usr/bin/env python
# encoding: utf-8

### IMPORTS ###

import locale
from docutils.core import publish_cmdline, default_description
from docutils.writers.latex2e import Writer as Latex2eWriter
from docutils.writers.latex2e import LaTeXTranslator, DocumentClass

## CONSTANTS & DEFINES: ###

BEAMER_DEFAULTS = {
    #'use_latex_toc': True,
    #'output_encoding': 'latin-1',
    'documentclass': 'article',
    'documentoptions': '12pt,a4paper',  # text is at the top of each slide rather than centered.  Changing to 'c' centers the text on each slide (vertically)
    #'sectnum_depth': 0,
}


### IMPLEMENTATION ###

try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass


class ThesisTranslator (LaTeXTranslator):
    """
    A converter for docutils elements to beamer-flavoured latex.
    """

    def __init__(self, document):
        LaTeXTranslator.__init__(self, document)
        self.head_prefix.extend(["\\usepackage{lineno}\n", "\\linenumbers"])
        print self.head_prefix
        self.d_class = DocumentClass('article')


class ThesisWriter (Latex2eWriter):
    """
    A docutils writer that modifies the translator and settings for beamer.
    """
    #settings_spec = BEAMER_SPEC
    settings_defaults = BEAMER_DEFAULTS

    def __init__(self):
        Latex2eWriter.__init__(self)
        self.translator_class = ThesisTranslator


if __name__ == '__main__':
    description = (
        "Generates Beamer-flavoured LaTeX for PDF-based presentations." + default_description)
    publish_cmdline(writer=ThesisWriter(), description=description)


### END ######################################################################
