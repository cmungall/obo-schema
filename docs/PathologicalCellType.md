
# Type: pathological cell type




URI: [oboschema:PathologicalCellType](http://purl.obolibrary.org/oboschema/PathologicalCellType)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[EvolvedCellType]<analog%20of%200..1-++[PathologicalCellType],[PathologicalCellType]<part%20of%200..1-++[PathologicalCellType],[PathologicalCellType]<subclass%20of%200..*-++[PathologicalCellType],[PathologicalCellType]uses%20-.->[Abnormal],[AnatomicalEntity]^-[PathologicalCellType],[LifeStage],[EvolvedCellType],[AnatomicalEntity],[Abnormal])

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md)

## Uses Mixins

 *  mixin: [Abnormal](Abnormal.md)

## Referenced by class

 *  **[PathologicalCellType](PathologicalCellType.md)** *[pathological cell type➞part of](pathological_cell_type_part_of.md)*  <sub>OPT</sub>  **[PathologicalCellType](PathologicalCellType.md)**
 *  **[PathologicalCellType](PathologicalCellType.md)** *[pathological cell type➞subclass of](pathological_cell_type_subclass_of.md)*  <sub>0..*</sub>  **[PathologicalCellType](PathologicalCellType.md)**

## Attributes


### Own

 * [pathological cell type➞analog of](pathological_cell_type_analog_of.md)  <sub>OPT</sub>
    * range: [EvolvedCellType](EvolvedCellType.md)
 * [pathological cell type➞part of](pathological_cell_type_part_of.md)  <sub>OPT</sub>
    * range: [PathologicalCellType](PathologicalCellType.md)
 * [pathological cell type➞subclass of](pathological_cell_type_subclass_of.md)  <sub>0..*</sub>
    * range: [PathologicalCellType](PathologicalCellType.md)

### Inherited from anatomical entity:

 * [anatomical entity➞develops from](anatomical_entity_develops_from.md)  <sub>0..*</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | abnormal cell type |

