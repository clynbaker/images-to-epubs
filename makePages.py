import uuid
import datetime

#Write to mimetype
mime = open('mimetype', 'w')
mime.write('application/epub+zip')
mime.close()

#Extract image file names from fileList.txt
filelist = open('fileList.txt', 'r')
namelist = []
for filename in filelist:
    name = filename.rstrip()[:-4]
    namelist.append(name)
filelist.close()

#Create a HTML file for each image
for name in namelist:
    htmlfile = open(name + '.html', 'w')
    htmlfile.write('<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n<head>\n\t<meta charset="UTF-8"/>\n'\
                   f'\t<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n\t<title>Page {name}</title>\n'\
                   f'</head>\n<body>\n\t<img src="{name}.png" alt="{name}"/>\n</body>\n</html>\n')
    htmlfile.close()

#Fill content.opf with information
contentfile = open('content.opf', 'w')
title = input("What should be the title of the ebook?\n")
newuuid = str(uuid.uuid4())
nowtime = datetime.datetime.utcnow()
nowtime = nowtime.strftime('%Y-%m-%dT%H:%M:%SZ')
contentfile.write('<package version="3.0" xmlns="http://www.idpf.org/2007/opf" xmlns:dc="http://purl.org/dc/elements/1.1/" '\
                  'xmlns:opf="http://www.idpf.org/2007/opf" unique-identifier="bookid">\n'\
                  f'\t<metadata>\n\t\t<dc:language>en</dc:language>\n\t\t<dc:title>{title}</dc:title>\n'\
                  f'\t\t<dc:creator>Image to EPUB tool by Clyn</dc:creator>\n\t\t<dc:identifier id="bookid">urn:uuid:{newuuid}'\
                  f'</dc:identifier>\n\t\t<meta property="dcterms:modified">{nowtime}</meta>\n\t</metadata>\n\t<manifest>\n'\
                  f'\t\t<item properties="cover-image" id="cover" href="{namelist[0]}.png" media-type="image/png"/>\n')
for name in namelist:
    contentfile.write(f'\t\t<item id="id{name}" href="{name}.html" media-type="application/xhtml+xml"/>\n'\
                      f'\t\t<item id="id{name}-image" href="{name}.png" media-type="image/png"/>\n')
contentfile.write('\t\t<item id="nav" href="nav.xhtml" properties="nav" media-type="application/xhtml+xml"/>\n\t</manifest>\n\t<spine>\n')
for name in namelist:
    contentfile.write(f'\t\t<itemref idref="id{name}"/>\n')
contentfile.write('\t</spine>\n\t<guide>\n'\
                  f'\t\t<reference type="cover" title="Cover" href="{namelist[0]}.html"/>\n'\
                  '\t</guide>\n</package>\n')
contentfile.close()

#Write to nav.xhtml
nav = open('nav.xhtml', 'w')
nav.write('<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">\n<head>\n'\
          '\t<title>Navigation</title>\n</head>\n<body>\n\t<nav id="nav" epub:type="toc">\n\t\t<h1>Navigation</h1>\n\t\t<ol>\n')
for name in namelist:
    nav.write(f'\t\t\t<li><a href="{name}.html">{name}</a></li>\n')
nav.write('\t\t</ol>\n\t</nav>\n</body>\n</html>\n')
nav.close()



