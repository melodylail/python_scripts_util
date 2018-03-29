import urllib

import sys,os,os.path
import requests

proxies = {'http': 'http://child-prc.intel.com:913'}
os.environ['HTTP_PROXY']="http://child-prc.intel.com:913"
os.environ['HTTPS_PROXY']="http://child-prc.intel.com:913"

#create the object, assign it to a variable
proxy = urllib.request.ProxyHandler({'http': 'child-prc.intel.com:913'})
# construct a new opener using your proxy settings
opener = urllib.request.build_opener(proxy)
# install the openen on the module-level
urllib.request.install_opener(opener)

#requests.get("http://google.com")
#requests.get("http://59.110.221.38/ids.data", proxies=proxies)
urllib.request.urlretrieve("http://59.110.221.38/ids.data", "ids.data")