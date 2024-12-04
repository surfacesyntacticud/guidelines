---
title: "Beja"
weight: 3
bookCollapseSection: true
---

# Beja Guidelines
**NB:** This page is under construction. 

## Publication
A overview of the SUD annotation of the Beja corpus is available in the paper: [A morph-based and a word-based treebank for Beja](https://aclanthology.org/2021.tlt-1.5.pdf).

  

## Annotation at the morph level


The SUD corpus of Beja is firstly annotated at the morph level (`mSUD_Beja-Autogramm`).

In the UD repository, the word-based corpus is released as `UD_Beja-Autogramm`.

The two other combinations are also available:

 - `SUD_Beja-Autogramm` the data following SUD guidelines but at the word level
 - `mUD_Beja-Autogramm` the data following UD guidelines but at the morph level

The table below shows how the conversions are made in order to produce all the corpora described above.

|  | SUD | | UD |
|:-:|:-----:|:-:|:----:|
| **morph-based** | **`mSUD_Beja-Autogramm`** [![gh](/images/Octocat.png)](https://github.com/surfacesyntacticud/mSUD_Beja-Autogramm) [![gm](/images/square_g.svg)](https://universal.grew.fr/?corpus=mSUD_Beja-Autogramm@latest) | [&#x21e8;](https://github.com/surfacesyntacticud/tools/tree/master/converter) | `mUD_Beja-Autogramm_MB` [![gh](/images/Octocat.png)](https://github.com/UniversalDependencies/UD_Beja-Autogramm/tree/dev/not-to-release) [![gm](/images/square_g.svg)](https://universal.grew.fr/?corpus=mUD_Beja-Autogramm@conv) |
| | [&#x21e9;](https://github.com/surfacesyntacticud/tools/tree/master/morph2word) | | |
| **word-based** | `SUD_Beja-Autogramm` [![gh](/images/Octocat.png)](https://github.com/surfacesyntacticud/mSUD_Beja-Autogramm/tree/master/SUD_Beja-Autogramm) [![gm](/images/square_g.svg)](https://universal.grew.fr/?corpus=SUD_Beja-Autogramm@latest) | [&#x21e8;](https://github.com/surfacesyntacticud/tools/tree/master/converter) | **`UD_Beja-Autogramm`** [![gh](/images/Octocat.png)](https://github.com/UniversalDependencies/UD_Beja-Autogramm/tree/dev) [![gm](/images/square_g.svg)](https://universal.grew.fr/?corpus=UD_Beja-Autogramm@conv) |
