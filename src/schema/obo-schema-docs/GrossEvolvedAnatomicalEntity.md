
# Type: gross evolved anatomical entity




URI: [oboschema:GrossEvolvedAnatomicalEntity](http://purl.obolibrary.org/oboschema/GrossEvolvedAnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecificGrossEvolvedAnatomicalEntity],[SpeciesNeutralGrossEvolvedAnatomicalEntity],[LifeStage],[GrossPathologicalAnatomicalEntity],[GrossEvolvedAnatomicalEntity]<develops%20from%200..*-++[GrossEvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]<part%20of%200..1-++[GrossEvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]<subclass%20of%200..*-++[GrossEvolvedAnatomicalEntity],[EvolvedCellType]++-%20part%20of%200..1>[GrossEvolvedAnatomicalEntity],[GrossConstructedAnatomicalEntity]++-%20analog%20of%200..1>[GrossEvolvedAnatomicalEntity],[GrossPathologicalAnatomicalEntity]++-%20pathological%20of%200..1>[GrossEvolvedAnatomicalEntity],[SpeciesSpecificGrossEvolvedAnatomicalEntity]++-%20subclass%20of%200..*>[GrossEvolvedAnatomicalEntity],[GrossEvolvedAnatomicalEntity]^-[SpeciesSpecificGrossEvolvedAnatomicalEntity],[GrossEvolvedAnatomicalEntity]^-[SpeciesNeutralGrossEvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]^-[GrossEvolvedAnatomicalEntity],[GrossConstructedAnatomicalEntity],[EvolvedCellType],[EvolvedAnatomicalEntity])

## Parents

 *  is_a: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)

## Children

 * [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)
 * [SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)

## Referenced by class

 *  **[EvolvedCellType](EvolvedCellType.md)** *[evolved cell type➞part of](evolved_cell_type_part_of.md)*  <sub>OPT</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**
 *  **[GrossConstructedAnatomicalEntity](GrossConstructedAnatomicalEntity.md)** *[gross constructed anatomical entity➞analog of](gross_constructed_anatomical_entity_analog_of.md)*  <sub>OPT</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**
 *  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)** *[gross evolved anatomical entity➞develops from](gross_evolved_anatomical_entity_develops_from.md)*  <sub>0..*</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**
 *  **[GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)** *[gross pathological anatomical entity➞pathological of](gross_pathological_anatomical_entity_pathological_of.md)*  <sub>OPT</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**
 *  **None** *[pathological of](pathological_of.md)*  <sub>OPT</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**
 *  **[SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)** *[species specific gross evolved anatomical entity➞subclass of](species_specific_gross_evolved_anatomical_entity_subclass_of.md)*  <sub>0..*</sub>  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)**

## Attributes


### Own

 * [gross evolved anatomical entity➞develops from](gross_evolved_anatomical_entity_develops_from.md)  <sub>0..*</sub>
    * range: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)
 * [gross evolved anatomical entity➞part of](gross_evolved_anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)
 * [gross evolved anatomical entity➞subclass of](gross_evolved_anatomical_entity_subclass_of.md)  <sub>0..*</sub>
    * range: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)

### Inherited from evolved anatomical entity:

 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
