#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the markdown-file you wish to convert")
    parser.add_argument("--no-toc", help="don't make any table of contents",
        action="store_true")
    parser.add_argument("--no-title", help="don't include a titlepage",
        action="store_true")
    args = parser.parse_args()
    
    print args.filename

if __name__=='__main__':
    main()

