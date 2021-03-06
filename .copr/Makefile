MOCK_RESULT_DIR := $(outdir)
MOCK_SRPM_RESULT_DIR := $(outdir)
ifndef outdir
	MOCK_RESULT_DIR := "./results/%(dist)s/%(target_arch)s/"
	MOCK_SRPM_RESULT_DIR := ./results/srpm
endif

MOCK_SOURCESDIR := $(spec)
ifndef spec
	MOCK_SOURCESDIR := ./
endif

MOCK_SRPM := $(srpm)
ifndef srpm
	MOCK_SRPM := $(MOCK_SRPM_RESULT_DIR)/*.src.rpm
endif

distros := fedora-26 fedora-27 fedora-28 fedora-29 fedora-rawhide
arches := x86_64 i386
rpm_targets := $(foreach a,$(arches),$(patsubst %,%-$a-rpm,$(distros)))
rpm_clean_targets := $(foreach a,$(arches),$(patsubst %,%-$a-clean,$(distros)))

MOCK_DISTGZ := $(distgz)
ifndef distgz
	MOCK_DISTGZ := xautolock-*.tgz
endif

.PHONY: fetch
fetch: $(MOCK_DISTGZ)

$(MOCK_DISTGZ):
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/xautolock.spec

.PHONY: srpm
srpm: fetch $(MOCK_SRPM)

$(MOCK_SRPM):
	mock --buildsrpm --spec=$(MOCK_SOURCESDIR)/xautolock.spec --sources=$(MOCK_SOURCESDIR) --resultdir=$(MOCK_SRPM_RESULT_DIR)

.PHONY: dist
dist: fetch srpm

#.PHONY: $(rpm_targets)
%-rpm: srpm
	mock --rebuild -r $* --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

.PHONY: rpm-all
rpm-all: $(rpm_targets)

#.PHONY: $(rpm_clean_targets)
%-clean:
	mock --rebuild -r $* --clean
	mock -r $* --scrub=chroot

.PHONY: clean-all
clean-all: $(rpm_clean_targets)

.PHONY: clean
clean: clean-all
	rm -rf $(MOCK_RESULT_DIR) results

.PHONY: distclean
distclean:
	rm -rf $(MOCK_SOURCESDIR)/xautolock-2.2.tgz

.PHONY: cleanall
cleanall: clean distclean

.PHONY: distall
distall: dist rpm-all

.PHONY: all
all: rpm-all

