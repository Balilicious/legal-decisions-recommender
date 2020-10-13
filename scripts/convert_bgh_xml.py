from io import BytesIO
import zipfile
import xmltodict
from pathlib import Path
import json


def convertXmls(archive):
	decisions = []
	with zipfile.ZipFile(archive, "r") as mainArchive:
		items = list(filter(lambda x: (not mainArchive.getinfo(x).is_dir()) and Path(x).suffix.lower() == ".zip", mainArchive.namelist() ))
		numItems = len(items)
		for (idx, item) in enumerate(items, start=1):
			print("\t" + 'Item '+str(idx)+' of '+str(numItems)+': '+ item)
			with zipfile.ZipFile( BytesIO(mainArchive.read(item)), "r") as innerArchive:
				xmls = innerArchive.namelist()
				for xml in xmls:
					if Path(xml).suffix.lower() == ".xml":
						with innerArchive.open(xml, "r") as xmlFile:
							xmlF = xmlFile.read()
							decision = xmltodict.parse(xmlF)
							decisions.append(decision)
							#dict2json_rowwise(decision, "converted_bgh_straf_decisions.json")
	dict2json(decisions, "converted_bgh_straf_decisions_nocomma.json")

def dict2json(dict_list, filename):
	with open(filename, 'w') as fp:
		#fp.write('[' + ',\n'.join(json.dumps(i) for i in dict_list) + ']\n')
		fp.write('\n'.join(json.dumps(i) for i in dict_list))

convertXmls("./data_rechtsprechung_bgh_strafsachen.zip")
