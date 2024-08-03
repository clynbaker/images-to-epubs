#!/bin/bash

# Instructions: Make sure you have this file in the same directory as
# makePages.py and container.xml. Run this script and it will make an
# epub folder, where each page is a PNG from the directory you told it.

pwd
echo What is the path of the directory with PNGs?
echo Just type . if it is the current directory.
read imgdir
echo What should the name of the new directory be?
read targetdir
mkdir $targetdir
cp $imgdir/*.png ./$targetdir/
cp ./makePages.py  ./$targetdir/
cd ./$targetdir
touch mimetype
touch nav.xhtml
mkdir META-INF
cp ../container.xml ./META-INF/
ls *.png > fileList.txt
python3 makePages.py
rm fileList.txt makePages.py
zip -X0 $targetdir.epub mimetype
zip -r $targetdir.epub * -x mimetype
rm -r META-INF *.png *.html mimetype content.opf nav.xhtml
echo Done!
