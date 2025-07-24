HAS_GSED!=which gsed
ifdef HAS_GSED
SED=	$(HAS_GSED)
else
SED=	sed
endif


HAS_GMAKE!=	which gmake
ifdef HAS_GMAKE
MAKE=	$(HAS_GMAKE)
else
MAKE=	make
endif

HAS_DOXYGEN!=	which doxygen
ifdef HAS_DOXYGEN
DOXYGEN?=	$(HAS_DOXYGEN)
else
@echo "doxygen cannot be found in PATH" >&2
@exit 1
endif

HAS_SPHINX!=	which sphinx-build
ifdef HAS_SPHINX
SPHINX?=				sphinx-build
else
@echo "sphinx-build cannot be found in PATH" >&2
@exit 1
endif

SRC_DIR=	.
BUILD_DIR=	_build

DOXYGEN_CONF=	doxygen.conf
DOXYGEN_OUTPUT_DIR=	_docs
DOXYGEN_XML_DIR=	$(DOXYGEN_OUTPUT_DIR)/xml
DOXYGEN_XML_FILE=	$(DOXYGEN_XML_DIR)/index.xml
DOXYGEN_FLAGS?=		-q

SPHINX_FLAGS?=			-W --keep-going -q
SPHINX_FLAGS_DEFAULT=
SPHINX_SRC_DIR=			.
SPHINX_BUILD_DIR=		_build
SPHINX_HTML_FILE=	$(SPHINX_BUILD_DIR)/html/index.html

BIN_DIR=	../bin
EIL_CMD=	$(BIN_DIR)/eil-q
EIL_NAME!=			$(EIL_CMD) name
EIL_DESCRIPTION!=	$(EIL_CMD) description
EIL_COPYRIGHT!=		$(EIL_CMD) copyright_string
EIL_CODEOWNERS!=	$(EIL_CMD) code_owners
EIL_VERSION!=		$(EIL_CMD) version

BUILD_ENV=	env PROJECT_NAME="$(EIL_NAME)" \
				PROJECT_BRIEF="$(EIL_DESCRIPTION)" \
				PROJECT_COPYRIGHT="$(EIL_COPYRIGHT)" \
				PROJECT_AUTHORS="$(EIL_CODEOWNERS)" \
				PROJECT_RELEASE="$(EIL_VERSION)" \
				OUTPUT_DIRECTORY="$(DOXYGEN_OUTPUT_DIR)" \
				MAKE=$(MAKE)

.DEFAULT_GOAL=	all
.PHONY:	all clean

# create DOXYGEN_OUTPUT_DIR, where doxygen generates XML files
$(DOXYGEN_OUTPUT_DIR):
	mkdir $(DOXYGEN_OUTPUT_DIR)

# generate XML files from sources with doxygen
$(DOXYGEN_XML_FILE): $(DOXYGEN_OUTPUT_DIR)
	$(BUILD_ENV) $(DOXYGEN) $(DOXYGEN_FLAGS) $(DOXYGEN_CONF)
	$(SED) -i 's/LIB8STATIC_ALWAYS_INLINE/inline static/g' $(DOXYGEN_XML_DIR)/*.xml
	$(SED) -i 's/LIB8STATIC/inline static/g' $(DOXYGEN_XML_DIR)/*.xml

build-doxygen: $(DOXYGEN_XML_FILE)

$(SPHINX_HTML_FILE):
	$(BUILD_ENV) $(SPHINX) -M html $(SPHINX_SRC_DIR) $(SPHINX_BUILD_DIR) $(SPHINX_FLAGS_DEFAULT) $(SPHINX_FLAGS)

# generate HTML files with sphinx-build.
html: $(SPHINX_HTML_FILE)

clean:
	rm -rf ${DOXYGEN_OUTPUT_DIR} $(BUILD_DIR) doxygen.log

all: html
