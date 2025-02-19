:

FOLDER=$(basename `pwd`)
ZIPNAME="CS391-$FOLDER"

FILES='
assets
index.html
README.md
scripts
'

rm -rf ${ZIPNAME}.zip
zip -r ${ZIPNAME}.zip $FILES

