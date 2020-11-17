
# Type: gross pathological anatomical entity




URI: [oboschema:GrossPathologicalAnatomicalEntity](http://purl.obolibrary.org/oboschema/GrossPathologicalAnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[LifeStage],[GrossEvolvedAnatomicalEntity]<pathological%20of%200..1-++[GrossPathologicalAnatomicalEntity],[GrossPathologicalAnatomicalEntity]<part%20of%200..1-++[GrossPathologicalAnatomicalEntity],[GrossPathologicalAnatomicalEntity]<subclass%20of%200..*-++[GrossPathologicalAnatomicalEntity],[GrossPathologicalAnatomicalEntity]uses%20-.->[Abnormal],[AnatomicalEntity]^-[GrossPathologicalAnatomicalEntity],[GrossEvolvedAnatomicalEntity],[AnatomicalEntity],[Abnormal])

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md)

## Uses Mixins

 *  mixin: [Abnormal](Abnormal.md)

## Referenced by class

 *  **[GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)** *[gross pathological anatomical entity➞part of](gross_pathological_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)**
 *  **[GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)** *[gross pathological anatomical entity➞subclass of](gross_pathological_anatomical_entity_subclass_of.md)*  <sub>0..*</sub>  **[GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)**

## Attributes


### Own

 * [gross pathological anatomical entity➞part of](gross_pathological_anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)
 * [gross pathological anatomical entity➞pathological of](gross_pathological_anatomical_entity_pathological_of.md)  <sub>OPT</sub>
    * range: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)
 * [gross pathological anatomical entity➞subclass of](gross_pathological_anatomical_entity_subclass_of.md)  <sub>0..*</sub>
    * range: [GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)

### Inherited from anatomical entity:

 * [anatomical entity➞develops from](anatomical_entity_develops_from.md)  <sub>0..*</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
