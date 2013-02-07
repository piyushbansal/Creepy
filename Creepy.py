import sys, urlparse, urllib2,robotparser,httplib,logging
from bs4 import BeautifulSoup


''' Setup Logger'''

Logger=logging.getLogger("MyLogger")
logging.basicConfig(filename='logging.log',filemode='w',level=logging.DEBUG)

''' Setup Robot'''

robot = robotparser.RobotFileParser()

class Creepy:
	def __init__(self):

		''' default constructor of the class Creepy'''

		self.url_seed="seed"
		self.url_number=0			# Stores the maximum number of links to be explored.
		self.queue=[]				# Basic construct to perform BFS
		self.repository=[]			# Collected URLs

	def processinput(self):

		''' Takes the input and stuffs it into required variables '''
		global Logger
		if(len(sys.argv)<2):
			logging.info("No seed url provided")
			print "No seed url provided"
			sys.exit()
		if(len(sys.argv)<3):
			logging.info("Number of URLs unspecified, default is 200")
			print "Number of URLs unspecified , default is 200"
			self.url_number=int(200)	# Default maximum number of links to be explored is 200		
		else :
			self.url_number=int(sys.argv[2])
		self.url_seed=sys.argv[1]		# Input seed url for crawling to start.

	def initqueue(self):
		self.queue.append(self.url_seed)

	def crawl(self):
		global Logger,robot
		while len(self.queue) > 0:
			url=self.queue[0]
			Logger.info('Crawling '+url)		# Logging which URL is being crawled
			urlparsed=urlparse.urlparse(url)	

			''' Respect robots.txt to prevent spider traps ! '''

			robot.set_url('http://'+urlparsed[1]+"/robots.txt")
			if not robot.can_fetch('Creepy', url.encode('ascii', 'replace')):
				logger.warning("Respect robots.txt, did not crawl: %s " % url)
				continue
	
			self.queue=self.queue[1:]

			''' Making a request block to be sent , with header Creepy '''

			request = urllib2.Request(str(url))
			request.add_header('User-Agent', 'Creepy')
	
			response,data=None,None
	
			''' Basic try except block for error handling '''

			try: 
				response = urllib2.urlopen(request,None,2.5)
			except urllib2.HTTPError, e:
				Logger.error('HTTPError = ' + str(e.code))
				Logger.info('chances are that you typed the URL wrong')
			except urllib2.URLError, e:
				Logger.error('URLError = ' + str(e.reason))
			except httplib.HTTPException, e:
				Logger.error('HTTPException')
			except Exception:
				Logger.error('generic exception: ' + traceback.format_exc())
	
			if response:
				data = response.read()			# Extracted HTML page

				''' Beautiful Soup to extract URLS '''

				soup = BeautifulSoup(data)
				for link in soup.find_all('a'):
					valid_url=link.get('href')

					''' Just external links are stored, internal links are ignored '''

					if valid_url and (valid_url.find('http')==0 or valid_url.find('https')==0) and valid_url not in self.repository:
							self.repository.append(valid_url)
							if(len(self.repository)>=self.url_number):
								return self.repository
							else:
								self.queue.append(valid_url)

	


if __name__ == "__main__":
	try:
		crawler=Creepy()
		crawler.processinput()
		crawler.initqueue()
		repository=crawler.crawl()
		for links in repository:
			print links
	except KeyboardInterrupt:
		Logger.error("Stopping due to KeyboardInterrupt")
		sys.exit()
	except Exception, e:
		Logger.error("generic Exception: %s " % e)

				




