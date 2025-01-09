# `mod` or `discourse` ?

In Spoken, we much more use the relation `discourse`, because there is much more discourse marker in oral productions, but also because we become aware that some units can be discourse markers rather than modifiers.  
Nevertheless, even in Spoken, we often hesitate between discourse and mod and some annotations are not very consistent. For instance, *en fait* is analyzed in both ways for similar constructions:

{{<grew key1="e.label" corpus="SUD_French-ParisStories@latest" >}}
pattern { e:Y -> X1; X1 [lemma="en"]; X2 [lemma="fait"]; X1 < X2 }
{{</grew>}}

One test we can use for distinguishing both constructions is the clefting: typical modifiers can be clefted while discourse markers cannot:

> _il a répondu **sans hésiter**_ &rarr; _c'est **sans hésiter** qu'il a répondu_

> _**bon** c'est pas gagné_ &rarr; _*c'est **bon** que c'est pas gagné_

Some adverbs cannot be clefted:

> _il est **toujours** content_ &rarr; _*c'est **toujours** qu'il est content_

but these adverbs are clearly modifiers and the test is not required.  
The test is only needed for small units which are prosodically detached.  
According to that, *en fait* or *du coup* should be analysed as `discourse`.

This analysis will also be applied to so called "sentence adverbs":

> _il a répondu **franchement**_ => _franchement_ is `mod`

> _**franchement** c'est pas gagné_ => _franchement_ is `discourse`