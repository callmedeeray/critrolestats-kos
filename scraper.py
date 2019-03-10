# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from lxml import html
import requests


# # Read in a page
# html = scraperwiki.scrape("https://www.critrolestats.com/dmcrits-wm")  
## need everything in the <ol> elements with class c6

##root = fromstring(page.content)
##print [child.tag for child in root.iterdescendants()]


page3 = requests.get('https://docs.google.com/document/d/e/2PACX-1vSxiGzyYSMs9Wd5VMJi1kk-vwxmMYRozfPfJ47jYrQjokC1N4-gwG6kMioUGcLj75KPFyTQsG4Zggyi/pub?embedded=true')
tree3 = html.fromstring(page3.content)


kos = tree3.xpath('//ol[2]//span/text()')


pk = 1
for k in kos:
    ind = k.find('(')
    char = k[0:ind-1]
    ind2 = k.find(')')
    epinfo = k[ind+1:ind2]
    bywhat = k[ind2+2:len(k)]
    dat = {'character': char, 'episode_info': epinfo, 'killed_by_what': bywhat, 'KOs': 1.0, 'full_string': k,'pk': pk}
    scraperwiki.sqlite.save(unique_keys=['pk'], data = dat)
    pk += 1


        


#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("ol[class='c6']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
