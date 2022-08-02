import json
from tools import *

with open("/Users/etyates/src/github/Open-Source-Catalog/code.json","r") as f:
	cod = json.loads(f.read())['releases']
with open("/Users/etyates/src/github/Open-Source-Catalog/catalog.json","r") as f:
	cat = json.loads(f.read())

def check(n):
	for pr in cod:
		if n == pr['name']:
			# print('YES')
			return True
	print('   NO')
	return False

for p in cat:
	# if p['permissions']['usageType'] == 'openSource':
	check(p['Software'])
