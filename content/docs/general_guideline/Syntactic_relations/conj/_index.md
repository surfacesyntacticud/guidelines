---
title: "conj & subrels"
weight: 1
# bookFlatSection: false
bookToc: true
# bookHidden: false
# bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# conj

## Universal

The `conj` relation in SUD corresponds to the three UD relations:
[`reparandum`](https://universaldependencies.org/u/dep/reparandum.html),
[`conj`](https://universaldependencies.org/u/dep/conj.html) and 
[`appos`](https://universaldependencies.org/u/dep/appos.html).

These three relations work as paradigmatic lists. That's why in SUD, we decided to gather these three relations under the main relation `conj` to underline the similarity between the three.

```grew
pattern { e : GOV-[1=conj]->DEP}
```

We distinguish:

 * [`conj:dicto`](./conj_dicto.md) for disfluencies when the speaker corrects his speech (parallel to `reparandum` in UD)
 * [`conj:coord`](./conj_coord.md) for elements connected by a coordinating conjunction (parallel to `conj` in UD)
 * [`conj:appos`](./conj_appos.md) for appositional modifiers that serve to define better the previous noun (parallel to `appos` in UD)

A global view of `conj` usage in the last release of SUD is shown in this [table](http://tables.grew.fr/?data=sud_deps/conj).

See also the [Coordination](../../Universal_construction/coordination/) page.


## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


