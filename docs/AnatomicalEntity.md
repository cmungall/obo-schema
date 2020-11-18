
# Type: anatomical entity




URI: [oboschema:AnatomicalEntity](http://purl.obolibrary.org/oboschema/AnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantAnatomicalEntity],[PhysicalEntity],[PathologicalCellType],[LifeStage],[GrossPathologicalAnatomicalEntity],[GrossConstructedAnatomicalEntity],[EvolvedAnatomicalEntity],[ConstructedCellType],[LifeStage]<existence%20ends%20during%200..1-++[AnatomicalEntity],[LifeStage]<existence%20starts%20during%200..1-++[AnatomicalEntity],[AnatomicalEntity]<develops%20from%200..*-++[AnatomicalEntity],[AnatomicalEntity]<part%20of%200..1-++[AnatomicalEntity],[AnatomicalEntity]<subclass%20of%200..*-++[AnatomicalEntity],[AnatomicalEntity]^-[VariantAnatomicalEntity],[AnatomicalEntity]^-[PathologicalCellType],[AnatomicalEntity]^-[GrossPathologicalAnatomicalEntity],[AnatomicalEntity]^-[GrossConstructedAnatomicalEntity],[AnatomicalEntity]^-[EvolvedAnatomicalEntity],[AnatomicalEntity]^-[ConstructedCellType],[AnatomicalEntity]^-[AbormalAnatomicalEntity],[PhysicalEntity]^-[AnatomicalEntity],[AbormalAnatomicalEntity])

## Parents

 *  is_a: [PhysicalEntity](PhysicalEntity.md)

## Children

 * [AbormalAnatomicalEntity](AbormalAnatomicalEntity.md)
 * [ConstructedCellType](ConstructedCellType.md)
 * [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)
 * [GrossConstructedAnatomicalEntity](GrossConstructedAnatomicalEntity.md)
 * [GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)
 * [PathologicalCellType](PathologicalCellType.md)
 * [VariantAnatomicalEntity](VariantAnatomicalEntity.md)

## Referenced by class

 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[anatomical entity➞develops from](anatomical_entity_develops_from.md)*  <sub>0..*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[anatomical entity➞part of](anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[anatomical entity➞subclass of](anatomical_entity_subclass_of.md)*  <sub>0..*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **None** *[part of](part_of.md)*  <sub>OPT</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**

## Attributes


### Own

 * [anatomical entity➞develops from](anatomical_entity_develops_from.md)  <sub>0..*</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞part of](anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity➞subclass of](anatomical_entity_subclass_of.md)  <sub>0..*</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
