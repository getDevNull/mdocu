#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from subprocess import call
import os.path

def main():
    
    # Define some variables
    outfile = "out.pdf" # Default output file
    home = os.path.expanduser("~")

    # First try the users own with-titlepage.tex, then the system-wide
    if  os.path.isfile(home + "/.mdocu/with-titlepage.tex"):
        with_title = home + "/.mdocu/with-titlepage.tex"
    else: 
        with_title = "/usr/share/mdocu/with-titlepage.tex" 

    # First try the users own without-titlepage.tex, the the system-wide
    if os.path.isfile(home + "/.mdocu/without-titlepage.tex"):
        without_title = home + "/.mdocu/without-titlepage.tex"        
    else:
        without_title = "/usr/share/mdocu/without-titlepage.tex"

    # Parse arguments for the script
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="the markdown-file you wish to convert")
    parser.add_argument("--notoc", help="don't make any table of contents",
        action="store_true")
    parser.add_argument("--notitle", help="don't include a titlepage",
        action="store_true")
    parser.add_argument("-c", "--custom", help="use a custom template", type=str)
    parser.add_argument("-o", "--output", type=str, 
        help="save file into OUTPUT")
    args = parser.parse_args()

    # Set output file to whatever was entered at the -o option
    if args.output:
        outfile = args.output

    # Set the custom template to whatever was entered at the -c option
    if args.custom:
        custom = args.custom

    # Iterate through the formating options    
    if args.notoc == True and args.notitle == False and not args.custom:
       call(["pandoc", "-N", "--template=" + with_title, 
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile]) 
    elif args.notoc == True and args.notitle == True:
       call(["pandoc", "-N", "--template=" + without_title, 
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile])
    elif args.notitle == True and args.notoc == False:
       call(["pandoc", "-N", "--template=" + without_title, "--toc",
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile])
    elif args.custom and args.notoc == True:
        call(["pandoc", "-N", "--template=" + custom,
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile])
    elif args.custom and args.notoc == False:
        call(["pandoc", "-N", "--template=" + custom, "--toc",
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile])
    else:
       call(["pandoc", "-N", "--template=" + with_title, "--toc",
            args.filename, "--filter", "pandoc-citeproc", "-o", outfile])

if __name__=='__main__':
    main()

