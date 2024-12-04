---
title: "comp & subrels"
weight: 3
# bookFlatSection: false
# bookToc: true
# bookHidden: false
# bookHidden: false
bookCollapseSection: true
# bookComments: false
# bookSearchExclude: false
---

# `comp` and extensions 

## Universal

The `comp` relation is used for arguments of verbs, nouns, adjectives, adverbs, auxiliaries, adpositions and conjunctions.

This relation is refined into several extensions: 
 - [`comp:aux`](./comp_aux) (auxiliary argument)
 - [`comp:cleft`](./comp_cleft) (cleft clauses)
 - [`comp:obj`](./comp_obj) (direct object)
 - [`comp:obl`](./comp_obl) (oblique argument)
 - [`comp:pred`](./comp_pred) (predicative argument)

In most cases, SUD native corpora are directly annotated with the extensions, rather than with the `comp` relation.
However, `comp` may sometimes be used when one has difficulty deciding between `comp:obj` and `comp:obl`.

A global view of `comp` usage in the last release (2.13) of SUD if given in this [table](http://tables.grew.fr/?data=sud_deps/comp).
