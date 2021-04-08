#!/usr/bin/env python3

# MIT License
#
# Copyright (c) 2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

# Li[dot]py : Python3 implementation of Scrift's list-directory command.
#
# github.com/ferhatgec/scrift
# ===========================
# github.com/ferhatgec/lirs

from os import path, listdir, getcwd
from pathlib import Path
from re import search

class Lipy:
    def __init__(self):
        self.directory = getcwd()
        self.file = ''

        self.everything = []

    def between(self, data: str, substring: str, substring2: str) -> str:
        return search(substring + '(.*)' + substring2, data).group(1)

    def get(self, extension: str) -> tuple:
        extension = extension[1:]

        for data in self.everything:
            if extension == data[1]:
                return (data[0], data[2])

        return ('[File]:      ', 34)

    def parse(self, data: str):
        color = int(self.between(data, '\>\{', '\}\<'))

        if color == 0:
            color = 34

        name = self.between(data, '\>\'', '\'<')
        extension = self.between(data, '\>\"', '\"<')

        self.everything.append((name, extension, color))

    def read_data(self):
        if path.exists(str(Path.home()) + '/' + '.lirs_data'):
            file_data = open(str(Path.home()) + '/' + '.lirs_data')

            for line in file_data.readlines():
                self.parse(line)
        else:
            open(str(Path.home()) + '/' + '.lirs_data', "x")
            self.read_data()

    def printf(self, color, data):
        print(color, data, '\033[1;97m', self.file, sep='', end='\n')

    def match(self, arg):
        if path.isdir(arg):
            self.printf('\033[1;94m', '[Direc]:     ')
            return

        arg = path.splitext(arg)[1]

        if arg == '.scrift_log': self.printf('\033[1;33m',       'FeLog*:      ')
        elif arg == '.scrift_ascii': self.printf('\033[1;33m',   'Ascii Art*:  ')
        elif arg == '.scrift_settings': self.printf('\033[1;33m','Settings*:   ')
        elif arg == '.scrift_history': self.printf('\033[1;33m', 'History*:    ')
        elif arg == '.scr': self.printf('\033[1;32m',            '[Scrift]:    ')
        elif arg == '.cpp': self.printf('\033[1;36m',            '[C++]:       ')
        elif arg == '.hpp': self.printf('\033[1;36m',            '[C++]:       ')
        elif arg == '.cxx': self.printf('\033[1;36m',            '[C++]:       ')
        elif arg == '.hxx': self.printf('\033[1;36m',            '[C++]:       ')
        elif arg == '.cc': self.printf('\033[1;36m',             '[C++]:       ')
        elif arg == '.hh': self.printf('\033[1;36m',             '[C++]:       ')
        elif arg == '.c': self.printf('\033[1;34m',              '[C]:         ')
        elif arg == '.h': self.printf('\033[1;34m',              '[C]:         ')
        elif arg == '.sh': self.printf('\033[1;32m',             '[Bash]:      ')
        elif arg == '.bash': self.printf('\033[1;32m',           '[Bash]:      ')
        elif arg == '.py': self.printf('\033[1;34m',             '[Python]:    ')
        elif arg == '.pyc': self.printf('\033[1;34m',            '[Python]:    ')
        elif arg == '.fls': self.printf('\033[1;33m',            '[FlaScript]: ')
        elif arg == '.flsh': self.printf('\033[1;33m',           '[FlaScript]: ')
        elif arg == '.md': self.printf('\033[1;33m',             '[Markdown]:  ')
        elif arg == '.freebr': self.printf('\033[1;35m',         '[FreeBr]:    ')
        elif arg == '.png': self.printf('\033[1;34m',            '[Png]:       ')
        elif arg == '.jpg': self.printf('\033[1;34m',            '[Jpg]:       ')
        elif arg == '.jpeg': self.printf('\033[1;34m',           '[Jpg]:       ')
        elif arg == '.gif': self.printf('\033[1;34m',            '[Gif]:       ')
        elif arg == '.htm': self.printf('\033[1;35m',            '[Html]:      ')
        elif arg == '.html': self.printf('\033[1;35m',           '[Html]:      ')
        elif arg == '.rs': self.printf('\033[1;33m',             '[Rust]:      ')
        elif arg == '.rslib': self.printf('\033[1;33m',          '[Rust]:      ')
        elif arg == '.lua': self.printf('\033[1;0m',             '[Lua]:       ')
        elif arg == '.inclink': self.printf('\033[1;35m',        '[incLink]:   ')
        else:
            get = self.get(arg)
            self.printf('\033[1;{}m'.format(get[1]), get[0])


    def match_content(self):
        dirs = listdir(getcwd())
        self.read_data()

        for data in dirs:
            self.file = data
            self.match(data)


init = Lipy()
init.match_content()