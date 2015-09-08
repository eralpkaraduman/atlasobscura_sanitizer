import json
import jinja2
import os

# http://www.atlasobscura.com/search?q=&lat=60.15&lng=25.02&bounds%5Bne%5D%5B%5D=60.25&bounds%5Bne%5D%5B%5D=25.23&bounds%5Bsw%5D%5B%5D=60.05&bounds%5Bsw%5D%5B%5D=24.80&page=1&source=desktop

with open('obscura_helsinki.json') as data_file:
	data = json.load(data_file)

results = data['results']

pois = []

for result in results:
	poi = dict(
		title = result["result"]["title"],
		thumbnail = result["result"]["thumbnail_url"],
		url = "http://atlasobscura.com"+result["result"]["url"]
		)
	pois.append(poi)

data = dict(pois = pois)

script_dir = os.path.dirname(os.path.abspath(__file__))

templateLoader = jinja2.FileSystemLoader( searchpath=script_dir )
templateEnv = jinja2.Environment( loader=templateLoader )
template = templateEnv.get_template('template.jinja')
html_string = template.render(data)

html_file = open("obscura.html","w")
html_file.write(html_string)
html_file.close()

print "ok"