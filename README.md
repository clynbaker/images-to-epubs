This is a tool to make an EPUB file containing images. (Currently it only recognizes PNGs.)

Download pngsToEpub.sh, makePages.py, and container.xml. They must all be in the same directory.
Collect the PNGs you want into a single directory. Then run pngsToEpub.sh. It will ask you for the directory that contains your PNGs. Next it will ask what you want to name the new directory that will contain your EPUB, and then what you want to name the EPUB itself.
The bash script will then use the python script to create an EPUB out of the PNGs! It should be readable by Kindles and other eReaders.
