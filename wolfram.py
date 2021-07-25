from io import SEEK_CUR
import wolframalpha
import wikipedia
import requests
import urllib
from voxpopuli import Voice
appId = "JWWL47-24YGYUY3G8"
client = wolframalpha.Client(appId)
# method that search wikipedia... 
def search_wiki(keyword=''):
  # running the query
  searchResults = wikipedia.search(keyword)
  # If there is no result, print no result
  if not searchResults:
    print("No result from Wikipedia")
    return
  # Search for page... try block 
  try:
    page = wikipedia.page(searchResults[0])

  except wikipedia.DisambiguationError as err:
    page = wikipedia.page(err.options[0])
  wikiSummary = str(page.summary)
  if len(wikiSummary) > 100:
    wikiSummary = wikiSummary.partition('.')[0] + '.'
  print(wikiSummary)
  return wikiSummary
    

def search(text=''):
  try:
    res = client.query(text)
  except urllib.error.URLError:
    return ("I Can't Do That Offline")
  # Wolfram cannot resolve the question
  if res['@success'] == 'false':
     print('Question cannot be resolved')
     return 'Question cannot be resolved'
  # Wolfram was able to resolve question
  else:
    result = ''
    # pod[0] is the question
    pod0 = res['pod'][0]
    # pod[1] may contains the answer
    pod1 = res['pod'][1]
    # checking if pod1 has primary=true or title=result|definition
    if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
      # extracting result from pod1
      result = resolveListOrDict(pod1['subpod'])
      print(result)
      question = resolveListOrDict(pod0['subpod'])
      question = removeBrackets(question)
      primaryImage(question)
      return result
    else:
      # extracting wolfram question interpretation from pod0
      question = resolveListOrDict(pod0['subpod'])
      # removing unnecessary parenthesis
      question = removeBrackets(question)
      # searching for response from wikipedia
      search_wiki(question)
      primaryImage(question)
      return search_wiki(question)


def removeBrackets(variable):
  return variable.split('(')[0]

def resolveListOrDict(variable):
  if isinstance(variable, list):
    return variable[0]['plaintext']
  else:
    return variable['plaintext']

def primaryImage(title=''):
    url = 'http://en.wikipedia.org/w/api.php'
    data = {'action':'query', 'prop':'pageimages','format':'json','piprop':'original','titles':title}
    try:
        res = requests.get(url, params=data)
        key = res.json()['query']['pages'].keys()[0]
        imageUrl = res.json()['query']['pages'][key]['original']['source']
        print(imageUrl)
    except Exception as err:
        print('Exception while finding image:= '+str(err))
 