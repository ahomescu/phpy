
PYXBGEN = pyxbgen
PARSER_NAME = phc_xml_parser
PARSER_PY = $(PARSER_NAME).py

all: $(PARSER_PY)

$(PARSER_PY): phc-2.0.xsd
	$(PYXBGEN) -u $< -m $(PARSER_NAME)

.PHONY: clean

clean:
	rm -rf $(PARSER_PY) $(PARSER_NAME).pyc


