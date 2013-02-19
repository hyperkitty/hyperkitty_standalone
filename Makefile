NAME = hyperkitty_standalone
LASTTAG := $(shell git tag | tail -1)
VERSION := $(patsubst v%,%,$(LASTTAG))

all: sdist
sdist: dist/$(NAME)-$(VERSION).tar.gz
dist/$(NAME)-$(VERSION).tar.gz:
	mkdir -p dist
	git archive --prefix=$(NAME)-$(VERSION)/ -o $@ $(LASTTAG)
