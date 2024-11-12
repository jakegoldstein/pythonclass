import json

def by_mean_temp(arg):
    mean_temp = arg["mean_temp"]

    return(int(mean_temp))

fh = open('weny_lod_tiny.json')
lod = json.load(fh)

sorted_dicts = sorted(lod, key=by_mean_temp)

for idict in sorted_dicts:
    print(idict)