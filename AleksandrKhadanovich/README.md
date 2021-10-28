# rss_reader.py

rss_reader is a Python command-line utility to print information in human-readable format from RSS URL given.

## Requirements

To use rss_reader unpack rssparser-1.0.tar.gz, 
and install rss_reader via setup.py. 


## Usage

###To run rss-reader you should enter:

>python rss_reader.py "URL" or rss_reader "URL",
where URL is valid RSS URL. 


###rss_reader provides optional arguments:
--Limit, --version, --json, --help.

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
