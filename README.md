# URL_Extracting
The code is a Python script that extracts URLs from a webpage using the requests and BeautifulSoup modules. The function get_urls takes a URL as its argument and returns a set of URLs found in the webpage.

The function first sends a GET request to the URL using the requests module and then parses the HTML content of the response using the BeautifulSoup module. It then finds all the anchor tags (<a>) in the parsed HTML using the find_all method of the soup object. For each anchor tag, it extracts the value of the href attribute using the get method of the link object. If the href value contains either 'http' or 'www', it adds the URL to the set of URLs.

If the href value contains either 'curlie.org' or 'wikipedia.org', the function recursively calls itself with the new URL and adds the resulting set of URLs to the existing set. This way, the function extracts URLs not only from the original webpage but also from any linked pages within the same domain.

Finally, the script calls the get_urls function with the URLs of two popular websites – curlie.org and wikipedia.org – and prints the resulting sets of URLs.
