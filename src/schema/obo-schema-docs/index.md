
# Obo-Schema schema


A high level map of OBO classes and how they connect


### Classes

 * [AbnormalPhenotype](AbnormalPhenotype.md)
    * [SpeciesNeutralAbnormalPhenotype](SpeciesNeutralAbnormalPhenotype.md)
    * [SpeciesSpecificAbnormalPhenotype](SpeciesSpecificAbnormalPhenotype.md)
 * [AtomicTraitOrPhenotypicFeature](AtomicTraitOrPhenotypicFeature.md)
    * [AtomicPhenotypicFeature](AtomicPhenotypicFeature.md)
       * [AnatomicalAtomicPhenotypicFeature](AnatomicalAtomicPhenotypicFeature.md)
       * [BiologicalProcessAtomicPhenotypicFeature](BiologicalProcessAtomicPhenotypicFeature.md)
       * [ChemicalEntityAtomicPhenotypicFeature](ChemicalEntityAtomicPhenotypicFeature.md)
    * [AtomicTrait](AtomicTrait.md)
 * [Characteristic](Characteristic.md)
    * [CharacteristicAttribute](CharacteristicAttribute.md)
    * [CharacteristicValue](CharacteristicValue.md)
 * [Disease](Disease.md)
 * [Entity](Entity.md)
    * [PhysicalEntityOrProcess](PhysicalEntityOrProcess.md)
       * [Occurrent](Occurrent.md)
          * [LifeStage](LifeStage.md)
             * [SpeciesNeutralLifeStage](SpeciesNeutralLifeStage.md)
             * [SpeciesSpecificLifeStage](SpeciesSpecificLifeStage.md)
       * [PhysicalEntity](PhysicalEntity.md)
          * [AnatomicalEntity](AnatomicalEntity.md)
             * [AbormalAnatomicalEntity](AbormalAnatomicalEntity.md)
             * [ConstructedCellType](ConstructedCellType.md)
             * [EvolvedAnatomicalEntity](EvolvedAnatomicalEntity.md)
                * [CellularEvolvedAnatomicalEntity](CellularEvolvedAnatomicalEntity.md)
                * [EvolvedCellType](EvolvedCellType.md)
                   * [SpeciesNeutralEvolvedCellType](SpeciesNeutralEvolvedCellType.md)
                   * [SpeciesSpecificEvolvedCellType](SpeciesSpecificEvolvedCellType.md)
                * [GrossEvolvedAnatomicalEntity](GrossEvolvedAnatomicalEntity.md)
                   * [SpeciesNeutralGrossEvolvedAnatomicalEntity](SpeciesNeutralGrossEvolvedAnatomicalEntity.md)
                   * [SpeciesSpecificGrossEvolvedAnatomicalEntity](SpeciesSpecificGrossEvolvedAnatomicalEntity.md)
             * [GrossConstructedAnatomicalEntity](GrossConstructedAnatomicalEntity.md)
             * [GrossPathologicalAnatomicalEntity](GrossPathologicalAnatomicalEntity.md)
             * [PathologicalCellType](PathologicalCellType.md)
             * [VariantAnatomicalEntity](VariantAnatomicalEntity.md)
          * [ChemicalEntity](ChemicalEntity.md)
          * [PlanetaryEntity](PlanetaryEntity.md)
       * [Process](Process.md)
          * [BiologicalProcessOrMolecularActivity](BiologicalProcessOrMolecularActivity.md)
             * [BiologicalProcess](BiologicalProcess.md)
             * [MolecularActivity](MolecularActivity.md)
          * [EnvironmentalProcess](EnvironmentalProcess.md)
          * [Exposure](Exposure.md)
          * [PathologicalProcess](PathologicalProcess.md)
 * [Information](Information.md)
    * [OntologyAxiom](OntologyAxiom.md)
    * [Publication](Publication.md)
 * [MixtureOfChemicalEntities](MixtureOfChemicalEntities.md)
    * [Food](Food.md)
 * [OrganismTaxon](OrganismTaxon.md)
    * [BroadOrganismTaxon](BroadOrganismTaxon.md)
    * [Species](Species.md)
 * [Unit](Unit.md)

