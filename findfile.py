#!/usr/bin/python3

#
# @(#) @(!--#) findfile.py, version 005, 30-august-2018
#
# search the listing.txt file
#

##############################################################################

#
# useful documentation and links
#
#    https://www.quora.com/How-do-I-get-around-the-Python-error-UnicodeEncodeError-ascii-codec-cant-encode-character-when-using-a-Python-script-on-the-command-line
#    https://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
#

##############################################################################

#
# imports
#

import sys
import os
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

##############################################################################

#
# constants
#

SCRIPT_TITLE = "Find File"
SCRIPT_NAME = "findfile.py"
LISTING_FILENAME = "listing.txt"

##############################################################################

def stringmatch(matchsearchstring, matchfilename, matchmethod):
    if matchsearchstring == '*':
        return True
    elif matchmethod == 'Exact':
        return matchsearchstring == matchfilename
    elif matchmethod == 'Contains':
        return matchsearchstring in matchfilename
    elif matchmethod == 'Starts':
        return matchfilename.startswith(matchsearchstring)
    elif matchmethod == 'Ends':
        return matchfilename.endswith(matchsearchstring)
    else:
        return False

##############################################################################

def suffixmatch(matchsuffix, currentsuffix):
    if matchsuffix == '':
        return True

    return matchsuffix.lower() == currentsuffix.lower()

##############################################################################

def dosearch(searchstring, suffix, matchmethod, matchcase):
    try:
        listingfile = open(LISTING_FILENAME, 'r', encoding='cp1252', errors='surrogateescape')
    except IOError:
        print('<pre>Unable to open listing file "{}" for reading</pre>'.format(LISTING_FILENAME))
        return

    matchsearchstring = searchstring

    if matchcase != 'y':
       matchsearchstring = matchsearchstring.lower()

    matchsuffix = suffix.lower()

    print('<pre>')

    ### print("Matchcase:", matchcase)
    ### print("Match search string:", matchsearchstring)
    
    numlines = 0
    nummatches = 0

    for line in listingfile:
        numlines += 1
        
        line = line.strip()

        pathcomponents = line.split('\\')
        numcomponents = len(pathcomponents)

        if numcomponents == 0:
            continue

        if numcomponents == 1:
            parentdir = ''
            filename = line
        else:
            parentdir = '\\'.join(pathcomponents[:-1])
            filename = pathcomponents[-1]

        currentsuffixlist = filename.split('.')

        if len(currentsuffixlist) == 1:
            currentsuffix = ''
            matchfilename = filename
        else:
            currentsuffix = currentsuffixlist[-1]
            matchfilename = '.'.join(currentsuffixlist[:-1])

        if matchcase != 'y':
            matchfilename = matchfilename.lower()

        ### print("Match search string:", matchsearchstring, "   Match filename:", matchfilename)

        if stringmatch(matchsearchstring, matchfilename, matchmethod):
            if suffixmatch(matchsuffix, currentsuffix):
                print('{:60s}    {}'.format(filename, parentdir))
                nummatches += 1
                ### print(line)
                ### print(parentdir)
                ### print(filename)
                ### print(numcomponents)
 
        
    if nummatches == 0:
        print("No matches out of a possible {} files/directories".format(numlines))
    elif nummatches == 1:
        print("<hr>")
        print("Exactly 1 match out of a possible {} files".format(numlines))
    else:
        print("<hr>")
        print("{} matches out of a possible {} files".format(nummatches, numlines))

    print('</pre>')

    listingfile.close()

    return

##############################################################################

#
# main
#

form = cgi.FieldStorage()

searchstring = form.getfirst('searchstring', '')
matchmethod  = form.getfirst('matchmethod',  '')
suffix       = form.getfirst('suffix',       '')
matchcase    = form.getfirst('matchcase',    '')
searchbutton = form.getfirst('searchbutton', '')

print('Content-type: text/html')
print('')

print('<head>')
print('<title>{}</title>'.format(SCRIPT_TITLE))
print('</head>')

print('<body>')

print('<h1>{}</h3>'.format(SCRIPT_TITLE))

print('<form method="post" action="{}">'.format(SCRIPT_NAME))

print('</p>')

print('<tt>Search string: </tt><input type="text" name="searchstring" value="{}">'.format(cgi.escape(searchstring)))

print('&nbsp;&nbsp;')

print('<select name="matchmethod">')
for method in [ 'Contains', 'Exact', 'Starts', 'Ends' ]:
    print('<option value="{}"'.format(method), end='')
    if method == matchmethod:
        print(' selected', end='')
    print('>{}</option>'.format(method))
print('</select>')

print('&nbsp;&nbsp;')

print('<tt>Match case: </tt><input type="checkbox" name="matchcase" value="y"', end='')
if matchcase == 'y':
    print(' checked', end='')
print('>')

print('<br>')
print('<br>')

print('<tt>File suffix:&nbsp;&nbsp; </tt><input type="text" name="suffix" value="{}">'.format(cgi.escape(suffix)))

print('<br>')
print('<br>')

print('<input type="submit" name="searchbutton" value="Search">')

print('</p>')

print('</form>')

if searchbutton != '':
    if searchstring == '':
        print('<pre>Please specify a search string</pre>')
    else:
        dosearch(searchstring, suffix, matchmethod, matchcase)

print('</body>')
