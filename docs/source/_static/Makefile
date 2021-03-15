IMAGES=$(wildcard *.svg)

all: png favicon

.PHONY: all png pdf favicon

png: $(patsubst %.svg,%.png,$(IMAGES))

pdf: $(patsubst %.svg,%.pdf,$(IMAGES))

favicon: favicon-32x32.png favicon.pdf

%.png: %.svg
	inkscape $< --export-type="png" --export-filename=$@ -w 1200

%.pdf: %.svg
	inkscape $< --export-area-drawing --export-type="pdf" --export-filename=$@

favicon-32x32.png: favicon.svg
	inkscape $< --export-type="png" --export-filename=$@ -w 32
