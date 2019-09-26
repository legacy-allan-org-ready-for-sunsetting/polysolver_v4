import sys, os 
import argparse
import subprocess
import errno

def make_dir(path):
  try:
    os.makedirs(path)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise

parser = argparse.ArgumentParser()
parser.add_argument("--TMP_DIR", required=True)
parser.add_argument("--bamNormal", required=True)
parser.add_argument("--outputPrefix", default="output")
parser.add_argument("--outputDir", required=True)

args = parser.parse_args()

tmp_dir = args.TMP_DIR
normal_bam = args.bamNormal
output_dir = args.outputDir
output_prefix = args.outputPrefix

make_dir(output_dir)
make_dir(tmp_dir)

# copy shell_call_hla_type to current working directory
cp_command = "cp /home/polysolver/scripts/shell_call_hla_type ."
subprocess.call(cp_command, shell=True)

# replace TMP_DIR with a value set in tmp_dir
sed_command = 'sed -i "171s/TMP_DIR=.*/TMP_DIR=%s/" shell_call_hla_type' % tmp_dir
subprocess.call(sed_command, shell=True)

# execute shell_call_hla_type with defaults from TEMPO
execute_cmd_list = [ "bash shell_call_hla_type" ]
execute_cmd_list.append(normal_bam)
execute_cmd_list.append("Unknown")
execute_cmd_list.append("1")
execute_cmd_list.append("hg19")
execute_cmd_list.append("STDFQ")
execute_cmd_list.append("0")
execute_cmd_list.append(output_dir)

exec_cmd = " ".join(execute_cmd_list)
subprocess.call(exec_cmd, shell=True)

# format output prefix
mv_command = "mv winners.hla.txt %s.hla.txt" % output_prefix
subprocess.call(mv_command, shell=True)
