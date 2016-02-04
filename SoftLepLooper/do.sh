#!/bin/bash

make -j12

INDIR=/nfs-6/userdata/mt2/softLep-v2_V00-01-10_25ns_miniaodv2_skim/
OUTDIR=output/softLep/

# INDIR=/nfs-6/userdata/mt2/softLep_V00-01-10_25ns_miniaodv2_skim/
# OUTDIR=output/softLep/

# INDIR=/nfs-6/userdata/mt2/softLep_V00-01-10_25ns_miniaodv2_skimFake/
# OUTDIR=output/softLepFake/

#INDIR=/nfs-6/userdata/mt2/V00-01-09_25ns_softLepSR/
#OUTDIR=output/softLepSR/

# INDIR=/nfs-6/userdata/mt2/V00-01-09_25ns_softLepCR/
# OUTDIR=output/softLepCR/

#declare -a Samples=(data_Run2015C data_Run2015D ttsl_mg_lo ttdl_mg_lo wjets_ht zinv_ht singletop qcd_ht ttw ttz ttg tth dyjetsll_ht gjet_ht)
#declare -a Samples=(wjets_ht zinv_ht singletop ttdl ttsl ttg tth ttw ttz dyjetsll qcd_ht ww zz wz data_Run2015D data_Run2015C)
#declare -a Samples=(wjets_ht zinv_ht singletop ttdl ttsl ttg tth ttw ttz dyjetsll qcd_ht ww  data_Run2015D data_Run2015C T2-4bd_375 T2-4bd_275)
#declare -a Samples=(wjets_ht zinv_ht singletop ttdl ttsl ttg tth ttw ttz dyjetsll qcd_ht ww  data_Run2015D data_Run2015C T2-4bd_375_295 T2-4bd_375_335 T2-4bd_375_365 T2-4bd_375_355)
#declare -a Samples=(T2-4bd_275_195 T2-4bd_275_235 T2-4bd_275_265 T2-4bd_275_255)
declare -a Samples=(T5qqqqWW_1025_775 T5qqqqWW_1300_600 T5qqqqWW_1500_100)

mkdir -p ${OUTDIR}
mkdir -p logs

for SAMPLE in ${Samples[@]};
  do echo nice -n 19 ./runLooper ${INDIR} ${SAMPLE} ${OUTDIR}
  nohup nice -n 19 ./runLooper ${INDIR} ${SAMPLE} ${OUTDIR} >& logs/${SAMPLE}.log &
done

