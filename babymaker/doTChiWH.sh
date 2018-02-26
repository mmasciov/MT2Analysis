#!/bin/bash

make -j 8 || return $?

INDIR=/hadoop/cms/store/group/snt/run2_moriond17_fastsim/SMS-TChiWH_WToLNu_HToBB_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16MiniAODv2-PUSummer16Fast_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/V08-00-16/
for ((i=1;i<=63;i++));
do
    nohup ./processBaby TChiWH_$i ${INDIR}merged_ntuple_${i}.root >& logs/TChiWH_${i}.txt &
done