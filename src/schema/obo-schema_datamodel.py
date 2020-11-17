# Auto generated from obo-schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2020-11-17 13:14
# Schema: obo-schema
#
# id: obo-schema
# description: A high level map of OBO classes and how they connect
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import String

metamodel_version = "1.6.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
DDANAT = CurieNamespace('DDANAT', 'http://purl.obolibrary.org/obo/DDANAT_')
DOID = CurieNamespace('DOID', 'http://purl.obolibrary.org/obo/DOID_')
ECTO = CurieNamespace('ECTO', 'http://example.org/UNKNOWN/ECTO/')
EMAPA = CurieNamespace('EMAPA', 'http://purl.obolibrary.org/obo/EMAPA_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
FAO = CurieNamespace('FAO', 'http://purl.obolibrary.org/obo/FAO_')
FBBT = CurieNamespace('FBbt', 'http://purl.obolibrary.org/obo/FBbt_')
FMA = CurieNamespace('FMA', 'http://purl.obolibrary.org/obo/FMA_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MA = CurieNamespace('MA', 'http://purl.obolibrary.org/obo/MA_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
MP = CurieNamespace('MP', 'http://purl.obolibrary.org/obo/MP_')
MPATH = CurieNamespace('MPATH', 'http://purl.obolibrary.org/obo/MPATH_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBA = CurieNamespace('OBA', 'http://purl.obolibrary.org/obo/OBA_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PMID = CurieNamespace('PMID', 'http://example.org/UNKNOWN/PMID/')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
TO = CurieNamespace('TO', 'http://purl.obolibrary.org/obo/TO_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
UPHENO = CurieNamespace('UPHENO', 'http://purl.obolibrary.org/obo/UPHENO_')
VT = CurieNamespace('VT', 'http://purl.obolibrary.org/obo/VT_')
WBBT = CurieNamespace('WBbt', 'http://purl.obolibrary.org/obo/WBBT_')
WBLS = CurieNamespace('WBls', 'http://purl.obolibrary.org/obo/WBLS_')
XAO = CurieNamespace('XAO', 'http://purl.obolibrary.org/obo/XAO_')
XPO = CurieNamespace('XPO', 'http://example.org/UNKNOWN/XPO/')
ZFA = CurieNamespace('ZFA', 'http://purl.obolibrary.org/obo/ZFA_')
ZFS = CurieNamespace('ZFS', 'http://purl.obolibrary.org/obo/ZFS_')
ZP = CurieNamespace('ZP', 'http://example.org/UNKNOWN/ZP/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
OBOSCHEMA = CurieNamespace('oboschema', 'http://purl.obolibrary.org/oboschema/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = OBOSCHEMA


# Types

# Class references



class Entity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Entity
    class_class_curie: ClassVar[str] = "oboschema:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Entity


class PhysicalEntityOrProcess(Entity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.PhysicalEntityOrProcess
    class_class_curie: ClassVar[str] = "oboschema:PhysicalEntityOrProcess"
    class_name: ClassVar[str] = "physical entity or process"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.PhysicalEntityOrProcess


class Occurrent(PhysicalEntityOrProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Occurrent
    class_class_curie: ClassVar[str] = "oboschema:Occurrent"
    class_name: ClassVar[str] = "occurrent"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Occurrent


class Process(PhysicalEntityOrProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Process
    class_class_curie: ClassVar[str] = "oboschema:Process"
    class_name: ClassVar[str] = "process"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Process


class PhysicalEntity(PhysicalEntityOrProcess):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.PhysicalEntity
    class_class_curie: ClassVar[str] = "oboschema:PhysicalEntity"
    class_name: ClassVar[str] = "physical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.PhysicalEntity


class OrganismTaxon(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.OrganismTaxon
    class_class_curie: ClassVar[str] = "oboschema:OrganismTaxon"
    class_name: ClassVar[str] = "organism taxon"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.OrganismTaxon


class Species(OrganismTaxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Species
    class_class_curie: ClassVar[str] = "oboschema:Species"
    class_name: ClassVar[str] = "species"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Species


class BroadOrganismTaxon(OrganismTaxon):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.BroadOrganismTaxon
    class_class_curie: ClassVar[str] = "oboschema:BroadOrganismTaxon"
    class_name: ClassVar[str] = "broad organism taxon"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.BroadOrganismTaxon


class Unit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Unit
    class_class_curie: ClassVar[str] = "oboschema:Unit"
    class_name: ClassVar[str] = "unit"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Unit


class Characteristic(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Characteristic
    class_class_curie: ClassVar[str] = "oboschema:Characteristic"
    class_name: ClassVar[str] = "characteristic"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Characteristic


class CharacteristicAttribute(Characteristic):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.CharacteristicAttribute
    class_class_curie: ClassVar[str] = "oboschema:CharacteristicAttribute"
    class_name: ClassVar[str] = "characteristic attribute"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.CharacteristicAttribute


class CharacteristicValue(Characteristic):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.CharacteristicValue
    class_class_curie: ClassVar[str] = "oboschema:CharacteristicValue"
    class_name: ClassVar[str] = "characteristic value"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.CharacteristicValue


@dataclass
class Disease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Disease
    class_class_curie: ClassVar[str] = "oboschema:Disease"
    class_name: ClassVar[str] = "disease"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Disease

    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class AbnormalPhenotype(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AbnormalPhenotype
    class_class_curie: ClassVar[str] = "oboschema:AbnormalPhenotype"
    class_name: ClassVar[str] = "abnormal phenotype"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AbnormalPhenotype

    has_part: Optional[Union[dict, "AtomicPhenotypicFeature"]] = None
    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_part is not None and not isinstance(self.has_part, AtomicPhenotypicFeature):
            self.has_part = AtomicPhenotypicFeature(**self.has_part)

        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


class SpeciesSpecificAbnormalPhenotype(AbnormalPhenotype):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificAbnormalPhenotype
    class_class_curie: ClassVar[str] = "oboschema:SpeciesSpecificAbnormalPhenotype"
    class_name: ClassVar[str] = "species specific abnormal phenotype"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificAbnormalPhenotype


class SpeciesNeutralAbnormalPhenotype(AbnormalPhenotype):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralAbnormalPhenotype
    class_class_curie: ClassVar[str] = "oboschema:SpeciesNeutralAbnormalPhenotype"
    class_name: ClassVar[str] = "species neutral abnormal phenotype"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralAbnormalPhenotype


@dataclass
class AtomicTraitOrPhenotypicFeature(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicTraitOrPhenotypicFeature
    class_class_curie: ClassVar[str] = "oboschema:AtomicTraitOrPhenotypicFeature"
    class_name: ClassVar[str] = "atomic trait or phenotypic feature"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicTraitOrPhenotypicFeature

    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class AtomicPhenotypicFeature(AtomicTraitOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicPhenotypicFeature
    class_class_curie: ClassVar[str] = "oboschema:AtomicPhenotypicFeature"
    class_name: ClassVar[str] = "atomic phenotypic feature"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicPhenotypicFeature

    subclass_of: Optional[Union[Union[dict, CharacteristicValue], List[Union[dict, CharacteristicValue]]]] = empty_list()
    characteristic_of: Optional[Union[dict, PhysicalEntityOrProcess]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, CharacteristicValue) else CharacteristicValue(**v) for v in self.subclass_of]

        if self.characteristic_of is not None and not isinstance(self.characteristic_of, PhysicalEntityOrProcess):
            self.characteristic_of = PhysicalEntityOrProcess()

        super().__post_init__(**kwargs)


@dataclass
class AtomicTrait(AtomicTraitOrPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicTrait
    class_class_curie: ClassVar[str] = "oboschema:AtomicTrait"
    class_name: ClassVar[str] = "atomic trait"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AtomicTrait

    subclass_of: Optional[Union[Union[dict, CharacteristicAttribute], List[Union[dict, CharacteristicAttribute]]]] = empty_list()
    characteristic_of: Optional[Union[dict, Entity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, CharacteristicAttribute) else CharacteristicAttribute(**v) for v in self.subclass_of]

        if self.characteristic_of is not None and not isinstance(self.characteristic_of, Entity):
            self.characteristic_of = Entity()

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalAtomicPhenotypicFeature(AtomicPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AnatomicalAtomicPhenotypicFeature
    class_class_curie: ClassVar[str] = "oboschema:AnatomicalAtomicPhenotypicFeature"
    class_name: ClassVar[str] = "anatomical atomic phenotypic feature"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AnatomicalAtomicPhenotypicFeature

    characteristic_of: Optional[Union[dict, "EvolvedAnatomicalEntity"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.characteristic_of is not None and not isinstance(self.characteristic_of, EvolvedAnatomicalEntity):
            self.characteristic_of = EvolvedAnatomicalEntity(**self.characteristic_of)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntityAtomicPhenotypicFeature(AtomicPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.ChemicalEntityAtomicPhenotypicFeature
    class_class_curie: ClassVar[str] = "oboschema:ChemicalEntityAtomicPhenotypicFeature"
    class_name: ClassVar[str] = "chemical entity atomic phenotypic feature"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.ChemicalEntityAtomicPhenotypicFeature

    characteristic_of: Optional[Union[dict, "ChemicalEntity"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.characteristic_of is not None and not isinstance(self.characteristic_of, ChemicalEntity):
            self.characteristic_of = ChemicalEntity(**self.characteristic_of)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcessAtomicPhenotypicFeature(AtomicPhenotypicFeature):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcessAtomicPhenotypicFeature
    class_class_curie: ClassVar[str] = "oboschema:BiologicalProcessAtomicPhenotypicFeature"
    class_name: ClassVar[str] = "biological process atomic phenotypic feature"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcessAtomicPhenotypicFeature

    characteristic_of: Optional[Union[dict, "BiologicalProcess"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.characteristic_of is not None and not isinstance(self.characteristic_of, BiologicalProcess):
            self.characteristic_of = BiologicalProcess(**self.characteristic_of)

        super().__post_init__(**kwargs)


@dataclass
class BiologicalProcessOrMolecularActivity(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcessOrMolecularActivity
    class_class_curie: ClassVar[str] = "oboschema:BiologicalProcessOrMolecularActivity"
    class_name: ClassVar[str] = "biological process or molecular activity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcessOrMolecularActivity

    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


class BiologicalProcess(BiologicalProcessOrMolecularActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcess
    class_class_curie: ClassVar[str] = "oboschema:BiologicalProcess"
    class_name: ClassVar[str] = "biological process"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.BiologicalProcess


class MolecularActivity(BiologicalProcessOrMolecularActivity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.MolecularActivity
    class_class_curie: ClassVar[str] = "oboschema:MolecularActivity"
    class_name: ClassVar[str] = "molecular activity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.MolecularActivity


@dataclass
class ChemicalEntity(PhysicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.ChemicalEntity
    class_class_curie: ClassVar[str] = "oboschema:ChemicalEntity"
    class_name: ClassVar[str] = "chemical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.ChemicalEntity

    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class MixtureOfChemicalEntities(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.MixtureOfChemicalEntities
    class_class_curie: ClassVar[str] = "oboschema:MixtureOfChemicalEntities"
    class_name: ClassVar[str] = "mixture of chemical entities"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.MixtureOfChemicalEntities

    has_part: Optional[Union[dict, ChemicalEntity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntity):
            self.has_part = ChemicalEntity(**self.has_part)

        super().__post_init__(**kwargs)


class Food(MixtureOfChemicalEntities):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Food
    class_class_curie: ClassVar[str] = "oboschema:Food"
    class_name: ClassVar[str] = "food"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Food


class PathologicalProcess(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.PathologicalProcess
    class_class_curie: ClassVar[str] = "oboschema:PathologicalProcess"
    class_name: ClassVar[str] = "pathological process"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.PathologicalProcess


class LifeStage(Occurrent):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.LifeStage
    class_class_curie: ClassVar[str] = "oboschema:LifeStage"
    class_name: ClassVar[str] = "life stage"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.LifeStage


@dataclass
class SpeciesSpecificLifeStage(LifeStage):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificLifeStage
    class_class_curie: ClassVar[str] = "oboschema:SpeciesSpecificLifeStage"
    class_name: ClassVar[str] = "species specific life stage"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificLifeStage

    in_taxon: Optional[Union[dict, Species]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, Species):
            self.in_taxon = Species()

        super().__post_init__(**kwargs)


@dataclass
class SpeciesNeutralLifeStage(LifeStage):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralLifeStage
    class_class_curie: ClassVar[str] = "oboschema:SpeciesNeutralLifeStage"
    class_name: ClassVar[str] = "species neutral life stage"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralLifeStage

    in_taxon: Optional[Union[dict, BroadOrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, BroadOrganismTaxon):
            self.in_taxon = BroadOrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class AnatomicalEntity(PhysicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:AnatomicalEntity"
    class_name: ClassVar[str] = "anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "AnatomicalEntity"], List[Union[dict, "AnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, "AnatomicalEntity"]] = None
    develops_from: Optional[Union[Union[dict, "AnatomicalEntity"], List[Union[dict, "AnatomicalEntity"]]]] = empty_list()
    existence_starts_during: Optional[Union[dict, LifeStage]] = None
    existence_ends_during: Optional[Union[dict, LifeStage]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, AnatomicalEntity) else AnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, AnatomicalEntity):
            self.part_of = AnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, AnatomicalEntity) else AnatomicalEntity(**v) for v in self.develops_from]

        if self.existence_starts_during is not None and not isinstance(self.existence_starts_during, LifeStage):
            self.existence_starts_during = LifeStage()

        if self.existence_ends_during is not None and not isinstance(self.existence_ends_during, LifeStage):
            self.existence_ends_during = LifeStage()

        super().__post_init__(**kwargs)


class VariantAnatomicalEntity(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.VariantAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:VariantAnatomicalEntity"
    class_name: ClassVar[str] = "variant anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.VariantAnatomicalEntity


class AbormalAnatomicalEntity(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.AbormalAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:AbormalAnatomicalEntity"
    class_name: ClassVar[str] = "abormal anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.AbormalAnatomicalEntity


@dataclass
class EvolvedAnatomicalEntity(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.EvolvedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:EvolvedAnatomicalEntity"
    class_name: ClassVar[str] = "evolved anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.EvolvedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "EvolvedAnatomicalEntity"], List[Union[dict, "EvolvedAnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, "EvolvedAnatomicalEntity"]] = None
    develops_from: Optional[Union[Union[dict, "EvolvedAnatomicalEntity"], List[Union[dict, "EvolvedAnatomicalEntity"]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, EvolvedAnatomicalEntity) else EvolvedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, EvolvedAnatomicalEntity):
            self.part_of = EvolvedAnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, EvolvedAnatomicalEntity) else EvolvedAnatomicalEntity(**v) for v in self.develops_from]

        super().__post_init__(**kwargs)


@dataclass
class CellularEvolvedAnatomicalEntity(EvolvedAnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.CellularEvolvedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:CellularEvolvedAnatomicalEntity"
    class_name: ClassVar[str] = "cellular evolved anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.CellularEvolvedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "CellularEvolvedAnatomicalEntity"], List[Union[dict, "CellularEvolvedAnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, EvolvedAnatomicalEntity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, CellularEvolvedAnatomicalEntity) else CellularEvolvedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, EvolvedAnatomicalEntity):
            self.part_of = EvolvedAnatomicalEntity(**self.part_of)

        super().__post_init__(**kwargs)


@dataclass
class GrossEvolvedAnatomicalEntity(EvolvedAnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.GrossEvolvedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:GrossEvolvedAnatomicalEntity"
    class_name: ClassVar[str] = "gross evolved anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.GrossEvolvedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, EvolvedAnatomicalEntity], List[Union[dict, EvolvedAnatomicalEntity]]]] = empty_list()
    part_of: Optional[Union[dict, EvolvedAnatomicalEntity]] = None
    develops_from: Optional[Union[Union[dict, "GrossEvolvedAnatomicalEntity"], List[Union[dict, "GrossEvolvedAnatomicalEntity"]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, EvolvedAnatomicalEntity) else EvolvedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, EvolvedAnatomicalEntity):
            self.part_of = EvolvedAnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, GrossEvolvedAnatomicalEntity) else GrossEvolvedAnatomicalEntity(**v) for v in self.develops_from]

        super().__post_init__(**kwargs)


@dataclass
class GrossConstructedAnatomicalEntity(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.GrossConstructedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:GrossConstructedAnatomicalEntity"
    class_name: ClassVar[str] = "gross constructed anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.GrossConstructedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "GrossConstructedAnatomicalEntity"], List[Union[dict, "GrossConstructedAnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, "GrossConstructedAnatomicalEntity"]] = None
    analog_of: Optional[Union[dict, GrossEvolvedAnatomicalEntity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, GrossConstructedAnatomicalEntity) else GrossConstructedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, GrossConstructedAnatomicalEntity):
            self.part_of = GrossConstructedAnatomicalEntity(**self.part_of)

        if self.analog_of is not None and not isinstance(self.analog_of, GrossEvolvedAnatomicalEntity):
            self.analog_of = GrossEvolvedAnatomicalEntity(**self.analog_of)

        super().__post_init__(**kwargs)


@dataclass
class GrossPathologicalAnatomicalEntity(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.GrossPathologicalAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:GrossPathologicalAnatomicalEntity"
    class_name: ClassVar[str] = "gross pathological anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.GrossPathologicalAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "GrossPathologicalAnatomicalEntity"], List[Union[dict, "GrossPathologicalAnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, "GrossPathologicalAnatomicalEntity"]] = None
    pathological_of: Optional[Union[dict, GrossEvolvedAnatomicalEntity]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, GrossPathologicalAnatomicalEntity) else GrossPathologicalAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, GrossPathologicalAnatomicalEntity):
            self.part_of = GrossPathologicalAnatomicalEntity(**self.part_of)

        if self.pathological_of is not None and not isinstance(self.pathological_of, GrossEvolvedAnatomicalEntity):
            self.pathological_of = GrossEvolvedAnatomicalEntity(**self.pathological_of)

        super().__post_init__(**kwargs)


@dataclass
class SpeciesNeutralGrossEvolvedAnatomicalEntity(GrossEvolvedAnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralGrossEvolvedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:SpeciesNeutralGrossEvolvedAnatomicalEntity"
    class_name: ClassVar[str] = "species neutral gross evolved anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralGrossEvolvedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]]]] = empty_list()
    part_of: Optional[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]] = None
    develops_from: Optional[Union[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]]]] = empty_list()
    existence_starts_during: Optional[Union[dict, SpeciesNeutralLifeStage]] = None
    existence_ends_during: Optional[Union[dict, SpeciesNeutralLifeStage]] = None
    in_taxon: Optional[Union[dict, BroadOrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, SpeciesNeutralGrossEvolvedAnatomicalEntity) else SpeciesNeutralGrossEvolvedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, SpeciesNeutralGrossEvolvedAnatomicalEntity):
            self.part_of = SpeciesNeutralGrossEvolvedAnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, SpeciesNeutralGrossEvolvedAnatomicalEntity) else SpeciesNeutralGrossEvolvedAnatomicalEntity(**v) for v in self.develops_from]

        if self.existence_starts_during is not None and not isinstance(self.existence_starts_during, SpeciesNeutralLifeStage):
            self.existence_starts_during = SpeciesNeutralLifeStage(**self.existence_starts_during)

        if self.existence_ends_during is not None and not isinstance(self.existence_ends_during, SpeciesNeutralLifeStage):
            self.existence_ends_during = SpeciesNeutralLifeStage(**self.existence_ends_during)

        if self.in_taxon is not None and not isinstance(self.in_taxon, BroadOrganismTaxon):
            self.in_taxon = BroadOrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class SpeciesSpecificGrossEvolvedAnatomicalEntity(GrossEvolvedAnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificGrossEvolvedAnatomicalEntity
    class_class_curie: ClassVar[str] = "oboschema:SpeciesSpecificGrossEvolvedAnatomicalEntity"
    class_name: ClassVar[str] = "species specific gross evolved anatomical entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificGrossEvolvedAnatomicalEntity

    subclass_of: Optional[Union[Union[dict, GrossEvolvedAnatomicalEntity], List[Union[dict, GrossEvolvedAnatomicalEntity]]]] = empty_list()
    part_of: Optional[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"]] = None
    develops_from: Optional[Union[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"]]]] = empty_list()
    existence_starts_during: Optional[Union[dict, LifeStage]] = None
    existence_ends_during: Optional[Union[dict, LifeStage]] = None
    in_taxon: Optional[Union[dict, Species]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, GrossEvolvedAnatomicalEntity) else GrossEvolvedAnatomicalEntity(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, SpeciesSpecificGrossEvolvedAnatomicalEntity):
            self.part_of = SpeciesSpecificGrossEvolvedAnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, SpeciesSpecificGrossEvolvedAnatomicalEntity) else SpeciesSpecificGrossEvolvedAnatomicalEntity(**v) for v in self.develops_from]

        if self.existence_starts_during is not None and not isinstance(self.existence_starts_during, LifeStage):
            self.existence_starts_during = LifeStage()

        if self.existence_ends_during is not None and not isinstance(self.existence_ends_during, LifeStage):
            self.existence_ends_during = LifeStage()

        if self.in_taxon is not None and not isinstance(self.in_taxon, Species):
            self.in_taxon = Species()

        super().__post_init__(**kwargs)


@dataclass
class EvolvedCellType(EvolvedAnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.EvolvedCellType
    class_class_curie: ClassVar[str] = "oboschema:EvolvedCellType"
    class_name: ClassVar[str] = "evolved cell type"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.EvolvedCellType

    subclass_of: Optional[Union[Union[dict, "EvolvedCellType"], List[Union[dict, "EvolvedCellType"]]]] = empty_list()
    part_of: Optional[Union[dict, GrossEvolvedAnatomicalEntity]] = None
    develops_from: Optional[Union[Union[dict, "EvolvedCellType"], List[Union[dict, "EvolvedCellType"]]]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, EvolvedCellType) else EvolvedCellType(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, GrossEvolvedAnatomicalEntity):
            self.part_of = GrossEvolvedAnatomicalEntity(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, EvolvedCellType) else EvolvedCellType(**v) for v in self.develops_from]

        super().__post_init__(**kwargs)


@dataclass
class ConstructedCellType(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.ConstructedCellType
    class_class_curie: ClassVar[str] = "oboschema:ConstructedCellType"
    class_name: ClassVar[str] = "constructed cell type"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.ConstructedCellType

    subclass_of: Optional[Union[Union[dict, "ConstructedCellType"], List[Union[dict, "ConstructedCellType"]]]] = empty_list()
    part_of: Optional[Union[dict, "ConstructedCellType"]] = None
    analog_of: Optional[Union[dict, EvolvedCellType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, ConstructedCellType) else ConstructedCellType(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, ConstructedCellType):
            self.part_of = ConstructedCellType(**self.part_of)

        if self.analog_of is not None and not isinstance(self.analog_of, EvolvedCellType):
            self.analog_of = EvolvedCellType(**self.analog_of)

        super().__post_init__(**kwargs)


@dataclass
class PathologicalCellType(AnatomicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.PathologicalCellType
    class_class_curie: ClassVar[str] = "oboschema:PathologicalCellType"
    class_name: ClassVar[str] = "pathological cell type"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.PathologicalCellType

    subclass_of: Optional[Union[Union[dict, "PathologicalCellType"], List[Union[dict, "PathologicalCellType"]]]] = empty_list()
    part_of: Optional[Union[dict, "PathologicalCellType"]] = None
    analog_of: Optional[Union[dict, EvolvedCellType]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, PathologicalCellType) else PathologicalCellType(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, PathologicalCellType):
            self.part_of = PathologicalCellType(**self.part_of)

        if self.analog_of is not None and not isinstance(self.analog_of, EvolvedCellType):
            self.analog_of = EvolvedCellType(**self.analog_of)

        super().__post_init__(**kwargs)


@dataclass
class SpeciesNeutralEvolvedCellType(EvolvedCellType):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralEvolvedCellType
    class_class_curie: ClassVar[str] = "oboschema:SpeciesNeutralEvolvedCellType"
    class_name: ClassVar[str] = "species neutral evolved cell type"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesNeutralEvolvedCellType

    subclass_of: Optional[Union[Union[dict, "SpeciesNeutralEvolvedCellType"], List[Union[dict, "SpeciesNeutralEvolvedCellType"]]]] = empty_list()
    part_of: Optional[Union[dict, "SpeciesNeutralEvolvedCellType"]] = None
    develops_from: Optional[Union[Union[dict, "SpeciesNeutralEvolvedCellType"], List[Union[dict, "SpeciesNeutralEvolvedCellType"]]]] = empty_list()
    existence_starts_during: Optional[Union[dict, SpeciesNeutralLifeStage]] = None
    existence_ends_during: Optional[Union[dict, SpeciesNeutralLifeStage]] = None
    in_taxon: Optional[Union[dict, BroadOrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, SpeciesNeutralEvolvedCellType) else SpeciesNeutralEvolvedCellType(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, SpeciesNeutralEvolvedCellType):
            self.part_of = SpeciesNeutralEvolvedCellType(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, SpeciesNeutralEvolvedCellType) else SpeciesNeutralEvolvedCellType(**v) for v in self.develops_from]

        if self.existence_starts_during is not None and not isinstance(self.existence_starts_during, SpeciesNeutralLifeStage):
            self.existence_starts_during = SpeciesNeutralLifeStage(**self.existence_starts_during)

        if self.existence_ends_during is not None and not isinstance(self.existence_ends_during, SpeciesNeutralLifeStage):
            self.existence_ends_during = SpeciesNeutralLifeStage(**self.existence_ends_during)

        if self.in_taxon is not None and not isinstance(self.in_taxon, BroadOrganismTaxon):
            self.in_taxon = BroadOrganismTaxon()

        super().__post_init__(**kwargs)


@dataclass
class SpeciesSpecificEvolvedCellType(EvolvedCellType):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificEvolvedCellType
    class_class_curie: ClassVar[str] = "oboschema:SpeciesSpecificEvolvedCellType"
    class_name: ClassVar[str] = "species specific evolved cell type"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.SpeciesSpecificEvolvedCellType

    subclass_of: Optional[Union[Union[dict, "SpeciesSpecificEvolvedCellType"], List[Union[dict, "SpeciesSpecificEvolvedCellType"]]]] = empty_list()
    part_of: Optional[Union[dict, "SpeciesSpecificEvolvedCellType"]] = None
    develops_from: Optional[Union[Union[dict, "SpeciesSpecificEvolvedCellType"], List[Union[dict, "SpeciesSpecificEvolvedCellType"]]]] = empty_list()
    existence_starts_during: Optional[Union[dict, LifeStage]] = None
    existence_ends_during: Optional[Union[dict, LifeStage]] = None
    in_taxon: Optional[Union[dict, Species]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.subclass_of is None:
            self.subclass_of = []
        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of]
        self.subclass_of = [v if isinstance(v, SpeciesSpecificEvolvedCellType) else SpeciesSpecificEvolvedCellType(**v) for v in self.subclass_of]

        if self.part_of is not None and not isinstance(self.part_of, SpeciesSpecificEvolvedCellType):
            self.part_of = SpeciesSpecificEvolvedCellType(**self.part_of)

        if self.develops_from is None:
            self.develops_from = []
        if not isinstance(self.develops_from, list):
            self.develops_from = [self.develops_from]
        self.develops_from = [v if isinstance(v, SpeciesSpecificEvolvedCellType) else SpeciesSpecificEvolvedCellType(**v) for v in self.develops_from]

        if self.existence_starts_during is not None and not isinstance(self.existence_starts_during, LifeStage):
            self.existence_starts_during = LifeStage()

        if self.existence_ends_during is not None and not isinstance(self.existence_ends_during, LifeStage):
            self.existence_ends_during = LifeStage()

        if self.in_taxon is not None and not isinstance(self.in_taxon, Species):
            self.in_taxon = Species()

        super().__post_init__(**kwargs)


@dataclass
class Exposure(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Exposure
    class_class_curie: ClassVar[str] = "oboschema:Exposure"
    class_name: ClassVar[str] = "exposure"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Exposure

    in_taxon: Optional[Union[dict, OrganismTaxon]] = None
    never_in_taxon: Optional[Union[dict, OrganismTaxon]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.in_taxon is not None and not isinstance(self.in_taxon, OrganismTaxon):
            self.in_taxon = OrganismTaxon()

        if self.never_in_taxon is not None and not isinstance(self.never_in_taxon, OrganismTaxon):
            self.never_in_taxon = OrganismTaxon()

        super().__post_init__(**kwargs)


class PlanetaryEntity(PhysicalEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.PlanetaryEntity
    class_class_curie: ClassVar[str] = "oboschema:PlanetaryEntity"
    class_name: ClassVar[str] = "planetary entity"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.PlanetaryEntity


class EnvironmentalProcess(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.EnvironmentalProcess
    class_class_curie: ClassVar[str] = "oboschema:EnvironmentalProcess"
    class_name: ClassVar[str] = "environmental process"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.EnvironmentalProcess


class Information(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Information
    class_class_curie: ClassVar[str] = "oboschema:Information"
    class_name: ClassVar[str] = "information"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Information


class Publication(Information):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Publication
    class_class_curie: ClassVar[str] = "oboschema:Publication"
    class_name: ClassVar[str] = "publication"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Publication


class OntologyAxiom(Information):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.OntologyAxiom
    class_class_curie: ClassVar[str] = "oboschema:OntologyAxiom"
    class_name: ClassVar[str] = "ontology axiom"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.OntologyAxiom


class Variant(Origin):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OBOSCHEMA.Variant
    class_class_curie: ClassVar[str] = "oboschema:Variant"
    class_name: ClassVar[str] = "variant"
    class_model_uri: ClassVar[URIRef] = OBOSCHEMA.Variant



# Slots
class slots:
    pass

slots.subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.subclass_of, domain=None, range=Optional[Union[str, List[str]]])

slots.part_of = Slot(uri=OBOSCHEMA.part_of, name="part_of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.part_of, domain=None, range=Optional[Union[str, List[str]]])

slots.develops_from = Slot(uri=OBOSCHEMA.develops_from, name="develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.develops_from, domain=None, range=Optional[Union[str, List[str]]])

slots.analog_of = Slot(uri=OBOSCHEMA.analog_of, name="analog of", curie=OBOSCHEMA.curie('analog_of'),
                   model_uri=OBOSCHEMA.analog_of, domain=None, range=Optional[str])

slots.existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.existence_starts_during, domain=None, range=Optional[str])

slots.existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.existence_ends_during, domain=None, range=Optional[str])

slots.in_taxon = Slot(uri=OBOSCHEMA.in_taxon, name="in taxon", curie=OBOSCHEMA.curie('in_taxon'),
                   model_uri=OBOSCHEMA.in_taxon, domain=None, range=Optional[Union[dict, OrganismTaxon]])

slots.never_in_taxon = Slot(uri=OBOSCHEMA.never_in_taxon, name="never in taxon", curie=OBOSCHEMA.curie('never_in_taxon'),
                   model_uri=OBOSCHEMA.never_in_taxon, domain=None, range=Optional[Union[dict, OrganismTaxon]])

slots.has_part = Slot(uri=OBOSCHEMA.has_part, name="has part", curie=OBOSCHEMA.curie('has_part'),
                   model_uri=OBOSCHEMA.has_part, domain=None, range=Optional[Union[dict, AtomicPhenotypicFeature]])

slots.characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.characteristic_of, domain=None, range=Optional[Union[dict, PhysicalEntityOrProcess]])

slots.part_of = Slot(uri=OBOSCHEMA.part_of, name="part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.part_of, domain=None, range=Optional[Union[dict, AnatomicalEntity]])

slots.pathological_of = Slot(uri=OBOSCHEMA.pathological_of, name="pathological of", curie=OBOSCHEMA.curie('pathological_of'),
                   model_uri=OBOSCHEMA.pathological_of, domain=None, range=Optional[Union[dict, GrossEvolvedAnatomicalEntity]])

slots.abnormal_phenotype_has_part = Slot(uri=OBOSCHEMA.has_part, name="abnormal phenotype_has part", curie=OBOSCHEMA.curie('has_part'),
                   model_uri=OBOSCHEMA.abnormal_phenotype_has_part, domain=AbnormalPhenotype, range=Optional[Union[dict, "AtomicPhenotypicFeature"]])

slots.atomic_phenotypic_feature_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="atomic phenotypic feature_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.atomic_phenotypic_feature_subclass_of, domain=AtomicPhenotypicFeature, range=Optional[Union[Union[dict, CharacteristicValue], List[Union[dict, CharacteristicValue]]]])

slots.atomic_phenotypic_feature_characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="atomic phenotypic feature_characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.atomic_phenotypic_feature_characteristic_of, domain=AtomicPhenotypicFeature, range=Optional[Union[dict, PhysicalEntityOrProcess]])

slots.atomic_trait_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="atomic trait_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.atomic_trait_subclass_of, domain=AtomicTrait, range=Optional[Union[Union[dict, CharacteristicAttribute], List[Union[dict, CharacteristicAttribute]]]])

slots.atomic_trait_characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="atomic trait_characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.atomic_trait_characteristic_of, domain=AtomicTrait, range=Optional[Union[dict, Entity]])

slots.anatomical_atomic_phenotypic_feature_characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="anatomical atomic phenotypic feature_characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.anatomical_atomic_phenotypic_feature_characteristic_of, domain=AnatomicalAtomicPhenotypicFeature, range=Optional[Union[dict, "EvolvedAnatomicalEntity"]])

slots.chemical_entity_atomic_phenotypic_feature_characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="chemical entity atomic phenotypic feature_characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.chemical_entity_atomic_phenotypic_feature_characteristic_of, domain=ChemicalEntityAtomicPhenotypicFeature, range=Optional[Union[dict, "ChemicalEntity"]])

slots.biological_process_atomic_phenotypic_feature_characteristic_of = Slot(uri=OBOSCHEMA.characteristic_of, name="biological process atomic phenotypic feature_characteristic of", curie=OBOSCHEMA.curie('characteristic_of'),
                   model_uri=OBOSCHEMA.biological_process_atomic_phenotypic_feature_characteristic_of, domain=BiologicalProcessAtomicPhenotypicFeature, range=Optional[Union[dict, "BiologicalProcess"]])

slots.mixture_of_chemical_entities_has_part = Slot(uri=OBOSCHEMA.has_part, name="mixture of chemical entities_has part", curie=OBOSCHEMA.curie('has_part'),
                   model_uri=OBOSCHEMA.mixture_of_chemical_entities_has_part, domain=MixtureOfChemicalEntities, range=Optional[Union[dict, ChemicalEntity]])

slots.anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.anatomical_entity_subclass_of, domain=AnatomicalEntity, range=Optional[Union[Union[dict, "AnatomicalEntity"], List[Union[dict, "AnatomicalEntity"]]]])

slots.anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.anatomical_entity_part_of, domain=AnatomicalEntity, range=Optional[Union[dict, "AnatomicalEntity"]])

slots.anatomical_entity_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="anatomical entity_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.anatomical_entity_develops_from, domain=AnatomicalEntity, range=Optional[Union[Union[dict, "AnatomicalEntity"], List[Union[dict, "AnatomicalEntity"]]]])

slots.anatomical_entity_existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="anatomical entity_existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.anatomical_entity_existence_starts_during, domain=AnatomicalEntity, range=Optional[Union[dict, LifeStage]])

slots.anatomical_entity_existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="anatomical entity_existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.anatomical_entity_existence_ends_during, domain=AnatomicalEntity, range=Optional[Union[dict, LifeStage]])

slots.evolved_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="evolved anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.evolved_anatomical_entity_subclass_of, domain=EvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "EvolvedAnatomicalEntity"], List[Union[dict, "EvolvedAnatomicalEntity"]]]])

slots.evolved_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="evolved anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.evolved_anatomical_entity_part_of, domain=EvolvedAnatomicalEntity, range=Optional[Union[dict, "EvolvedAnatomicalEntity"]])

slots.evolved_anatomical_entity_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="evolved anatomical entity_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.evolved_anatomical_entity_develops_from, domain=EvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "EvolvedAnatomicalEntity"], List[Union[dict, "EvolvedAnatomicalEntity"]]]])

slots.cellular_evolved_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="cellular evolved anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.cellular_evolved_anatomical_entity_subclass_of, domain=CellularEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "CellularEvolvedAnatomicalEntity"], List[Union[dict, "CellularEvolvedAnatomicalEntity"]]]])

slots.cellular_evolved_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="cellular evolved anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.cellular_evolved_anatomical_entity_part_of, domain=CellularEvolvedAnatomicalEntity, range=Optional[Union[dict, EvolvedAnatomicalEntity]])

slots.gross_evolved_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="gross evolved anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.gross_evolved_anatomical_entity_subclass_of, domain=GrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, EvolvedAnatomicalEntity], List[Union[dict, EvolvedAnatomicalEntity]]]])

slots.gross_evolved_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="gross evolved anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.gross_evolved_anatomical_entity_part_of, domain=GrossEvolvedAnatomicalEntity, range=Optional[Union[dict, EvolvedAnatomicalEntity]])

slots.gross_evolved_anatomical_entity_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="gross evolved anatomical entity_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.gross_evolved_anatomical_entity_develops_from, domain=GrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "GrossEvolvedAnatomicalEntity"], List[Union[dict, "GrossEvolvedAnatomicalEntity"]]]])

slots.gross_constructed_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="gross constructed anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.gross_constructed_anatomical_entity_subclass_of, domain=GrossConstructedAnatomicalEntity, range=Optional[Union[Union[dict, "GrossConstructedAnatomicalEntity"], List[Union[dict, "GrossConstructedAnatomicalEntity"]]]])

slots.gross_constructed_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="gross constructed anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.gross_constructed_anatomical_entity_part_of, domain=GrossConstructedAnatomicalEntity, range=Optional[Union[dict, "GrossConstructedAnatomicalEntity"]])

slots.gross_constructed_anatomical_entity_analog_of = Slot(uri=OBOSCHEMA.analog_of, name="gross constructed anatomical entity_analog of", curie=OBOSCHEMA.curie('analog_of'),
                   model_uri=OBOSCHEMA.gross_constructed_anatomical_entity_analog_of, domain=GrossConstructedAnatomicalEntity, range=Optional[Union[dict, GrossEvolvedAnatomicalEntity]])

slots.gross_pathological_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="gross pathological anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.gross_pathological_anatomical_entity_subclass_of, domain=GrossPathologicalAnatomicalEntity, range=Optional[Union[Union[dict, "GrossPathologicalAnatomicalEntity"], List[Union[dict, "GrossPathologicalAnatomicalEntity"]]]])

slots.gross_pathological_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="gross pathological anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.gross_pathological_anatomical_entity_part_of, domain=GrossPathologicalAnatomicalEntity, range=Optional[Union[dict, "GrossPathologicalAnatomicalEntity"]])

slots.gross_pathological_anatomical_entity_pathological_of = Slot(uri=OBOSCHEMA.pathological_of, name="gross pathological anatomical entity_pathological of", curie=OBOSCHEMA.curie('pathological_of'),
                   model_uri=OBOSCHEMA.gross_pathological_anatomical_entity_pathological_of, domain=GrossPathologicalAnatomicalEntity, range=Optional[Union[dict, GrossEvolvedAnatomicalEntity]])

slots.species_neutral_gross_evolved_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="species neutral gross evolved anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.species_neutral_gross_evolved_anatomical_entity_subclass_of, domain=SpeciesNeutralGrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]]]])

slots.species_neutral_gross_evolved_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="species neutral gross evolved anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.species_neutral_gross_evolved_anatomical_entity_part_of, domain=SpeciesNeutralGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]])

slots.species_neutral_gross_evolved_anatomical_entity_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="species neutral gross evolved anatomical entity_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.species_neutral_gross_evolved_anatomical_entity_develops_from, domain=SpeciesNeutralGrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesNeutralGrossEvolvedAnatomicalEntity"]]]])

slots.species_neutral_gross_evolved_anatomical_entity_existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="species neutral gross evolved anatomical entity_existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.species_neutral_gross_evolved_anatomical_entity_existence_starts_during, domain=SpeciesNeutralGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, SpeciesNeutralLifeStage]])

slots.species_neutral_gross_evolved_anatomical_entity_existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="species neutral gross evolved anatomical entity_existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.species_neutral_gross_evolved_anatomical_entity_existence_ends_during, domain=SpeciesNeutralGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, SpeciesNeutralLifeStage]])

slots.species_specific_gross_evolved_anatomical_entity_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="species specific gross evolved anatomical entity_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.species_specific_gross_evolved_anatomical_entity_subclass_of, domain=SpeciesSpecificGrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, GrossEvolvedAnatomicalEntity], List[Union[dict, GrossEvolvedAnatomicalEntity]]]])

slots.species_specific_gross_evolved_anatomical_entity_part_of = Slot(uri=OBOSCHEMA.part_of, name="species specific gross evolved anatomical entity_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.species_specific_gross_evolved_anatomical_entity_part_of, domain=SpeciesSpecificGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"]])

slots.species_specific_gross_evolved_anatomical_entity_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="species specific gross evolved anatomical entity_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.species_specific_gross_evolved_anatomical_entity_develops_from, domain=SpeciesSpecificGrossEvolvedAnatomicalEntity, range=Optional[Union[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"], List[Union[dict, "SpeciesSpecificGrossEvolvedAnatomicalEntity"]]]])

slots.species_specific_gross_evolved_anatomical_entity_existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="species specific gross evolved anatomical entity_existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.species_specific_gross_evolved_anatomical_entity_existence_starts_during, domain=SpeciesSpecificGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, LifeStage]])

slots.species_specific_gross_evolved_anatomical_entity_existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="species specific gross evolved anatomical entity_existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.species_specific_gross_evolved_anatomical_entity_existence_ends_during, domain=SpeciesSpecificGrossEvolvedAnatomicalEntity, range=Optional[Union[dict, LifeStage]])

slots.evolved_cell_type_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="evolved cell type_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.evolved_cell_type_subclass_of, domain=EvolvedCellType, range=Optional[Union[Union[dict, "EvolvedCellType"], List[Union[dict, "EvolvedCellType"]]]])

slots.evolved_cell_type_part_of = Slot(uri=OBOSCHEMA.part_of, name="evolved cell type_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.evolved_cell_type_part_of, domain=EvolvedCellType, range=Optional[Union[dict, GrossEvolvedAnatomicalEntity]])

slots.evolved_cell_type_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="evolved cell type_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.evolved_cell_type_develops_from, domain=EvolvedCellType, range=Optional[Union[Union[dict, "EvolvedCellType"], List[Union[dict, "EvolvedCellType"]]]])

slots.constructed_cell_type_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="constructed cell type_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.constructed_cell_type_subclass_of, domain=ConstructedCellType, range=Optional[Union[Union[dict, "ConstructedCellType"], List[Union[dict, "ConstructedCellType"]]]])

slots.constructed_cell_type_part_of = Slot(uri=OBOSCHEMA.part_of, name="constructed cell type_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.constructed_cell_type_part_of, domain=ConstructedCellType, range=Optional[Union[dict, "ConstructedCellType"]])

slots.constructed_cell_type_analog_of = Slot(uri=OBOSCHEMA.analog_of, name="constructed cell type_analog of", curie=OBOSCHEMA.curie('analog_of'),
                   model_uri=OBOSCHEMA.constructed_cell_type_analog_of, domain=ConstructedCellType, range=Optional[Union[dict, EvolvedCellType]])

slots.pathological_cell_type_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="pathological cell type_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.pathological_cell_type_subclass_of, domain=PathologicalCellType, range=Optional[Union[Union[dict, "PathologicalCellType"], List[Union[dict, "PathologicalCellType"]]]])

slots.pathological_cell_type_part_of = Slot(uri=OBOSCHEMA.part_of, name="pathological cell type_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.pathological_cell_type_part_of, domain=PathologicalCellType, range=Optional[Union[dict, "PathologicalCellType"]])

slots.pathological_cell_type_analog_of = Slot(uri=OBOSCHEMA.analog_of, name="pathological cell type_analog of", curie=OBOSCHEMA.curie('analog_of'),
                   model_uri=OBOSCHEMA.pathological_cell_type_analog_of, domain=PathologicalCellType, range=Optional[Union[dict, EvolvedCellType]])

slots.species_neutral_evolved_cell_type_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="species neutral evolved cell type_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.species_neutral_evolved_cell_type_subclass_of, domain=SpeciesNeutralEvolvedCellType, range=Optional[Union[Union[dict, "SpeciesNeutralEvolvedCellType"], List[Union[dict, "SpeciesNeutralEvolvedCellType"]]]])

slots.species_neutral_evolved_cell_type_part_of = Slot(uri=OBOSCHEMA.part_of, name="species neutral evolved cell type_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.species_neutral_evolved_cell_type_part_of, domain=SpeciesNeutralEvolvedCellType, range=Optional[Union[dict, "SpeciesNeutralEvolvedCellType"]])

slots.species_neutral_evolved_cell_type_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="species neutral evolved cell type_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.species_neutral_evolved_cell_type_develops_from, domain=SpeciesNeutralEvolvedCellType, range=Optional[Union[Union[dict, "SpeciesNeutralEvolvedCellType"], List[Union[dict, "SpeciesNeutralEvolvedCellType"]]]])

slots.species_neutral_evolved_cell_type_existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="species neutral evolved cell type_existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.species_neutral_evolved_cell_type_existence_starts_during, domain=SpeciesNeutralEvolvedCellType, range=Optional[Union[dict, SpeciesNeutralLifeStage]])

slots.species_neutral_evolved_cell_type_existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="species neutral evolved cell type_existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.species_neutral_evolved_cell_type_existence_ends_during, domain=SpeciesNeutralEvolvedCellType, range=Optional[Union[dict, SpeciesNeutralLifeStage]])

slots.species_specific_evolved_cell_type_subclass_of = Slot(uri=OBOSCHEMA.subclass_of, name="species specific evolved cell type_subclass of", curie=OBOSCHEMA.curie('subclass_of'),
                   model_uri=OBOSCHEMA.species_specific_evolved_cell_type_subclass_of, domain=SpeciesSpecificEvolvedCellType, range=Optional[Union[Union[dict, "SpeciesSpecificEvolvedCellType"], List[Union[dict, "SpeciesSpecificEvolvedCellType"]]]])

slots.species_specific_evolved_cell_type_part_of = Slot(uri=OBOSCHEMA.part_of, name="species specific evolved cell type_part of", curie=OBOSCHEMA.curie('part_of'),
                   model_uri=OBOSCHEMA.species_specific_evolved_cell_type_part_of, domain=SpeciesSpecificEvolvedCellType, range=Optional[Union[dict, "SpeciesSpecificEvolvedCellType"]])

slots.species_specific_evolved_cell_type_develops_from = Slot(uri=OBOSCHEMA.develops_from, name="species specific evolved cell type_develops from", curie=OBOSCHEMA.curie('develops_from'),
                   model_uri=OBOSCHEMA.species_specific_evolved_cell_type_develops_from, domain=SpeciesSpecificEvolvedCellType, range=Optional[Union[Union[dict, "SpeciesSpecificEvolvedCellType"], List[Union[dict, "SpeciesSpecificEvolvedCellType"]]]])

slots.species_specific_evolved_cell_type_existence_starts_during = Slot(uri=OBOSCHEMA.existence_starts_during, name="species specific evolved cell type_existence starts during", curie=OBOSCHEMA.curie('existence_starts_during'),
                   model_uri=OBOSCHEMA.species_specific_evolved_cell_type_existence_starts_during, domain=SpeciesSpecificEvolvedCellType, range=Optional[Union[dict, LifeStage]])

slots.species_specific_evolved_cell_type_existence_ends_during = Slot(uri=OBOSCHEMA.existence_ends_during, name="species specific evolved cell type_existence ends during", curie=OBOSCHEMA.curie('existence_ends_during'),
                   model_uri=OBOSCHEMA.species_specific_evolved_cell_type_existence_ends_during, domain=SpeciesSpecificEvolvedCellType, range=Optional[Union[dict, LifeStage]])

slots.organismal_in_taxon = Slot(uri=OBOSCHEMA.in_taxon, name="organismal_in taxon", curie=OBOSCHEMA.curie('in_taxon'),
                   model_uri=OBOSCHEMA.organismal_in_taxon, domain=None, range=Optional[Union[dict, OrganismTaxon]])

slots.organismal_never_in_taxon = Slot(uri=OBOSCHEMA.never_in_taxon, name="organismal_never in taxon", curie=OBOSCHEMA.curie('never_in_taxon'),
                   model_uri=OBOSCHEMA.organismal_never_in_taxon, domain=None, range=Optional[Union[dict, OrganismTaxon]])

slots.species_specific_in_taxon = Slot(uri=OBOSCHEMA.in_taxon, name="species specific_in taxon", curie=OBOSCHEMA.curie('in_taxon'),
                   model_uri=OBOSCHEMA.species_specific_in_taxon, domain=None, range=Optional[Union[dict, Species]])

slots.species_neutral_in_taxon = Slot(uri=OBOSCHEMA.in_taxon, name="species neutral_in taxon", curie=OBOSCHEMA.curie('in_taxon'),
                   model_uri=OBOSCHEMA.species_neutral_in_taxon, domain=None, range=Optional[Union[dict, BroadOrganismTaxon]])
