import urllib

def read_text(uri):
    quotes = open(uri)
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)

    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alter!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly")
read_text("/Users/lilu/Downloads/test/profanity.txt")
