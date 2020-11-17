
# Type: species neutral gross evolved anatomical entity




URI: [oboschema:SpeciesNeutralGrossEvolvedAnatomicalEntity](http://purl.obolibrary.org/oboschema/SpeciesNeutralGrossEvolvedAnatomicalEntity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SpeciesNeutralLifeStage],[SpeciesNeutralLifeStage]<existence%20ends%20during%200..1-++[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralLifeStage]<existence%20starts%20during%200..1-++[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralGrossEvolvedAnatomicalEntity]<develops%20from%200..1-++[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralGrossEvolvedAnatomicalEntity]<part%20of%200..1-++[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralGrossEvolvedAnatomicalEntity]<subclass%20of%200..1-++[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutralGrossEvolvedAnatomicalEntity]uses%20-.->[SpeciesNeutral],[GrossEvolvedAnatomicalEntity]^-[SpeciesNeutralGrossEvolvedAnatomicalEntity],[SpeciesNeutral],[OrganismTaxon],[GrossEvolvedAnatomicalEntity],[BroadOrganismTaxon])

## Parents

 *  is_a: [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)

## Uses Mixins

 *  mixin: [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies

## Referenced by class

 *  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)** *[species neutral gross evolved anatomical entity➞develops from](species_neutral_gross_evolved_anatomical_entity_develops_from.md)*  <sub>OPT</sub>  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)**
 *  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)** *[species neutral gross evolved anatomical entity➞part of](species_neutral_gross_evolved_anatomical_entity_part_of.md)*  <sub>OPT</sub>  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)**
 *  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)** *[species neutral gross evolved anatomical entity➞subclass of](species_neutral_gross_evolved_anatomical_entity_subclass_of.md)*  <sub>OPT</sub>  **[SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)**

## Attributes


### Own

 * [species neutral gross evolved anatomical entity➞develops from](species_neutral_gross_evolved_anatomical_entity_develops_from.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)
 * [species neutral gross evolved anatomical entity➞existence ends during](species_neutral_gross_evolved_anatomical_entity_existence_ends_during.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)
 * [species neutral gross evolved anatomical entity➞existence starts during](species_neutral_gross_evolved_anatomical_entity_existence_starts_during.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)
 * [species neutral gross evolved anatomical entity➞part of](species_neutral_gross_evolved_anatomical_entity_part_of.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)
 * [species neutral gross evolved anatomical entity➞subclass of](species_neutral_gross_evolved_anatomical_entity_subclass_of.md)  <sub>OPT</sub>
    * range: [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from species neutral:

 * [species neutral➞in taxon](species_neutral_in_taxon.md)  <sub>OPT</sub>
    * range: [BroadOrganismTaxon](BroadOrganismTaxon.md)
