#!/bin/bash
PATH="/bin:/sbin:/usr/sbin:/usr/bin:/usr/local/bin:/usr/local/sbin"

if [ $EUID -ne 0 ]; then
    echo "You need to be root to install mdocu"
    exit 1
fi

if [ -d /usr/share/mdocu ]; then
    echo "It seems that mdocu is already installed on your system"
    exit 1
fi

mkdir /usr/share/mdocu
if [ $? -eq 0 ]; then
    echo "Created /usr/share/mdocu"
else
    echo "Couldn't create /usr/share/mdocu, aborting"
    exit 1
fi

cp without-titlepage.tex /usr/share/mdocu && \
cp with-titlepage.tex /usr/share/mdocu
if [ $? -eq 0 ]; then
    echo "Copied templates to /usr/share/mdocu"
else
    echo "Couldn't coopy templates to /usr/share/mdocu"
fi

cp makepdf.py /usr/bin/makepdf
if [ $? -eq 0 ]; then
    echo "Copied makepdf to /usr/bin"
    echo "Mdocu has succesfully installed on your system"
    exit 0
else
    echo "Couldn't copy makepdf to to /usr/bin"
    exit 1
fi
