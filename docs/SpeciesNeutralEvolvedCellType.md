
# Type: species neutral evolved cell type




URI: [oboschema:SpeciesNeutralEvolvedCellType](http://purl.obolibrary.org/oboschema/SpeciesNeutralEvolvedCellType)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesNeutralLifeStage],[SpeciesNeutralLifeStage]<existence%20ends%20during%200..1-++[SpeciesNeutralEvolvedCellType],[SpeciesNeutralLifeStage]<existence%20starts%20during%200..1-++[SpeciesNeutralEvolvedCellType],[SpeciesNeutralEvolvedCellType]<develops%20from%200..1-++[SpeciesNeutralEvolvedCellType],[SpeciesNeutralEvolvedCellType]<part%20of%200..1-++[SpeciesNeutralEvolvedCellType],[SpeciesNeutralEvolvedCellType]<subclass%20of%200..1-++[SpeciesNeutralEvolvedCellType],[SpeciesNeutralEvolvedCellType]uses%20-.->[SpeciesNeutral],[EvolvedCellType]^-[SpeciesNeutralEvolvedCellType],[SpeciesNeutral],[OrganismTaxon],[EvolvedCellType],[BroadOrganismTaxon])

## Parents

 *  is_a: [EvolvedCellType](EvolvedCellType.md)

## Uses Mixins

 *  mixin: [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies

## Referenced by class

 *  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)** *[species neutral evolved cell type➞develops from](species_neutral_evolved_cell_type_develops_from.md)*  <sub>OPT</sub>  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)**
 *  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)** *[species neutral evolved cell type➞part of](species_neutral_evolved_cell_type_part_of.md)*  <sub>OPT</sub>  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)**
 *  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)** *[species neutral evolved cell type➞subclass of](species_neutral_evolved_cell_type_subclass_of.md)*  <sub>OPT</sub>  **[SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)**

## Attributes


### Own

 * [species neutral evolved cell type➞develops from](species_neutral_evolved_cell_type_develops_from.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)
 * [species neutral evolved cell type➞existence ends during](species_neutral_evolved_cell_type_existence_ends_during.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)
 * [species neutral evolved cell type➞existence starts during](species_neutral_evolved_cell_type_existence_starts_during.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)
 * [species neutral evolved cell type➞part of](species_neutral_evolved_cell_type_part_of.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)
 * [species neutral evolved cell type➞subclass of](species_neutral_evolved_cell_type_subclass_of.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species neutral:

 * [species neutral➞in taxon](species_neutral_in_taxon.md)  <sub>OPT</sub>
    * range: [BroadOrganismTaxon](BroadOrganismTaxon.md)
