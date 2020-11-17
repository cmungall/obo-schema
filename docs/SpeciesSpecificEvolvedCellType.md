
# Type: species specific evolved cell type




URI: [oboschema:SpeciesSpecificEvolvedCellType](http://purl.obolibrary.org/oboschema/SpeciesSpecificEvolvedCellType)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[LifeStage]<existence%20ends%20during%200..1-++[SpeciesSpecificEvolvedCellType],[LifeStage]<existence%20starts%20during%200..1-++[SpeciesSpecificEvolvedCellType],[SpeciesSpecificEvolvedCellType]<develops%20from%200..1-++[SpeciesSpecificEvolvedCellType],[SpeciesSpecificEvolvedCellType]<part%20of%200..1-++[SpeciesSpecificEvolvedCellType],[SpeciesSpecificEvolvedCellType]<subclass%20of%200..1-++[SpeciesSpecificEvolvedCellType],[SpeciesSpecificEvolvedCellType]uses%20-.->[SpeciesSpecific],[EvolvedCellType]^-[SpeciesSpecificEvolvedCellType],[SpeciesSpecific],[Species],[OrganismTaxon],[LifeStage],[EvolvedCellType])

## Parents

 *  is_a: [EvolvedCellType](EvolvedCellType.md)

## Uses Mixins

 *  mixin: [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

## Referenced by class

 *  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)** *[species specific evolved cell type➞develops from](species_specific_evolved_cell_type_develops_from.md)*  <sub>OPT</sub>  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)**
 *  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)** *[species specific evolved cell type➞part of](species_specific_evolved_cell_type_part_of.md)*  <sub>OPT</sub>  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)**
 *  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)** *[species specific evolved cell type➞subclass of](species_specific_evolved_cell_type_subclass_of.md)*  <sub>OPT</sub>  **[SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)**

## Attributes


### Own

 * [species specific evolved cell type➞develops from](species_specific_evolved_cell_type_develops_from.md)  <sub>OPT</sub>
    * range: [SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)
 * [species specific evolved cell type➞existence ends during](species_specific_evolved_cell_type_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [species specific evolved cell type➞existence starts during](species_specific_evolved_cell_type_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [species specific evolved cell type➞part of](species_specific_evolved_cell_type_part_of.md)  <sub>OPT</sub>
    * range: [SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)
 * [species specific evolved cell type➞subclass of](species_specific_evolved_cell_type_subclass_of.md)  <sub>OPT</sub>
    * range: [SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species specific:

 * [species specific➞in taxon](species_specific_in_taxon.md)  <sub>OPT</sub>
    * range: [Species](Species.md)
