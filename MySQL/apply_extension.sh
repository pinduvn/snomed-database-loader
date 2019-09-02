#!/bin/bash
set -e;

combine() {
	filePattern=$1
	cd ${intExtract}
	for thisFile in ${filePattern}*; do
		echo "Copying $thisFile"
		targetFile=`echo ${thisFile} | sed "s/${intModuleStr}/${intModuleStr}${extModuleStr}/g"` 
		cat $thisFile > ../${resultDir}/${targetFile}
		destination="../${resultDir}/${targetFile}"
		for extFile in ../${extExtract}/${filePattern}*; do
			echo "Adding ${extFile} to ${destination}"
			tail -q -n +2 ${extFile} >> ${destination}
		done
	done
	cd -
}

intReleasePath=$1
extReleasePath=$2

if [ -z ${extReleasePath} ]
then
	echo "Usage:  ./apply_extension.sh <int release location> <ext release location>"
	echo "eg ./apply_extension.sh ~/SnomedCT_InternationalRF2_Production_20180731T120000Z.zip ~/uk_sct2dr_26.2.0_20181107000001.zip"
	exit -1
fi

intModuleStr=INT
extModuleStr=GB1000001
echo "Enter module string used in extension filenames [$extModuleStr]:"
read newModuleStr
if [ -n "${newModuleStr}" ]
then
	extModuleStr=$newModuleStr
fi

tmpRND=`date +%s | sha256sum | base64 | head -c 9`
intExtract="int_extract_${tmpRND}"
unzip -j ${intReleasePath} "*Snapshot*" -d ${intExtract}

extExtract="ext_extract_${tmpRND}"
unzip -j ${extReleasePath} "*Snapshot*" -d ${extExtract}

resultDir="combined_${tmpRND}"
mkdir ${resultDir}

combine sct2_Relationship
combine sct2_StatedRelationship
combine sct2_Concept
combine sct2_Description

echo "All done, zipping up the combined files"
zip -r combined_release_${tmpRND}.zip ${resultDir}

echo "Cleaning up temporary working directories"
rm -rf ${intExtract}
rm -rf ${extExtract}
rm -rf ${resultDir}


echo "Finished!"