
# Type: species specific life stage




URI: [oboschema:SpeciesSpecificLifeStage](http://purl.obolibrary.org/oboschema/SpeciesSpecificLifeStage)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecificLifeStage]uses%20-.->[SpeciesSpecific],[LifeStage]^-[SpeciesSpecificLifeStage],[SpeciesSpecific],[Species],[OrganismTaxon],[LifeStage])

## Parents

 *  is_a: [LifeStage](LifeStage.md)

## Uses Mixins

 *  mixin: [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

## Attributes


### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species specific:

 * [species specific➞in taxon](species_specific_in_taxon.md)  <sub>OPT</sub>
    * range: [Species](Species.md)
