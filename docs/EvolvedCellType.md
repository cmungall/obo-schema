
# Type: evolved cell type




URI: [oboschema:EvolvedCellType](http://purl.obolibrary.org/oboschema/EvolvedCellType)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesSpecificEvolvedCellType],[SpeciesNeutralEvolvedCellType],[PathologicalCellType],[LifeStage],[GrossEvolvedAnatomicalEntity],[EvolvedCellType]<develops%20from%200..1-++[EvolvedCellType],[GrossEvolvedAnatomicalEntity]<part%20of%200..1-++[EvolvedCellType],[EvolvedCellType]<subclass%20of%200..1-++[EvolvedCellType],[ConstructedCellType]++-%20analog%20of%200..1>[EvolvedCellType],[PathologicalCellType]++-%20analog%20of%200..1>[EvolvedCellType],[EvolvedCellType]^-[SpeciesSpecificEvolvedCellType],[EvolvedCellType]^-[SpeciesNeutralEvolvedCellType],[EvolvedAnatomicalEntity]^-[EvolvedCellType],[EvolvedAnatomicalEntity],[ConstructedCellType])

## Parents

 *  is_a: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)

## Children

 * [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)
 * [SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)

## Referenced by class

 *  **[ConstructedCellType](ConstructedCellType.md)** *[constructed cell type➞analog of](constructed_cell_type_analog_of.md)*  <sub>OPT</sub>  **[EvolvedCellType](EvolvedCellType.md)**
 *  **[EvolvedCellType](EvolvedCellType.md)** *[evolved cell type➞develops from](evolved_cell_type_develops_from.md)*  <sub>OPT</sub>  **[EvolvedCellType](EvolvedCellType.md)**
 *  **[EvolvedCellType](EvolvedCellType.md)** *[evolved cell type➞subclass of](evolved_cell_type_subclass_of.md)*  <sub>OPT</sub>  **[EvolvedCellType](EvolvedCellType.md)**
 *  **[PathologicalCellType](PathologicalCellType.md)** *[pathological cell type➞analog of](pathological_cell_type_analog_of.md)*  <sub>OPT</sub>  **[EvolvedCellType](EvolvedCellType.md)**

## Attributes


### Own

 * [evolved cell type➞develops from](evolved_cell_type_develops_from.md)  <sub>OPT</sub>
    * range: [EvolvedCellType](EvolvedCellType.md)
 * [evolved cell type➞part of](evolved_cell_type_part_of.md)  <sub>OPT</sub>
    * range: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)
 * [evolved cell type➞subclass of](evolved_cell_type_subclass_of.md)  <sub>OPT</sub>
    * range: [EvolvedCellType](EvolvedCellType.md)

### Inherited from evolved anatomical entity:

 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
