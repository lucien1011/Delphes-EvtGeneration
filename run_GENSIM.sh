#!/bin/bash

echo "================= Edit PSet.py file =================="
sed -i s#THISDIR#${PWD}#g PSet.py

# Copy Input Files
echo "================= List current path ================"
echo "${PWD}"
ls ${PWD}

cat PSet.py

echo "================= cmsRun PSet.py =========================="
cmsRun -j FrameworkJobReport.xml -p PSet.py 
