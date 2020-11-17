EXTS = _datamodel.py .graphql .schema.json .owl.ttl -docs .shex

all: $(patsubst %,src/schema/obo-schema%, $(EXTS)) pngs

pngs: src/schema/obo-schema.owl.png

test: all

src/schema/%_datamodel.py: src/schema/%.yaml
	gen-py-classes $< > $@
src/schema/%.graphql: src/schema/%.yaml
	gen-graphql $< > $@
src/schema/%.schema.json: src/schema/%.yaml
	gen-json-schema -t transaction $< > $@
src/schema/%.shex: src/schema/%.yaml
	gen-shex $< > $@
src/schema/%.csv: src/schema/%.yaml
	gen-csv $< > $@
src/schema/%.owl.ttl: src/schema/%.yaml
	gen-owl $< > $@
.PRECIOUS: src/schema/%.owl.ttl
src/schema/%.owl.json: src/schema/%.owl.ttl
	robot relax -i $< -o $@
src/schema/%.owl.json: src/schema/%.owl.ttl
	robot relax -i $< -o $@
src/schema/%.owl.png: src/schema/%.owl.json
	og2dot.js -t png -o $@ $<
src/schema/%.ttl: src/schema/%.owl
	cp $< $@
src/schema/%-docs: src/schema/%.yaml
	pipenv run gen-markdown --dir $@ $<

deploy-docs:
	cp src/schema/obo-schema-docs/*md docs/


OWLSRC = src/schema/obo-schema.owl.ttl
# scans wikidata for potential matches; the result is a sub-ontology
matches/close-matches.ttl: $(OWLSRC)
	wd-ontomatch -d ontomatcher -i $< match_all && cp CACHE.ttl $@

matches/close-matches-enhanced.ttl: matches/close-matches.ttl
	robot query -i $< -u sparql/wd-add-category.ru -o $@

matches/matches.tsv: matches/close-matches.ttl  $(OWLSRC)
	rdfmatch -p obo-schema -w matches/weights.pro  -i prefixes.ttl -i $(OWLSRC) -G matches/matches.ttl -d index -i $< match > $@
nomatches.tsv: close-matches.ttl bosch.ttl
	rdfmatch --label_only -p bosch --match_prefix wd -w conf/bosch_weights.pro  -i prefixes.ttl -i bosch.ttl -G matches.ttl -d index -i $< nomatch > $@

