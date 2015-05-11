#!/bin/bash
set -e
PATH="/bin:/sbin:/usr/sbin:/usr/bin:/usr/local/bin:/usr/local/sbin"

if [ $EUID -ne 0 ]; then
    echo "You need to be root to install mdocu"
    exit 1
fi

if [ -d /usr/share/mdocu ]; then
    echo "It seems that mdocu is already installed on your system"
    exit 1
fi

mkdir -v /usr/share/mdocu

cp -v without-titlepage.tex /usr/share/mdocu
cp -v with-titlepage.tex /usr/share/mdocu

cp -v makepdf.py /usr/bin/makepdf

echo "Mdocu has succesfully installed on your system"
exit 0
