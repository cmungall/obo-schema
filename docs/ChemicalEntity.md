
# Type: chemical entity




URI: [oboschema:ChemicalEntity](http://purl.obolibrary.org/oboschema/ChemicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEntity],[Organismal],[OrganismTaxon],[MixtureOfChemicalEntities],[ChemicalEntityAtomicPhenotypicFeature],[ChemicalEntityAtomicPhenotypicFeature]++-%20characteristic%20of%200..1>[ChemicalEntity],[MixtureOfChemicalEntities]++-%20has%20part%200..1>[ChemicalEntity],[ChemicalEntity]uses%20-.->[Organismal],[PhysicalEntity]^-[ChemicalEntity])

## Parents

 *  is_a: [PhysicalEntity](PhysicalEntity.md)

## Uses Mixins

 *  mixin: [Organismal](Organismal.md)

## Referenced by class

 *  **[ChemicalEntityAtomicPhenotypicFeature](ChemicalEntityAtomicPhenotypicFeature.md)** *[chemical entity atomic phenotypic feature➞characteristic of](chemical_entity_atomic_phenotypic_feature_characteristic_of.md)*  <sub>OPT</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[MixtureOfChemicalEntities](MixtureOfChemicalEntities.md)** *[mixture of chemical entities➞has part](mixture_of_chemical_entities_has_part.md)*  <sub>OPT</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Mixed in from organismal:

 * [organismal➞in taxon](organismal_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
