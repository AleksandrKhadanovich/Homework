# rss_reader.py

rss_reader is a Python command-line utility to print information in human-readable format from RSS URL given.

## Requirements

###To use rss_reader lxml, bs4, requests, fpdf, Pillow libraries should be installed.
rss_reader.py is on PYTHONPATH.


## Usage

###To run rss-reader you should enter:
>python rss_reader.py "URL",
where URL is valid RSS URL.

###rss_reader provides optional arguments:
--limit, --version, --json, --verbose, --help, --date, --tohtml, --topdf

###--limit : limits number of news if this parameter provided with positive integer
###--version : prints version info
###--json : prints result at JSON in stdout 
###--verbose : Outputs verbose status messages
###--date : Prints result for date entered
###--tohtml : Convert current or saved information to html format (path to save file must be provided)
###--topdf : Convert current or saved information to pdf format (path to save file must be provided)


###When rss-reader is run with source argument, downloaded information from rss is saved in cwd as 
'newslog.txt' and 'newslogjson.txt' (for json output).


###JSON format is representation of data as a list of objects consisting of name - value pairs.
rss_reader lets prints result as JSON in stdout.
if --json argument rss_reader represent data as follows:
[
    {
        "Title": "text", 
        "Link": "text", 
        "Published": "text"
    }, 
    {
        "Title": "text", 
        "Link": "text", 
        "Published": "text"
    }, 
    {
        "Title": "text", 
        "Link": "text", 
        "Published": "text"
    }
] 

For more information enter 
>python rss_reader.py --help 
in command line.

## License
Freeware license
