
# Type: species specific gross evolved anatomical entity




URI: [oboschema:SpeciesSpecificGrossEvolvedAnatomicalEntity](http://purl.obolibrary.org/oboschema/SpeciesSpecificGrossEvolvedAnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[LifeStage]<existence%20ends%20during%200..1-++[SpeciesSpecificGrossEvolvedAnatomicalEntity],[LifeStage]<existence%20starts%20during%200..1-++[SpeciesSpecificGrossEvolvedAnatomicalEntity],[SpeciesSpecificGrossEvolvedAnatomicalEntity]<develops%20from%200..1-++[SpeciesSpecificGrossEvolvedAnatomicalEntity],[SpeciesSpecificGrossEvolvedAnatomicalEntity]<part%20of%200..1-++[SpeciesSpecificGrossEvolvedAnatomicalEntity],[GrossEvolvedAnatomicalEntity]<subclass%20of%200..1-++[SpeciesSpecificGrossEvolvedAnatomicalEntity],[SpeciesSpecificGrossEvolvedAnatomicalEntity]uses%20-.->[SpeciesSpecific],[GrossEvolvedAnatomicalEntity]^-[SpeciesSpecificGrossEvolvedAnatomicalEntity],[SpeciesSpecific],[Species],[OrganismTaxon],[LifeStage],[GrossEvolvedAnatomicalEntity])

## Parents

 *  is_a: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)

## Uses Mixins

 *  mixin: [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

## Referenced by class

 *  **[SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)** *[species specific gross evolved anatomical entity➞develops from](species_specific_gross_evolved_anatomical_entity_develops_from.md)*  <sub>OPT</sub>  **[SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)**
 *  **[SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)** *[species specific gross evolved anatomical entity➞part of](species_specific_gross_evolved_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)**

## Attributes


### Own

 * [species specific gross evolved anatomical entity➞develops from](species_specific_gross_evolved_anatomical_entity_develops_from.md)  <sub>OPT</sub>
    * range: [SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)
 * [species specific gross evolved anatomical entity➞existence ends during](species_specific_gross_evolved_anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [species specific gross evolved anatomical entity➞existence starts during](species_specific_gross_evolved_anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [species specific gross evolved anatomical entity➞part of](species_specific_gross_evolved_anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)
 * [species specific gross evolved anatomical entity➞subclass of](species_specific_gross_evolved_anatomical_entity_subclass_of.md)  <sub>OPT</sub>
    * range: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species specific:

 * [species specific➞in taxon](species_specific_in_taxon.md)  <sub>OPT</sub>
    * range: [Species](Species.md)
