import os,argparse

#____________________________________________________________||
parser = argparse.ArgumentParser()
parser.add_argument('--outputPath',action='store')
parser.add_argument('--General_requestName',action='store')
parser.add_argument('--General_workArea',action='store')
parser.add_argument('--JobType_psetName',action='store')
parser.add_argument('--JobType_scriptExe',action='store')
parser.add_argument('--JobType_inputFiles',action='store')
parser.add_argument('--JobType_outputFiles',action='store')
parser.add_argument('--Data_outLFNDirBase',action='store')
parser.add_argument('--Data_outputDatasetTag',action='store')
parser.add_argument('--njobs',action='store',type=int)

option = parser.parse_args()

#____________________________________________________________||
templateText = """
from WMCore.Configuration import Configuration

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

#____________________________________________________________||
config = Configuration()

#____________________________________________________________||
config.section_("General")
config.General.requestName     = '{requestName}'
config.General.workArea        = '{workArea}'
config.General.transferOutputs = True
config.General.transferLogs    = True

#____________________________________________________________||
config.section_("JobType")
config.JobType.pluginName                       = 'PrivateMC'
config.JobType.psetName                         = '{psetName}'
config.JobType.scriptExe                        = '{scriptExe}'
config.JobType.inputFiles                       = {inputFiles}
config.JobType.numCores                         = 8
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles                      = {outputFiles}
config.JobType.allowUndistributedCMSSW          = True

#____________________________________________________________||
config.section_("Data")
config.Data.outputPrimaryDataset    = '{requestName}'
config.Data.inputDBS                = 'global'
config.Data.splitting               = 'EventBased'
config.Data.unitsPerJob             = 10000
config.Data.totalUnits              = config.Data.unitsPerJob * {njobs} 
config.Data.outLFNDirBase           = '{outLFNDirBase}'
config.Data.publication             = True
config.Data.publishDBS              = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag        = '{outputDatasetTag}'

#____________________________________________________________||
config.section_("Site")
config.Site.storageSite = 'T2_US_Florida'
"""

#____________________________________________________________||
outputText = templateText.format(
    requestName = option.General_requestName,
    workArea = option.General_workArea,
    psetName = option.JobType_psetName,
    scriptExe = option.JobType_scriptExe,
    inputFiles = str(option.JobType_inputFiles.split(",")),
    outputFiles = str(option.JobType_outputFiles.split(",")),
    njobs = option.njobs,
    outLFNDirBase = option.Data_outLFNDirBase,
    outputDatasetTag = option.Data_outputDatasetTag,
    )
outputFile = open(option.outputPath,"w")
outputFile.write(outputText)
outputFile.close()

os.system('crab submit '+option.outputPath)