### Mixins

 * [Abnormal](Abnormal.md)
 * [Constructed](Constructed.md)
 * [Evolved](Evolved.md)
 * [NonOrganismal](NonOrganismal.md) - an entity or class that is not a part or derived from an organism.
 * [Organismal](Organismal.md)
    * [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies
    * [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus
 * [Origin](Origin.md)
    * [Abnormal](Abnormal.md)
    * [Constructed](Constructed.md)
    * [Evolved](Evolved.md)
    * [Variant](Variant.md)
 * [SpeciesNeutral](SpeciesNeutral.md) - may still be specific to a broader taxonomic grouping, e.g. metazoa. Must explicitly group other ontologies
 * [SpeciesSpecific](SpeciesSpecific.md) - species specific may also be applicable at broader levels, e.g. genus

### Slots

 * [analog of](analog_of.md)
    * [constructed cell type➞analog of](constructed_cell_type_analog_of.md)
    * [gross constructed anatomical entity➞analog of](gross_constructed_anatomical_entity_analog_of.md)
    * [pathological cell type➞analog of](pathological_cell_type_analog_of.md)
 * [characteristic of](characteristic_of.md)
    * [atomic phenotypic feature➞characteristic of](atomic_phenotypic_feature_characteristic_of.md)
       * [anatomical atomic phenotypic feature➞characteristic of](anatomical_atomic_phenotypic_feature_characteristic_of.md)
       * [biological process atomic phenotypic feature➞characteristic of](biological_process_atomic_phenotypic_feature_characteristic_of.md)
       * [chemical entity atomic phenotypic feature➞characteristic of](chemical_entity_atomic_phenotypic_feature_characteristic_of.md)
    * [atomic trait➞characteristic of](atomic_trait_characteristic_of.md)
 * [develops from](develops_from.md)
    * [anatomical entity➞develops from](anatomical_entity_develops_from.md)
       * [evolved anatomical entity➞develops from](evolved_anatomical_entity_develops_from.md)
          * [evolved cell type➞develops from](evolved_cell_type_develops_from.md)
             * [species neutral evolved cell type➞develops from](species_neutral_evolved_cell_type_develops_from.md)
             * [species specific evolved cell type➞develops from](species_specific_evolved_cell_type_develops_from.md)
          * [gross evolved anatomical entity➞develops from](gross_evolved_anatomical_entity_develops_from.md)
             * [species neutral gross evolved anatomical entity➞develops from](species_neutral_gross_evolved_anatomical_entity_develops_from.md)
             * [species specific gross evolved anatomical entity➞develops from](species_specific_gross_evolved_anatomical_entity_develops_from.md)
 * [existence ends during](existence_ends_during.md)
    * [anatomical entity➞existence ends during](anatomical_entity_existence_ends_during.md)
       * [species neutral evolved cell type➞existence ends during](species_neutral_evolved_cell_type_existence_ends_during.md)
       * [species neutral gross evolved anatomical entity➞existence ends during](species_neutral_gross_evolved_anatomical_entity_existence_ends_during.md)
       * [species specific evolved cell type➞existence ends during](species_specific_evolved_cell_type_existence_ends_during.md)
       * [species specific gross evolved anatomical entity➞existence ends during](species_specific_gross_evolved_anatomical_entity_existence_ends_during.md)
 * [existence starts during](existence_starts_during.md)
    * [anatomical entity➞existence starts during](anatomical_entity_existence_starts_during.md)
       * [species neutral evolved cell type➞existence starts during](species_neutral_evolved_cell_type_existence_starts_during.md)
       * [species neutral gross evolved anatomical entity➞existence starts during](species_neutral_gross_evolved_anatomical_entity_existence_starts_during.md)
       * [species specific evolved cell type➞existence starts during](species_specific_evolved_cell_type_existence_starts_during.md)
       * [species specific gross evolved anatomical entity➞existence starts during](species_specific_gross_evolved_anatomical_entity_existence_starts_during.md)
 * [has part](has_part.md)
    * [abnormal phenotype➞has part](abnormal_phenotype_has_part.md)
    * [mixture of chemical entities➞has part](mixture_of_chemical_entities_has_part.md)
 * [in taxon](in_taxon.md)
    * [organismal➞in taxon](organismal_in_taxon.md)
       * [species neutral➞in taxon](species_neutral_in_taxon.md)
       * [species specific➞in taxon](species_specific_in_taxon.md)
 * [never in taxon](never_in_taxon.md)
    * [organismal➞never in taxon](organismal_never_in_taxon.md)
 * [part of](part_of.md)
    * [anatomical entity➞part of](anatomical_entity_part_of.md)
       * [constructed cell type➞part of](constructed_cell_type_part_of.md)
       * [evolved anatomical entity➞part of](evolved_anatomical_entity_part_of.md)
          * [cellular evolved anatomical entity➞part of](cellular_evolved_anatomical_entity_part_of.md)
          * [evolved cell type➞part of](evolved_cell_type_part_of.md)
             * [species neutral evolved cell type➞part of](species_neutral_evolved_cell_type_part_of.md)
             * [species specific evolved cell type➞part of](species_specific_evolved_cell_type_part_of.md)
          * [gross evolved anatomical entity➞part of](gross_evolved_anatomical_entity_part_of.md)
             * [species neutral gross evolved anatomical entity➞part of](species_neutral_gross_evolved_anatomical_entity_part_of.md)
             * [species specific gross evolved anatomical entity➞part of](species_specific_gross_evolved_anatomical_entity_part_of.md)
       * [gross constructed anatomical entity➞part of](gross_constructed_anatomical_entity_part_of.md)
       * [gross pathological anatomical entity➞part of](gross_pathological_anatomical_entity_part_of.md)
       * [pathological cell type➞part of](pathological_cell_type_part_of.md)
 * [part_of](part_of.md)
 * [pathological of](pathological_of.md)
    * [gross pathological anatomical entity➞pathological of](gross_pathological_anatomical_entity_pathological_of.md)
 * [subclass of](subclass_of.md)
    * [anatomical entity➞subclass of](anatomical_entity_subclass_of.md)
       * [constructed cell type➞subclass of](constructed_cell_type_subclass_of.md)
       * [evolved anatomical entity➞subclass of](evolved_anatomical_entity_subclass_of.md)
          * [cellular evolved anatomical entity➞subclass of](cellular_evolved_anatomical_entity_subclass_of.md)
          * [evolved cell type➞subclass of](evolved_cell_type_subclass_of.md)
             * [species neutral evolved cell type➞subclass of](species_neutral_evolved_cell_type_subclass_of.md)
             * [species specific evolved cell type➞subclass of](species_specific_evolved_cell_type_subclass_of.md)
          * [gross evolved anatomical entity➞subclass of](gross_evolved_anatomical_entity_subclass_of.md)
             * [species neutral gross evolved anatomical entity➞subclass of](species_neutral_gross_evolved_anatomical_entity_subclass_of.md)
             * [species specific gross evolved anatomical entity➞subclass of](species_specific_gross_evolved_anatomical_entity_subclass_of.md)
       * [gross constructed anatomical entity➞subclass of](gross_constructed_anatomical_entity_subclass_of.md)
       * [gross pathological anatomical entity➞subclass of](gross_pathological_anatomical_entity_subclass_of.md)
       * [pathological cell type➞subclass of](pathological_cell_type_subclass_of.md)
    * [atomic phenotypic feature➞subclass of](atomic_phenotypic_feature_subclass_of.md)
    * [atomic trait➞subclass of](atomic_trait_subclass_of.md)

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
