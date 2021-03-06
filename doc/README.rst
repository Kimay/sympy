How to Build Documentation
==========================

To make the html documentation, install the prerequisites, e.g. on
Debian/Ubuntu (similarly for other distributions)::

    apt-get install python-sphinx texlive-latex-recommended dvipng

and do::

    make html

and to view it, do::

    epiphany _build/html/index.html

How to Build Translated Tutorial
================================

To build the translated tutorial, build the documentation
using ``make html`` and then just run::

    make htmli18n

This will create ``tutorial.cs.html``, ``tutorial.ru.html`` (and so on for all
languages) in the ``_build/html/`` directory. The input is the English tutorial
``tutorial.txt`` and the .po files ``tutorial.cs.po``, ``tutorial.ru.po``, etc.
You can freely change the English tutorial -- sentences that are not translated
will remain in English in the translated verions.

Note: ``make htmli18n`` is currently quite slow, so it is not run by default.
However, this can be trivially implemented by modifying the ``Makefile``.

How to Update Translations
==========================

In order to update translations, you first need to generate the
``tutorial.pot`` template by::

    make gettext

Then you need to translate it (or update the translation) into
``tutorial.cs.po``, etc. You can use gettext utilities to merge the
translations if needed. Then just build it using ``make htmli18n`` (see the
previous section).
