:

FOLDER=$(basename `pwd`)
ZIPNAME="CS391-$FOLDER"

FILES='
next.config.mjs
next-env.d.ts
package.json
public
README.md
src
tsconfig.json
'

rm -rf ${ZIPNAME}.zip
zip -r ${ZIPNAME}.zip $FILES

