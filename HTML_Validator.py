#!/bin/python3

import re


def validate_html(html):
    '''
    This function performs a limited version of html validation
    by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    if len(html) == 0:
        return True
    html_tags = _extract_tags(html)
    if len(html_tags) == 0:
        return False
    if len(html_tags) % 2 != 0:
        return False
    stack = []
    for tag in html_tags:
        if "/" not in tag:
            stack.append(tag)
        else:
            if len(stack) == 0:
                # check for closing tag
                return False
            else:
                if _match(tag, stack[-1]):
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False


def _match(tag_one, tag_two):
    '''
    This functions checks if an opening and closing html match.

    >>> _match('<strong>', '</strong>')
    True
    >>> _match('<strong>', '</b>')
    False
    '''
    tag_one = re.findall(r'\w+', tag_one)
    tag_two = re.findall(r'\w+', tag_two)
    return tag_one == tag_two


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    >>> _extract_tags('<a href="www.something">link this</a>')
    ['<a>', '</a>']
    '''
    tags = re.findall(r'<.*?>', html)
    t_no_atrb = []  # creates a list of tags without the attributes
    for tag in tags:
        if re.match(r'^</', tag) is None:
            tm = re.match(r'^<\w+', tag)
            tag = tm.group(0) + ">"
        t_no_atrb.append(tag)
    return t_no_atrb
