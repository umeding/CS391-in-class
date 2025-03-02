:
set -x

FOLDER=$(basename `pwd`)
ZIPNAME="CS391-$FOLDER"

FILES='
*.py
*.sh
requirements.txt
README.md
'

rm -rf ${ZIPNAME} ${ZIPNAME}.zip
mkdir ${ZIPNAME}
cp -r $FILES $ZIPNAME

zip -r ${ZIPNAME}.zip $ZIPNAME

rm -rf $ZIPNAME
