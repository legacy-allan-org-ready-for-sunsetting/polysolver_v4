cwlVersion: v1.0

class: CommandLineTool
baseCommand: [shell_call_hla_type]
id: polysolver

requirements:
  InlineJavascriptRequirement: {}
  DockerRequirement: 
    dockerPull: sachet/polysolver:v4
  ResourceRequirement:
    ramMin: 1000
    coresMin: 8


