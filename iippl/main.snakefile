shell.prefix("set -o pipefail; ")
import os
from iippl.snakeUtils import set_object_graph, all_obj_ids, all_obj_dirs, all_obj_types, T, DT, EFS, P, DP, PP
from iippl.ObjectGraph import load_object_graph

pipeline = os.environ["PIPELINE_DIR"]

configfile: "../parameters.yaml"

objectGraphFile = "../OG.json"
if 'objectGraphFile' in config:
    objectGraphFile = config['objectGraphFile']
OG = load_object_graph(objectGraphFile) 
set_object_graph(OG)

def GP(parameter):
    return config[parameter]

GP = config

for t in all_obj_types():
    tsfn = pipeline + "/" + t + ".snakefile"
    if not os.path.isfile(tsfn):
        print("Creating a starter", tsfn)
        F = open(tsfn,"w")
        print("rule %s_obj:\n"
              "  input:\n"
              "    DT('obj.flag')\n"
              "  output: \n"
              "    touch(T('obj.flag'))" % (t),file=F)
        F.close()
    include: tsfn

rule all_main:
  input:
    expand("{od}/obj.flag", od=all_obj_dirs())

