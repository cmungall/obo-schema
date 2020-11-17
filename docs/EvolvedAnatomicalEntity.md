
# Type: evolved anatomical entity




URI: [oboschema:EvolvedAnatomicalEntity](http://purl.obolibrary.org/oboschema/EvolvedAnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[LifeStage],[GrossEvolvedAnatomicalEntity],[EvolvedCellType],[EvolvedAnatomicalEntity]<develops%20from%200..1-++[EvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]<part%20of%200..1-++[EvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]<subclass%20of%200..1-++[EvolvedAnatomicalEntity],[AnatomicalAtomicPhenotypicFeature]++-%20characteristic%20of%200..1>[EvolvedAnatomicalEntity],[CellularEvolvedAnatomicalEntity]++-%20part%20of%200..1>[EvolvedAnatomicalEntity],[GrossEvolvedAnatomicalEntity]++-%20part%20of%200..1>[EvolvedAnatomicalEntity],[GrossEvolvedAnatomicalEntity]++-%20subclass%20of%200..1>[EvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]uses%20-.->[Evolved],[EvolvedAnatomicalEntity]^-[GrossEvolvedAnatomicalEntity],[EvolvedAnatomicalEntity]^-[EvolvedCellType],[EvolvedAnatomicalEntity]^-[CellularEvolvedAnatomicalEntity],[AnatomicalEntity]^-[EvolvedAnatomicalEntity],[Evolved],[CellularEvolvedAnatomicalEntity],[AnatomicalEntity],[AnatomicalAtomicPhenotypicFeature])

## Parents

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md)

## Uses Mixins

 *  mixin: [Evolved](Evolved.md)

## Children

 * [CellularEvolvedAnatomicalEntity](CellularEvolvedAnatomicalEntity.md)
 * [EvolvedCellType](EvolvedCellType.md)
 * [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)

## Referenced by class

 *  **[AnatomicalAtomicPhenotypicFeature](AnatomicalAtomicPhenotypicFeature.md)** *[anatomical atomic phenotypic feature➞characteristic of](anatomical_atomic_phenotypic_feature_characteristic_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[CellularEvolvedAnatomicalEntity](CellularEvolvedAnatomicalEntity.md)** *[cellular evolved anatomical entity➞part of](cellular_evolved_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)** *[evolved anatomical entity➞develops from](evolved_anatomical_entity_develops_from.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)** *[evolved anatomical entity➞part of](evolved_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)** *[evolved anatomical entity➞subclass of](evolved_anatomical_entity_subclass_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)** *[gross evolved anatomical entity➞part of](gross_evolved_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**
 *  **[GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)** *[gross evolved anatomical entity➞subclass of](gross_evolved_anatomical_entity_subclass_of.md)*  <sub>OPT</sub>  **[EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)**

## Attributes


### Own

 * [evolved anatomical entity➞develops from](evolved_anatomical_entity_develops_from.md)  <sub>OPT</sub>
    * range: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)
 * [evolved anatomical entity➞part of](evolved_anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)
 * [evolved anatomical entity➞subclass of](evolved_anatomical_entity_subclass_of.md)  <sub>OPT</sub>
    * range: [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)

### Inherited from anatomical entity:

 * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
