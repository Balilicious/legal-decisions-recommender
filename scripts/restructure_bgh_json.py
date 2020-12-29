#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
restructure and filter original BGH decisions
"""

import xmltodict
import json

# read decisions from json, transform every decision, write transformed version to new file:
def transformDecisionFromJsonList(filename_in, transformFunction, filename_out):
    transformed_decisions = []
    file = open(filename_in, "r")
    json_list = file.readlines()
    for item in json_list:
        decision = json.loads(item)
        transformed_decision = transformFunction(decision)
        transformed_decisions.append(transformed_decision)   
    dict2json(transformed_decisions, filename_out)

 # write dict to json file
def dict2json(dict_list, filename):
	with open(filename, 'w') as fp:				
		fp.write('\n'.join(json.dumps(i) for i in dict_list))


# transform original json decision to substantially condensed version of decision as dict
def transformDecision(decision):

    entry = decision

    doknr = extract_element_from_json(entry, ["dokument", "doknr"])
    gertyp = extract_element_from_json(entry, ["dokument", "gertyp"])
    spruchkoerper = extract_element_from_json(entry, ["dokument", "spruchkoerper"])
    datum = extract_element_from_json(entry, ["dokument", "entsch-datum"])
    az = extract_element_from_json(entry, ["dokument", "aktenzeichen"])
    doktyp = extract_element_from_json(entry, ["dokument", "doktyp"])

    titel = extract_element_from_json(entry, ["dokument", "titelzeile", "dl", "dd", "p"])

    tenor = extract_element_from_json(entry, ["dokument", "tenor", "div", "dl", "dd", "p"])

    gruende = extract_element_from_json(entry, ["dokument", "gruende", "div", "dl", "dd", "p"])

    decision_dict = {"az": az[0], "datum": datum[0], "doknr": doknr[0], "gertyp": gertyp[0], "spruchkoerper": spruchkoerper[0], "doktyp": doktyp[0], "titel": titel[0], "tenor": tenor, "gruende": gruende}

    return decision_dict


# function from https://bcmullins.github.io/parsing-json-python/:
def extract_element_from_json(obj, path):
    '''
    Extracts an element from a nested dictionary or
    a list of nested dictionaries along a specified path.
    If the input is a dictionary, a list is returned.
    If the input is a list of dictionary, a list of lists is returned.
    obj - list or dict - input dictionary or list of dictionaries
    path - list - list of strings that form the path to the desired element
    '''
    def extract(obj, path, ind, arr):
        '''
            Extracts an element from a nested dictionary
            along a specified path and returns a list.
            obj - dict - input dictionary
            path - list - list of strings that form the JSON path
            ind - int - starting index
            arr - list - output list
        '''
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        
                        if type(item) is str:
                            arr.append(item)
                        else:
                            arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr


transformDecisionFromJsonList("orig_data/converted_bgh_straf_decisions_nocomma.json", transformDecision, "orig_data/restructured_bgh_decisions_nocomma.json")
