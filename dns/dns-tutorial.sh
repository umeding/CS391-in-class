:
NAME=dns-tutorial
OUTPUT=${NAME}.docx
INPUT=${NAME}.md
pandoc $INPUT \
  -o $OUTPUT \
  --from markdown+backtick_code_blocks+fenced_code_blocks+pipe_tables \
  --template=/home/uwe/Software/pas/eisvogel.tex \
  --listing
xdg-open $OUTPUT
