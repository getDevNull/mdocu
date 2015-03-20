# mdocu #
mdocu is a small Python program that I've put together after getting more and
more interested in Markdown and Pandoc. It all started after talking to
[Jonas Björk](http://www.jonasbjork.net) about writing all
documentation in Markdown to speed up the process of writing. I started thinking
of a way to combine Markdown with LaTeX (I really like LaTeX) and found out about
Pandoc after some googling around. Pandoc can convert many formats into many
more formats, including Markdown to LaTeX (and PDF from LaTeX).
To make the document look better you have to write a template in LaTeX and
append a lot of options and arguments to Pandoc. Therefor I started writing a
Python program to quickly make a PDF out of any Markdown file with great result.
So that is what this tiny Python program is all about; to make a nice-looking
PDF out of any Markdown document.

## Installation ##
To install mdocu simply run the script install.sh as root or with sudo
priviledges, for example `sudo ./install.sh` or if you're using `su` to become
root run:

```
su
./install.sh
```

### Uninstall ###
If you which to remove all files provided by mdocu from the system simply run
the script uninstall.sh as either root or as a regular user with sudo
priviledges, for example `sudo ./uninstall.sh`.

## Required packages ##
mdocu is depending on LaTeX and Pandoc. On Ubuntu and Debian systems these can
all be installed with the command below:

```
sudo apt-get install texlive-latex-extra pandoc pandoc-citeproc \
texlive-fonts-recommended texlive-fonts-extra 
```

### For non-english writers ###
If you're writing a document that's non-english you'll also need a language pack
for your language. These packages are called texlive-lang-swedish for example for
swedish. Please note that you'll also need to change the line
`\usepackage[english]{babel}` to the language your writing in, for example
swedish will become `\usepackage[swedish]{babel}`. You'll need to change this
for both */usr/share/mdocu/with-titlepage.tex* and
*/usr/share/mdocu/without-titlepage.tex*.

## Usage ##
```
usage: makepdf [-h] [--notoc] [--notitle] [-o OUTPUT] filename

positional arguments:
  filename                      the markdown-file you wish to convert

optional arguments:
  -h, --help                    show this help message and exit
  --notoc                       don't make any table of contents
  --notitle                     don't include a titlepage
  -o OUTPUT, --output OUTPUT    save file into OUTPUT

```

### Example ###
`makepdf example.md --notoc -o example.pdf` will produce a PDF-file called
example.pdf from the markdown file example.md with no table of contents (but
with a title page).
By default if no -o option is given, the PDF-file will be save in *out.pdf*.
By default mdocu will both create a table of content and a nice looking title
page. Please note that you'll need to customize the title page by your own. This
is done in */usr/share/mdocu/with-titlepage.tex*.

## Thanks ##
Thanks to [Jonas Björk](http://www.jonasbjork.net) for mentioning that
Markdown can be an easy and powerful system for writing quick documents. 

## Copyright ##
mdocu is released under GNU General Public Licence by 
[Jack-Benny Persson](mailto:jack-benny@getdevnull.com) at
[getDevNull](http://www.getdevnull.com).
