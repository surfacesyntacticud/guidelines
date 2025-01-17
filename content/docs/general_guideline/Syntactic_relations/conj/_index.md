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

 * [`conj:dicto`](./conj_dicto.md) for disfluencies when the speaker corrects his speech (parallel to `reparandum` in written texts)
 * [`conj:coord`](./conj_coord.md) for elements connected by a coordinating conjunction (parallel to `conj` in written texts)
 * [`conj:appos`](./conj_appos.md) for appositional modifiers that serve to define better the previous noun (parallel to `appos` in written texts)

A global view of `conj` usage in the last release of SUD if shown in this [table](http://tables.grew.fr/?data=sud_deps/conj).

### Chained conjuncts

In UD, all conjuncts of a coordination are attached to the head of the first conjunct in a bouquet.
In SUD, each conjunct is attached to the head of the previous one in a chain.

The first example below shows the annotation of a coordination in UD and the second one the corresponding annotation in SUD:

> English
{{< conll_ud >}}
1	John	John	PROPN	_	_	7	nsubj	_	_
2	,	,	PUNCT	_	_	3	punct	_	_
3	Mary	Mary	PROPN	_	_	1	conj	_	_
4	and	and	CCONJ	_	_	5	cc	_	_
5	Peter	Peter	PROPN	_	_	1	conj	_	_
6	will	will	AUX	_	_	7	aux	_	_
7	come	come	VERB	_	_	0	root	_	_
{{< /conll_ud >}}

> English
{{< conll >}}
1	John	John	PROPN	_	_	6	subj	_	_
2	,	,	PUNCT	_	_	3	punct	_	_
3	Mary	Mary	PROPN	_	_	1	conj:coord	_	_
4	and	and	CCONJ	_	_	5	cc	_	_
5	Peter	Peter	PROPN	_	_	3	conj:coord	_	_
6	will	will	AUX	_	_	0	root	_	_
7	come	come	VERB	_	_	6	comp:aux	_	_
{{< /conll >}}





## French

TODO
### Overview

### Specific Pattern




## Haitian Creole

TODO
### Overview

### Specific Pattern


