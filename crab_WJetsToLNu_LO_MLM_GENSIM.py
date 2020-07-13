
from WMCore.Configuration import Configuration

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

#____________________________________________________________||
config = Configuration()

#____________________________________________________________||
config.section_("General")
config.General.requestName     = 'WJetsToLNu_LO_MLM'
config.General.workArea        = 'crab_WJetsToLNu_LO_MLM_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

#____________________________________________________________||
config.section_("JobType")
config.JobType.pluginName                       = 'PrivateMC'
config.JobType.psetName                         = 'step1_GENSIM_WJetsToLNu_cfg.py'
config.JobType.scriptExe                        = 'run_GENSIM.sh'
config.JobType.inputFiles                       = ['WJetsToLNu_LO_MLM_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']
config.JobType.numCores                         = 8
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles                      = ['LHE-GEN-SIM_inLHE.root', 'LHE-GEN-SIM.root']
config.JobType.allowUndistributedCMSSW          = True

#____________________________________________________________||
config.section_("Data")
config.Data.outputPrimaryDataset    = 'WJetsToLNu_LO_MLM'
config.Data.inputDBS                = 'global'
config.Data.splitting               = 'EventBased'
config.Data.unitsPerJob             = 10000
config.Data.totalUnits              = config.Data.unitsPerJob * 2000 
config.Data.outLFNDirBase           = '/store/user/klo/WJetsToLNu_LO_MLM/GEN-SIM/'
config.Data.publication             = True
config.Data.publishDBS              = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag        = 'PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3'

#____________________________________________________________||
config.section_("Site")
config.Site.storageSite = 'T2_US_Florida'
