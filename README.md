# Find a file on your Windows laptop / desktop using Python 3 http.server module with CGI

Ever saved a file on your laptop / desktop and then cannot find it later?

The `findfile` Python script might help :-]

## How does it work?

First of all you run a simple Windows batch file called `index.bat` that
creates a file called:

```
listing.txt
```

which is a list of all the files on your computer's `C:` drive.

Next you run another simple Windows batch file called `runff.bat` that starts a local
web server running on port 8000.

Now you open a web browser (e.g. one of Microsoft Edge, Mozilla FireFox or
Google Chrome) and enter this URL into the address bar:

```
http://127.0.0.1:8000/cgi-bin/findfile.py
```

You can now enter search text and look for file names containing that
text.

## Pre-requisites

You need Python 3 installed on your Windows laptop / desktop.

Goto:

[Python.org]<https://www.python.org/>

and look for the `Downloads` link.

## Installing `findfile`

Download the ZIP file containing the `findfile` master repository.

Unzip the ZIP file to an empty directory.

Copy the following unzipped files:

```
findfile.py
index.bat
runff.bat
```

to your user profile directory.  Your user profile directory is usually
the directory you are placed in when you start the Command Prompt desktop app.

## Running `findfile`

Open a Command Prompt.  There are a number of ways of doing this.  One way
is to search for the word:

```
cmd
```

and then click on:

```
Command Prompt
Desktop app
```

Once the command prompt which looks like:

```
C:\Users\yourusername>
```

appears type:

```
index
```

This will run the `index.bat` Windows batch file.  Depending on
how many files/directories are on your `C:` drive and how fast
your laptop /desktop is this could take a few minues.

When the `index.bat` Windows batch file has completed type:

```
runff
```

This will run the `runff.bat` Windows batch file.  This batch file
starts the local web server on port 8000.

Now start a web browser and enter the following URL in the address bar:

```
http://127.0.0.1:8000/cgi-bin/findfile.py
```

In the `Search String` input field type some text and then click
on the `Search` button.

For example if you think you saved a file with the word `payslip` in
the file name then type `payslip` in the `Search String` input field
and click `Search`.

## Refining searches

The web page allows searches to be refined by matching the search string to be an exact match,
a file name that starts with the search text and a file name that ends with the search test.

You can also make the search case sensitive by ticking the `Match case`.

If you know the type of file you are searching for you can enter the
file suffix.  For example PDF files have a file suffix of `pdf`.

## Stopping `findfile`

To stop the `findfile` local web server click on the 'X' at the top right corner of the window.

## A note on indexing

You will need to run the `index.bat` Windows batch file on a regular basis to keep
the index up to date.

----------------
End of README.md
