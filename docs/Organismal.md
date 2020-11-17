
# Type: organismal




URI: [oboschema:Organismal](http://purl.obolibrary.org/oboschema/Organismal)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecific],[SpeciesNeutral],[OrganismTaxon]<never%20in%20taxon%200..1-++[Organismal],[OrganismTaxon]<in%20taxon%200..1-++[Organismal],[Exposure]uses%20-.->[Organismal],[Disease]uses%20-.->[Organismal],[ChemicalEntity]uses%20-.->[Organismal],[BiologicalProcessOrMolecularActivity]uses%20-.->[Organismal],[AtomicTraitOrPhenotypicFeature]uses%20-.->[Organismal],[AbnormalPhenotype]uses%20-.->[Organismal],[Organismal]^-[SpeciesSpecific],[Organismal]^-[SpeciesNeutral],[OrganismTaxon],[Exposure],[Disease],[ChemicalEntity],[BiologicalProcessOrMolecularActivity],[AtomicTraitOrPhenotypicFeature],[AbnormalPhenotype])

## Children

 * [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies
 * [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

## Mixin for

 * [AbnormalPhenotype](AbnormalPhenotype.md) (mixin) 
 * [AtomicTraitOrPhenotypicFeature](AtomicTraitOrPhenotypicFeature.md) (mixin) 
 * [BiologicalProcessOrMolecularActivity](BiologicalProcessOrMolecularActivity.md) (mixin) 
 * [ChemicalEntity](ChemicalEntity.md) (mixin) 
 * [Disease](Disease.md) (mixin) 
 * [Exposure](Exposure.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [organismal➞in taxon](organismal_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
