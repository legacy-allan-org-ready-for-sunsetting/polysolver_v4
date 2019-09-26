cwlVersion: v1.0

class: CommandLineTool
baseCommand: [ /opt/polysolver/scripts/hla_call_workaround.py ]
id: polysolver

requirements:
  InlineJavascriptRequirement: {}
  DockerRequirement: 
    dockerPull: mskcc/polysolver:v4
  ResourceRequirement:
    ramMin: 10000
    coresMin: 8

inputs:
  tmp_dir:
    type: string
    inputBinding:
      prefix: --TMP_DIR

  output_prefix:
    type: string
    inputBinding:
      prefix: --outputPrefix
  
  bam_normal:
    type: File
    inputBinding:
      prefix: --bamNormal
    secondaryFiles:
      - ^.bai
 
  output_dir:
    type: string
    inputBinding:
      prefix: --outputDir 

outputs:
  output:
    type: File
    outputBinding:
      glob: |
        ${
          return inputs.output_prefix + ".hla.txt";
        }
