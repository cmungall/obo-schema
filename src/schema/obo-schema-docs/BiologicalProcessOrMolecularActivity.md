
# Type: biological process or molecular activity




URI: [oboschema:BiologicalProcessOrMolecularActivity](http://purl.obolibrary.org/oboschema/BiologicalProcessOrMolecularActivity)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Process],[Organismal],[OrganismTaxon],[MolecularActivity],[Evolved],[BiologicalProcessOrMolecularActivity]uses%20-.->[Organismal],[BiologicalProcessOrMolecularActivity]uses%20-.->[Evolved],[BiologicalProcessOrMolecularActivity]^-[MolecularActivity],[BiologicalProcessOrMolecularActivity]^-[BiologicalProcess],[Process]^-[BiologicalProcessOrMolecularActivity],[BiologicalProcess])

## Parents

 *  is_a: [Process](Process.md)

## Uses Mixins

 *  mixin: [Organismal](Organismal.md)
 *  mixin: [Evolved](Evolved.md)

## Children

 * [BiologicalProcess](BiologicalProcess.md)
 * [MolecularActivity](MolecularActivity.md)

## Referenced by class


## Attributes


### Mixed in from organismal:

 * [organismal➞in taxon](organismal_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)

### Mixed in from organismal:

 * [organismal➞never in taxon](organismal_never_in_taxon.md)  <sub>OPT</sub>
    * range: [OrganismTaxon](OrganismTaxon.md)
