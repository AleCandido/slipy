IMAGES=$(wildcard *.svg)

all: png favicon

.PHONY: all png pdf favicon

png: $(patsubst %.svg,%.png,$(IMAGES))

pdf: $(patsubst %.svg,%.pdf,$(IMAGES))

favicon: favicon-32x32.png favicon.pdf

%.png: %.svg
	inkscape $< --export-png $@ -w 1200

%.pdf: %.svg
	inkscape --file=$< --export-area-drawing --without-gui --export-pdf=$@

favicon-32x32.png: favicon.svg
	inkscape $< --export-png $@ -w 32
