#!/bin/bash

#
# args
#

FILEID=$1
FILE=$2
COPYDIR=$3

echo "[wrapper] FILEID    = " ${FILEID}
echo "[wrapper] FILE      = " ${FILE}
echo "[wrapper] COPYDIR   = " ${COPYDIR}

#
# set up environment
#
CMSSW_VERSION=CMSSW_9_2_4

###version using cvmfs install of CMSSW
echo "[wrapper] setting env"
export SCRAM_ARCH=slc6_amd64_gcc530
source /cvmfs/cms.cern.ch/cmsset_default.sh
OLDDIR=`pwd`
cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/cmssw/$CMSSW_VERSION/src
#cmsenv
eval `scramv1 runtime -sh`
cd $OLDDIR

# ### version using nfs install of CMSSW
# echo "[wrapper] setting env"
# export SCRAM_ARCH=slc6_amd64_gcc493
# source /nfs-7/cmssoft/cms.cern.ch/cmssw/cmsset_default.sh
# OLDDIR=`pwd`
# cd /nfs-7/cmssoft/cms.cern.ch/cmssw/slc6_amd64_gcc493/cms/cmssw-patch/$CMSSW_VERSION/src
# #cmsenv
# eval `scramv1 runtime -sh`
# cd $OLDDIR

echo

echo "[wrapper] printing env"
printenv
echo 

echo "[wrapper] hostname  = " `hostname`
echo "[wrapper] date      = " `date`
echo "[wrapper] linux timestamp = " `date +%s`
echo "[wrapper] checking input file with ls"
ls -alrth ${FILE}

echo "[wrapper] trying to gfal-copy the file..."
gfal-copy -p -f -t 4200 --verbose  gsiftp://gftp.t2.ucsd.edu${FILE} file://`pwd`/${COPYDIR##*/}_${FILEID}.root
FILE=${COPYDIR##*/}_${FILEID}.root
echo "[wrapper] current directory contents:"
ls

ls $FILE
# catch exit code
if [ $? -ne 0 ]; then
    echo "[wrapper] could not find input file, trying xrootd instead"
    FILESHORT=${FILE#/hadoop/cms}
    xrdfs xrootd.t2.ucsd.edu ls ${FILESHORT}
    if [ $? -ne 0 ]; then
        echo "[wrapper] could not find input file with xrootd either, exiting"
        exit 1
    else
        echo "[wrapper] found file with xrootd, will proceed"
        FILE="root://xrootd.t2.ucsd.edu/"${FILESHORT}
    fi
fi

#
# untar input sandbox
#

echo "[wrapper] current directory is:"
pwd

echo "[wrapper] extracting input sandbox"
tar -zxf input.tar.gz

#source job_input/setupenv.sh
#printenv

cd job_input
mv ../$FILE .
echo "[wrapper] input contents are"
ls -a

echo "[wrapper] directory contents are"
ls

#
# run it
#
echo "[wrapper] running: ./processBaby ${FILEID} ${FILE}"

./processBaby ${FILEID} ${FILE} 100

#
# do something with output
#

echo "[wrapper] output is"
ls

#
# clean up
#

echo "[wrapper] copying file"
OUTPUT=`ls -t | grep ${FILEID} | head -n1`
echo "[wrapper] OUTPUT = " ${OUTPUT}

if [ ! -d "${COPYDIR}" ]; then
    echo "creating output directory " ${COPYDIR}
    mkdir ${COPYDIR}
fi

gfal-copy -p -f -t 4200 --verbose file://`pwd`/${OUTPUT} gsiftp://gftp.t2.ucsd.edu${COPYDIR}/${OUTPUT}

echo "[wrapper] cleaning up"
for FILE in `find . -not -name "*stderr" -not -name "*stdout"`; do rm -rf $FILE; done
echo "[wrapper] cleaned up"
ls
