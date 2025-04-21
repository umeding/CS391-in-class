:

FOLDER=$(basename `pwd`)
ZIPNAME="CS391-$FOLDER"

FILES='
README.md
uml.drawio
jsdoc
tsdoc
python
'

rm -rf ${ZIPNAME}.zip
zip -r ${ZIPNAME}.zip $FILES

