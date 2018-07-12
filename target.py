# Searches web page for target keyword
# If located, displays number of occurances

# make input() does the job on either 2.x or 3.x
try:
  input = raw_input
except NameError:
  pass

def thorough_search(url, keyword):

  url = input('Enter URL, beginning with https://\n')
  keyword = input('Enter target to search for\n')
  import pluralize
  try:
 # tries for Python 3.x and falls back to Python 2.x urllib2, if needed
    from urllib.request import urlopen
  except ImportError or ModuleNotFoundError:
    from urllib2 import urlopen
  import re
    
 # defines variable for analyzing web page content
  html_content = (urlopen(url).read())
  matches = re.findall(str(keyword), str(html_content))

  response = "Target `%s` in `%s` was located and appears %s!" % (keyword, url, pluralize.how_many(len(matches), 'time')) 
  print("\n" + response)

# calls funtion, asks for input, assigns values for (url, keyword)  
thorough_search(input, input)

# displays results until "Enter" is pressed
exit = input("\nPress Enter to close")
print(exit)
