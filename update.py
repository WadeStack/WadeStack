import re
import requests
import xml.etree.ElementTree as ET

feed = requests.get('https://WadeStack.github.io/atom.xml').text
root = ET.fromstring(feed)
nsfeed = {'nsfeed': 'http://www.w3.org/2005/Atom'}
with open('README.md', 'w') as f:
    f.write(r'''
```python
print("want to be a awesome engineer")
```
''')

## Statistics
![Stats](https://github-readme-stats.vercel.app/api?username=netcan)
![Lang](https://github-readme-stats.vercel.app/api/top-langs/?username=netcan&hide=ipynb,html&layout=compact)
''')
