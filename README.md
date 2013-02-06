Creepy
======

A python based Web Crawler, simple and sexy :D
Has a logger where error,info anf warning logs are stored.

Dependencies
------------

Make sure that you have BeautifulSoup installed, rest are pretty much common python libraries.


Usage:
-----

$ python Creepy.py {URL name} {Number of links}

example:

$ python Creepy.py http://www.google.com 12
# Do checkout logging.log in case you want to read logs.


Output:

['http://www.google.co.in/imghp?hl=en&tab=wi', 'http://maps.google.co.in/maps?hl=en&tab=wl', 'https://play.google.com/?hl=en&tab=w8', 'http://www.youtube.com/?gl=IN&tab=w1', 'http://news.google.co.in/nwshp?hl=en&tab=wn', 'https://mail.google.com/mail/?tab=wm', 'https://drive.google.com/?tab=wo', 'http://www.google.co.in/intl/en/options/', 'http://www.google.co.in/history/optout?hl=en', 'https://accounts.google.com/ServiceLogin?hl=en&continue=http://www.google.co.in/', 'http://www.google.co.in/setprefs?sig=0_eZNCOkQ0w6T8K66yLMxMn5b3A4Y%3D&hl=hi&source=homepage', 'http://www.google.co.in/setprefs?sig=0_eZNCOkQ0w6T8K66yLMxMn5b3A4Y%3D&hl=bn&source=homepage', 'http://www.google.co.in/setprefs?sig=0_eZNCOkQ0w6T8K66yLMxMn5b3A4Y%3D&hl=te&source=homepage']
