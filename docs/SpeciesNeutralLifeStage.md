
# Type: species neutral life stage




URI: [oboschema:SpeciesNeutralLifeStage](http://purl.obolibrary.org/oboschema/SpeciesNeutralLifeStage)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesNeutralEvolvedCellType]++-%20existence%20ends%20during%200..1>[SpeciesNeutralLifeStage],[SpeciesNeutralEvolvedCellType]++-%20existence%20starts%20during%200..1>[SpeciesNeutralLifeStage],[SpeciesNeutralGrossEvolvedAnatomicalEntity]++-%20existence%20ends%20during%200..1>[SpeciesNeutralLifeStage],[SpeciesNeutralGrossEvolvedAnatomicalEntity]++-%20existence%20starts%20during%200..1>[SpeciesNeutralLifeStage],[SpeciesNeutralLifeStage]uses%20-.->[SpeciesNeutral],[LifeStage]^-[SpeciesNeutralLifeStage],[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralEvolvedCellType],[SpeciesNeutral],[OrganismTaxon],[LifeStage],[BroadOrganismTaxon])

## Parents

 *  is_a: [LifeStage](LifeStage.md)

## Uses Mixins

 *  mixin: [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies

## Referenced by class

 *  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)** *[species neutral evolved cell type➞existence ends during](species_neutral_evolved_cell_type_existence_ends_during.md)*  <sub>OPT</sub>  **[SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)**
 *  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)** *[species neutral evolved cell type➞existence starts during](species_neutral_evolved_cell_type_existence_starts_during.md)*  <sub>OPT</sub>  **[SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)**
 *  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)** *[species neutral gross evolved anatomical entity➞existence ends during](species_neutral_gross_evolved_anatomical_entity_existence_ends_during.md)*  <sub>OPT</sub>  **[SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)**
 *  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)** *[species neutral gross evolved anatomical entity➞existence starts during](species_neutral_gross_evolved_anatomical_entity_existence_starts_during.md)*  <sub>OPT</sub>  **[SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)**

## Attributes


### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species neutral:

 * [species neutral➞in taxon](species_neutral_in_taxon.md)  <sub>OPT</sub>
    * range: [BroadOrganismTaxon](BroadOrganismTaxon.md)
