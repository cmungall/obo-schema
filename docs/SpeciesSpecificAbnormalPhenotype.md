
# Type: species specific abnormal phenotype




URI: [oboschema:SpeciesSpecificAbnormalPhenotype](http://purl.obolibrary.org/oboschema/SpeciesSpecificAbnormalPhenotype)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecificAbnormalPhenotype]uses%20-.->[SpeciesSpecific],[AbnormalPhenotype]^-[SpeciesSpecificAbnormalPhenotype],[SpeciesSpecific],[OrganismTaxon],[AtomicPhenotypicFeature],[AbnormalPhenotype])

## Parents

 *  is_a: [AbnormalPhenotype](AbnormalPhenotype.md)

## Uses Mixins

 *  mixin: [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

## Attributes


### Inherited from abnormal phenotype:

 * [abnormal phenotype➞has part](abnormal_phenotype_has_part.md)  <sub>OPT</sub>
    * range: [AtomicPhenotypicFeature](AtomicPhenotypicFeature.md)

### Mixed in from organismal:

 * [organismal➞in taxon](organismal_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
