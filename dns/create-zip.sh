:

FOLDER=$(basename `pwd`)
ZIPNAME="CS391-$FOLDER"

FILES='
dns-tutorial.docx
dns-tutorial.md
dns-tutorial.sh
entrypoint.sh
main.py
'

rm -rf ${ZIPNAME}.zip
zip -r ${ZIPNAME}.zip $FILES

