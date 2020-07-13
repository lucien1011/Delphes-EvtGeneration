
from WMCore.Configuration import Configuration

import datetime, time
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')

#____________________________________________________________||
config = Configuration()

#____________________________________________________________||
config.section_("General")
config.General.requestName     = 'ZJetsToLL_LO_MLM'
config.General.workArea        = 'crab_ZJetsToLL_LO_MLM_GENSIM'
config.General.transferOutputs = True
config.General.transferLogs    = True

#____________________________________________________________||
config.section_("JobType")
config.JobType.pluginName                       = 'PrivateMC'
config.JobType.psetName                         = 'step1_GENSIM_cfg.py'
config.JobType.scriptExe                        = 'run_GENSIM.sh'
config.JobType.inputFiles                       = ['ZJetsToLL_LO_MLM_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']
config.JobType.numCores                         = 8
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles                      = ['LHE-GEN-SIM_inLHE.root', 'LHE-GEN-SIM.root']
config.JobType.allowUndistributedCMSSW          = True

#____________________________________________________________||
config.section_("Data")
config.Data.outputPrimaryDataset    = 'ZJetsToLL_LO_MLM'
config.Data.inputDBS                = 'global'
config.Data.splitting               = 'EventBased'
config.Data.unitsPerJob             = 5000
config.Data.totalUnits              = config.Data.unitsPerJob * 1000 
config.Data.outLFNDirBase           = '/store/user/klo/ZJetsToLL_LO_MLM/GEN-SIM/'
config.Data.publication             = True
config.Data.publishDBS              = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSWriter/'
config.Data.outputDatasetTag        = 'PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3'

#____________________________________________________________||
config.section_("Site")
config.Site.storageSite = 'T2_US_Florida'
