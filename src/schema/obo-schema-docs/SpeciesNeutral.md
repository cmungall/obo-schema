
# Type: species neutral


may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies

URI: [oboschema:SpeciesNeutral](http://purl.obolibrary.org/oboschema/SpeciesNeutral)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[BroadOrganismTaxon]<in%20taxon%200..1-++[SpeciesNeutral],[SpeciesNeutralLifeStage]uses%20-.->[SpeciesNeutral],[SpeciesNeutralGrossEvolvedAnatomicalEntity]uses%20-.->[SpeciesNeutral],[SpeciesNeutralEvolvedCellType]uses%20-.->[SpeciesNeutral],[SpeciesNeutralAbnormalPhenotype]uses%20-.->[SpeciesNeutral],[Organismal]^-[SpeciesNeutral],[SpeciesNeutralLifeStage],[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralEvolvedCellType],[SpeciesNeutralAbnormalPhenotype],[Organismal],[OrganismTaxon],[BroadOrganismTaxon])

## Parents

 *  is_a: [Organismal](Organismal.md)

## Mixin for

 * [SpeciesNeutralAbnormalPhenotype](SpeciesNeutralAbnormalPhenotype.md) (mixin) 
 * [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md) (mixin) 
 * [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md) (mixin) 
 * [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md) (mixin) 

## Referenced by class


## Attributes


### Own

 * [species neutral➞in taxon](species_neutral_in_taxon.md)  <sub>OPT</sub>
    * range: [BroadOrganismTaxon](BroadOrganismTaxon.md)

### Inherited from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
