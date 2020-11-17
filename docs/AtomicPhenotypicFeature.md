
# Type: atomic phenotypic feature




URI: [oboschema:AtomicPhenotypicFeature](http://purl.obolibrary.org/oboschema/AtomicPhenotypicFeature)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntityOrProcess],[OrganismTaxon],[ChemicalEntityAtomicPhenotypicFeature],[CharacteristicValue],[BiologicalProcessAtomicPhenotypicFeature],[AtomicTraitOrPhenotypicFeature],[PhysicalEntityOrProcess]<characteristic%20of%200..1-++[AtomicPhenotypicFeature],[CharacteristicValue]<subclass%20of%200..1-++[AtomicPhenotypicFeature],[AbnormalPhenotype]++-%20has%20part%200..1>[AtomicPhenotypicFeature],[AtomicPhenotypicFeature]^-[ChemicalEntityAtomicPhenotypicFeature],[AtomicPhenotypicFeature]^-[BiologicalProcessAtomicPhenotypicFeature],[AtomicPhenotypicFeature]^-[AnatomicalAtomicPhenotypicFeature],[AtomicTraitOrPhenotypicFeature]^-[AtomicPhenotypicFeature],[AnatomicalAtomicPhenotypicFeature],[AbnormalPhenotype])

## Parents

 *  is_a: [AtomicTraitOrPhenotypicFeature](AtomicTraitOrPhenotypicFeature.md)

## Children

 * [AnatomicalAtomicPhenotypicFeature](AnatomicalAtomicPhenotypicFeature.md)
 * [BiologicalProcessAtomicPhenotypicFeature](BiologicalProcessAtomicPhenotypicFeature.md)
 * [ChemicalEntityAtomicPhenotypicFeature](ChemicalEntityAtomicPhenotypicFeature.md)

## Referenced by class

 *  **[AbnormalPhenotype](AbnormalPhenotype.md)** *[abnormal phenotype➞has part](abnormal_phenotype_has_part.md)*  <sub>OPT</sub>  **[AtomicPhenotypicFeature](AtomicPhenotypicFeature.md)**
 *  **None** *[has part](has_part.md)*  <sub>OPT</sub>  **[AtomicPhenotypicFeature](AtomicPhenotypicFeature.md)**

## Attributes


### Own

 * [atomic phenotypic feature➞characteristic of](atomic_phenotypic_feature_characteristic_of.md)  <sub>OPT</sub>
    * range: [PhysicalEntityOrProcess](PhysicalEntityOrProcess.md)
 * [atomic phenotypic feature➞subclass of](atomic_phenotypic_feature_subclass_of.md)  <sub>OPT</sub>
    * range: [CharacteristicValue](CharacteristicValue.md)
