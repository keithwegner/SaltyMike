import json, re, os, sys, emoji, time
import json_parser
from random import randint
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

# out_file=open("data.json","w+")
# out_file.write('[')
# with open('input.txt', 'r') as in_file:
#    size = os.path.getsize('input.txt')
#    for line in in_file.readlines():
#     size -= len(line)
#     if not size and re.match("^}$", line, flags=0):
#       line = '},'
#     out_file.write(line)
# out_file.write(']')
# out_file.close() 

result_set = {}

def main():
  init(strip=not sys.stdout.isatty())
  cprint(figlet_format('salty mike\'s salt parser', font='starwars'), 'white', 'on_blue', attrs=['dark','bold'])

  data_file = input("Provide input file path (or press enter if file is \'in.json\'): ")
  if not data_file:
    data_file = 'in.json'
  
  conf_file = input('Provide configuration file path (or press enter if file is \'conf.properties\'): ')
  if not conf_file:
    conf_file = 'conf.properties'
  print()
  with open(conf_file) as c:
      conf = c.read().splitlines()
  with open(data_file, 'r') as json_file:
    hosts = json.loads(''.join(json_file))
    for host in hosts:
      for k,v in host.items():
        addResults(conf, k, json_parser.parse(host))
        json_parser.output_dict = {}
  print_results()

def addResults(conf, hostname, output_dict):
    if hostname not in result_set:
      result_set[hostname] = []
    for k,v in json_parser.output_dict.items():
      if k in conf:
        result_set[hostname] = ['%s=%s'%(k,v[0])]
      for i in v:
        for j in conf:
          if j in i:
            if hostname in result_set:
              result_set[hostname].append(i)
            else:
              result_set[hostname] = [i]

def print_results():
  sys.stdout.write('Processing')
  rand_int = randint(30,60)
  for i in range(rand_int):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(0.1)
  print('\nCompleted! %s  Let\'s see what we found!\n' %'\N{slightly smiling face}')
  time.sleep(2)

  for k,v in result_set.items():
    print('host:%s'%k)
    print('  |')
    if(len(v)==0) :
      print('  |---> None found %s'%'\N{pile of poo}')
    for l in v:
      print('  |---> %s' %l)
    print()
if __name__=="__main__":
  main()