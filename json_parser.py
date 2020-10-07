output_dict = {}

def parse(dict_obj):
  for k, v in dict_obj.items():
    if isinstance(v,list):
      for i in v:
        parse(i)
    elif isinstance(v, dict):
      parse(v)
    else:
      addToDict(k, str(v))

def addToDict(k, v):
  if k in output_dict.keys():
    output_dict[k].append(v)
  else:
    output_dict[k] = [v]