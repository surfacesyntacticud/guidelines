---
title: "Zaar"
weight: 3
bookToc: true
bookCollapseSection: true
---

# Zaar Guidelines


## UPOS

Distribution of `upos` in **SUD_Zaar-Autogramm**:

{{< agg zaar_pos_clust >}}

{{< grew key1="X.upos" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { X [upos] }
{{< /grew >}}

### `PUNCT`

The `PUNCT` upos is used to encode prosodic elements in the transcription.
{{< grew key1="X.form" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { X [upos=PUNCT] }
{{< /grew >}}

### `PART`

The `PART` upos is used with many lemmas in the Zaar treebank.
{{< grew key1="X.lemma" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { X [upos=PART] }
{{< /grew >}}

All `PART` have a feature `PartType`:
{{< grew key1="X.PartType" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { X [upos=PART] }
{{< /grew >}}

{{% hint info %}}
Comment convertir en UD. Pour UD [PART](https://universaldependencies.org/u/pos/PART.html) doit être utilisé de façon très restrictive. Il doit n'y avoir qu'un petit nombre de lemmes, qu'il faut déclarer (comme pour les AUX).

En fonction des `PartType` les `PART` sont presque toujours tête ou feuille: https://universal.grew.fr/?custom=68e29e3f5b1c3 &rarr; regarder les exceptions.
{{% /hint %}}


### `AUX`

The `AUX` tag is used with many lemmas:

{{< grew key1="X.lemma" corpus="SUD_Zaar-Autogramm@latest">}}
pattern { X [upos=AUX] }
{{< /grew >}}

{{% hint info %}}
54 lemmes différents pour les `AUX` (avec *count*). Problème pour la conversion UD où on doit déclarer chaque lemme séparément.

NB: pour le moment, on enlève les lemmes des AUX à la conversion pour esquiver le validateur là-dessus&nbsp;!

Quelques AUX qui ne sont pas dans une structure syntaxique attendue: https://universal.grew.fr/?custom=68e2a11dc1dda
{{% /hint %}}


