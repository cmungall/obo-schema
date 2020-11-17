
# Type: abnormal phenotype




URI: [oboschema:AbnormalPhenotype](http://purl.obolibrary.org/oboschema/AbnormalPhenotype)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecificAbnormalPhenotype],[SpeciesNeutralAbnormalPhenotype],[Organismal],[OrganismTaxon],[AtomicPhenotypicFeature],[AtomicPhenotypicFeature]<has%20part%200..1-++[AbnormalPhenotype],[AbnormalPhenotype]uses%20-.->[Abnormal],[AbnormalPhenotype]uses%20-.->[Organismal],[AbnormalPhenotype]^-[SpeciesSpecificAbnormalPhenotype],[AbnormalPhenotype]^-[SpeciesNeutralAbnormalPhenotype],[Abnormal])

## Uses Mixins

 *  mixin: [Abnormal](Abnormal.md)
 *  mixin: [Organismal](Organismal.md)

## Children

 * [SpeciesNeutralAbnormalPhenotype](SpeciesNeutralAbnormalPhenotype.md)
 * [SpeciesSpecificAbnormalPhenotype](SpeciesSpecificAbnormalPhenotype.md)

## Referenced by class


## Attributes


### Own

 * [abnormal phenotype➞has part](abnormal_phenotype_has_part.md)  <sub>OPT</sub>
    * range: [AtomicPhenotypicFeature](AtomicPhenotypicFeature.md)

### Mixed in from organismal:

 * [organismal➞in taxon](organismal_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
