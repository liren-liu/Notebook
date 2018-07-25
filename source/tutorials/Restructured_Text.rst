A ReStructuredText Primer
=========================

.. contents::


The text below contains links that look like "(quickref__)".  These
are relative links that point to the `Quick reStructuredText`_ user
reference.  If these links don't work, please refer to the `master
quick reference`_ document.

__
.. _Quick reStructuredText: quickref.html
.. _master quick reference:
   http://docutils.sourceforge.net/docs/user/rst/quickref.html

.. Note:: This document is an informal introduction to
   reStructuredText.  The `What Next?`_ section below has links to
   further resources, including a formal reference.


Structure
---------

From the outset, let me say that "Structured Text" is probably a bit
of a misnomer.  It's more like "Relaxed Text" that uses certain
consistent patterns.  These patterns are interpreted by a HTML
converter to produce "Very Structured Text" that can be used by a web
browser.

The most basic pattern recognised is a **paragraph** (quickref__).
That's a chunk of text that is separated by blank lines (one is
enough).  Paragraphs must have the same indentation -- that is, line
up at their left edge.  Paragraphs that start indented will result in
indented quote paragraphs. For example::

  This is a paragraph.  It's quite
  short.

     This paragraph will result in an indented block of
     text, typically used for quoting other text.

  This is another one.

Results in:

  This is a paragraph.  It's quite
  short.

     This paragraph will result in an indented block of
     text, typically used for quoting other text.

  This is another one.

__ quickref.html#paragraphs


Text styles
-----------

(quickref__)

__ quickref.html#inline-markup

Inside paragraphs and other bodies of text, you may additionally mark
text for *italics* with "``*italics*``" or **bold** with
"``**bold**``".  This is called "inline markup".

If you want something to appear as a fixed-space literal, use
"````double back-quotes````".  Note that no further fiddling is done
inside the double back-quotes -- so asterisks "``*``" etc. are left
alone.

If you find that you want to use one of the "special" characters in
text, it will generally be OK -- reStructuredText is pretty smart.
For example, this lone asterisk * is handled just fine, as is the
asterisk in this equation: 5*6=30.  If you actually
want text \*surrounded by asterisks* to **not** be italicised, then
you need to indicate that the asterisk is not special.  You do this by
placing a backslash just before it, like so "``\*``" (quickref__), or
by enclosing it in double back-quotes (inline literals), like this::

    ``*``

__ quickref.html#escaping

.. Tip:: Think of inline markup as a form of (parentheses) and use it
   the same way: immediately before and after the text being marked
   up.  Inline markup by itself (surrounded by whitespace) or in the
   middle of a word won't be recognized.  See the `markup spec`__ for
   full details.

__ ../../ref/rst/restructuredtext.html#inline-markup


Lists
-----

Lists of items come in three main flavours: **enumerated**,
**bulleted** and **definitions**.  In all list cases, you may have as
many paragraphs, sublists, etc. as you want, as long as the left-hand
side of the paragraph or whatever aligns with the first line of text
in the list item.

Lists must always start a new paragraph -- that is, they must appear
after a blank line.

**enumerated** lists (numbers, letters or roman numerals; quickref__)
  __ quickref.html#enumerated-lists

  Start a line off with a number or letter followed by a period ".",
  right bracket ")" or surrounded by brackets "( )" -- whatever you're
  comfortable with.  All of the following forms are recognised::

    1. numbers

    A. upper-case letters
       and it goes over many lines

       with two paragraphs and all!

    a. lower-case letters

       3. with a sub-list starting at a different number
       4. make sure the numbers are in the correct sequence though!

    I. upper-case roman numerals

    i. lower-case roman numerals

    (1) numbers again

    1) and again

  Results in (note: the different enumerated list styles are not
  always supported by every web browser, so you may not get the full
  effect here):

  1. numbers

  A. upper-case letters
     and it goes over many lines

     with two paragraphs and all!

  a. lower-case letters

     3. with a sub-list starting at a different number
     4. make sure the numbers are in the correct sequence though!

  I. upper-case roman numerals

  i. lower-case roman numerals

  (1) numbers again

  1) and again

**bulleted** lists (quickref__)
  __ quickref.html#bullet-lists

  Just like enumerated lists, start the line off with a bullet point
  character - either "-", "+" or "*"::

    * a bullet point using "*"

      - a sub-list using "-"

        + yet another sub-list

      - another item

  Results in:

  * a bullet point using "*"

    - a sub-list using "-"

      + yet another sub-list

    - another item

**definition** lists (quickref__)
  __ quickref.html#definition-lists

  Unlike the other two, the definition lists consist of a term, and
  the definition of that term.  The format of a definition list is::

    what
      Definition lists associate a term with a definition.

    *how*
      The term is a one-line phrase, and the definition is one or more
      paragraphs or body elements, indented relative to the term.
      Blank lines are not allowed between term and definition.

  Results in:

  what
    Definition lists associate a term with a definition.

  *how*
    The term is a one-line phrase, and the definition is one or more
    paragraphs or body elements, indented relative to the term.
    Blank lines are not allowed between term and definition.


Preformatting (code samples)
----------------------------
(quickref__)

__ quickref.html#literal-blocks

To just include a chunk of preformatted, never-to-be-fiddled-with
text, finish the prior paragraph with "``::``".  The preformatted
block is finished when the text falls back to the same indentation
level as a paragraph prior to the preformatted block.  For example::

  An example::

      Whitespace, newlines, blank lines, and all kinds of markup
        (like *this* or \this) is preserved by literal blocks.
    Lookie here, I've dropped an indentation level
    (but not far enough)

  no more example

Results in:

  An example::

      Whitespace, newlines, blank lines, and all kinds of markup
        (like *this* or \this) is preserved by literal blocks.
    Lookie here, I've dropped an indentation level
    (but not far enough)

  no more example

Note that if a paragraph consists only of "``::``", then it's removed
from the output::

  ::

      This is preformatted text, and the
      last "::" paragraph is removed

Results in:

::

    This is preformatted text, and the
    last "::" paragraph is removed


:Author: Richard Jones
