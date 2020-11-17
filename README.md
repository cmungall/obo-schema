# Map of OBO schema

This repo includes an experimehtal schema for OBO classes

Schema: [obo-schema](http://cmungall.github.io/obo-schema)

## Basic idea

## Schema

Browse the schema here: [http://cmungall.github.io/obo-schema](http://cmungall.github.io/obo-schema)

Realist pedants be advised to assume the suffix 'species', 'class', or 'type' on the end of these (meta)class names

See the [src/schema/](src/schema/) folder

The source is in YAML (biolinkml)

Currently the main derived artefacts of interest are:

 - [JSON Schema](src/schema/obo-schema.schema.json)
 - [ShEx](src/schema/obo-schema.shex)
 - [Python dataclasses](src/schema/obo-schema_datamodel.py)

With care, you also see:

 - [OWL](src/schema/obo-schema.owl.ttl) -- note this should be read as a meta-ontology by OBO people

## TODO

lots
