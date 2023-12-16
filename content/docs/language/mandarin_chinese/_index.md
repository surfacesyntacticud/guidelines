---
title: "Mandarin Chinese"
weight: 3
bookCollapseSection: true
---

# Mandarin Chinese Guidelines 

This sections outlines various features and annotation conventions useful for the annotation of Mandarin Chinese.

## Current discussion
### 没 (mei) 
This important character, 没 (méi), is a marker of negation. It can negate the perfective aspect marker 有 (yǒu), the existential 有 (yǒu), or any verb in the perfective aspect, such as in 我没吃 (wǒ méi chī), meaning "I didn't eat".

In many cases, the 没有 (méiyǒu) construction is simplified to just 没 (méi). It's a matter of debate whether, in these cases, we should continue to annotate 没 (méi) as an adverb (ADV) or if it should take the part of speech of the character 有 (yǒu) that disappears.


### 听说 (tingshuo) 
What is the dependency ?
- It can't be a compound:svc as the doer is not the same in both verb (I heard (other people) said)
- It can't be a comp:res as SAY is not the result of LISTEN

It seems to me that it's either a normal comp:obj, or a /m relation. As we can insert a noun or a pronoun between both characters, I (KG) think it's a comp:obj