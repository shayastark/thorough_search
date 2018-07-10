# Searches web page for target keyword
# If located, displays number of occurances

def thorough_search(url, keyword):
  
  
  url = input('Enter URL, beginning with https://\n')
  keyword = input('Enter target to search for\n')
  try:
 # tries for Python 3.x and falls back to Python 2.x urllib2, if needed
    from urllib.request import urlopen
  except ImportError or ModuleNotFoundError:
    from urllib2 import urlopen
    
 # defines variable for analyzing web page content
  html_content = (urlopen(url).read())
  matches = re.findall(str(keyword), str(html_content))
  import re

 # creates a list. planning to adjust list functionality 
  new = []
  
  new = matches
  searchy =+ new.count(str(keyword))
  
  
 # loop to break redundancy when adding to list
  for new in matches:
    break
    return new
  
  
 # rules for printing output
  if len(matches) == 0 or searchy == 0: 
     print('\nTarget: ' + keyword + '\n' +' in ' + url + ' was not found.' + '\n' + ' Check for spelling errors.')
  elif len(matches) == 1 or searchy == 1:
     print('\nTarget: ' + keyword + '\n' + ' in ' + url + ' was located and appears ' + str(searchy) + ' time.')
  
  else:
     print('\nTarget: ' + keyword + '\n' + ' in ' + url + ' was located and appears ' + str(searchy) + ' times.')
      
  
# calls funtion, asks for input, assigns values for (url, keyword)  
thorough_search(input, input)

# displays results until "Enter" is pressed
input("\n\n\n\n\n\n\n\n\n\nPress Enter to close")
