#!/bin/bash

if [ $EUID -ne 0 ]; then
    echo "You need to be root to be able to remove files from the system"
    exit 1
fi

echo "Removing template files"
rm /usr/share/mdocu/without-titlepage.tex
rm /usr/share/mdocu/with-titlepage.tex
echo "Done"

echo "Removing /usr/share/mdocu"
rmdir /usr/share/mdocu
echo "Done"

echo "Removing makepdf"
rm /usr/bin/makepdf
echo "Done"

