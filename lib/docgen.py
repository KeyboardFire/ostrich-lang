#!/usr/bin/python3

import ost_instructions
from textwrap import dedent
import datetime

OUTFILE = '../doc/builtin.md'

instr = ost_instructions.ost_instructions()
keys = sorted(ost_instructions.ost_instructions().keys())

with open(OUTFILE, 'w') as f:

    print(dedent('''
    # Ostrich builtins

    Here is a list of all Ostrich instructions and what they do. They are
    arranged in ASCIIbetical order (the same order as in the source code).

    *doc last autogenerated on %s*
    ''' % datetime.datetime.today().strftime('%c')), file=f)

    for k in keys:
        # special-cases
        if k == '\n': continue  # \n and <space> are the same thing in the docs
        if k in '0123456789': continue  # don't need to doc numbers, obviously

        doc = dedent(instr[k].__doc__ or 'TODO').strip()

        # formatting special cases
        if k == ' ': k = '\\n`, ` '
        if k == '`': k = '` ` `'

        print('## `%s`\n\n%s\n' % (k, doc), file=f)
