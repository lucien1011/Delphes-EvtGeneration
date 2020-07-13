#!/bin/bash

#________________________________________________________________________________________________________________________||
# GENSIM
#python submitGENSIM.py --General_requestName ZJetsToLL_LO_MLM --General_workArea crab_ZJetsToLL_LO_MLM_GENSIM \
#--JobType_psetName step1_GENSIM_cfg.py --JobType_inputFiles ZJetsToLL_LO_MLM_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz --JobType_outputFiles LHE-GEN-SIM_inLHE.root,LHE-GEN-SIM.root --JobType_scriptExe run_GENSIM.sh \
#--Data_outLFNDirBase /store/user/klo/ZJetsToLL_LO_MLM/GEN-SIM/ --Data_outputDatasetTag PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3 \
#--njobs 1000 --outputPath crab_ZJetsToLL_LO_MLM_GENSIM.py ;

python submitGENSIM.py --General_requestName WJetsToLNu_LO_MLM --General_workArea crab_WJetsToLNu_LO_MLM_GENSIM \
--JobType_psetName step1_GENSIM_WJetsToLNu_cfg.py --JobType_inputFiles WJetsToLNu_LO_MLM_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz --JobType_outputFiles LHE-GEN-SIM_inLHE.root,LHE-GEN-SIM.root --JobType_scriptExe run_GENSIM.sh \
--Data_outLFNDirBase /store/user/klo/WJetsToLNu_LO_MLM/GEN-SIM/ --Data_outputDatasetTag PUMoriond17-Realistic25ns13TeVEarly2017Collision-93X_mc2017_realistic_v3 \
--njobs 2000 --outputPath crab_WJetsToLNu_LO_MLM_GENSIM.py ;

