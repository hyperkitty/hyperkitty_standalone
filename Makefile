NAME = hyperkitty_standalone
LASTTAG := $(shell git tag | tail -1)
VERSION := $(patsubst v%,%,$(LASTTAG))
NEXTVER := $(shell echo $(VERSION) | python -c 'import sys; v = sys.stdin.read().split("."); v[-1] = str(int(v[-1])+1); print ".".join(v)')

all: sdist
sdist: dist/$(NAME)-$(VERSION).tar.gz
dist/$(NAME)-$(VERSION).tar.gz:
	mkdir -p dist
	git archive --prefix=$(NAME)-$(VERSION)/ -o $@ $(LASTTAG)
prerel: dist/$(NAME)-$(NEXTVER)dev.tar.gz
dist/$(NAME)-$(NEXTVER)dev.tar.gz:
	mkdir -p dist
	git archive --prefix=$(NAME)-$(NEXTVER)dev/ -o $@ HEAD


.PHONY: all sdist prerel
