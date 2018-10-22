# Bernd 19.10.2018

- analyse nach synthese

* [ ] Common Fate interpretation
* [ ] NMF

Daniel D. Lee and H. Sebastian Seung. Algorithms for non-negative matrix factorization. In Proceedings of the Neural Information Processing Systems (NIPS), pages 556–562, Denver, CO, USA, 2000.


Dittmar:

> When using NMF for ADT, it is essential to choose a suitable rank R ∈ N of the approximation (i.e., number of components) and to provide a good initialization for W. One popular choice (see for example [7, 37, 158, 160]) is to set R to the number of distinct drum instruments and to initialize individual columns W (:, r) with averaged spectra of isolated drum sound events. The rationale is to let the NMF component updates start from a point in the parameter space that is already close to a meaningful local optimum.

# TODO

Release WICE dataset

# TODO references

# Bernd Deadline

* [X] Write Common Fate DNN Section
* [X] Merge Counting Papers
* [ ] Redo Dataset Chapter
* [X] Fix bibliography of chapter 05 and 06
* [ ] NMF Example
* [ ] Add CountNet
* [ ] add negative log likelihood
* add pescador training to count net paper.

# Zenodos

* [ ] Countit Responses: 10.5281/zenodo.1467968
* [ ] Unison Dataset


# Tasks for Highly Overlapped sources

Source Separation Literature and basic techniques
Source Counting literature

Aber wie soll das funktionieren für counting. Es gibt keine basic techniques die funktionieren. Daher passt da snicht so gut rein.

# Aspects of Concurrency

* Analysis

What is a good metric of concurrency? Timbre/Dense doesn't really work, because it is hard to quantify.
Better is just counting, but count what?

number concurrent sources, number of different sources, maximum number of sources
Detection vs Subitizing vs

ICA war entry-study... daher so einfache Frage

* Separation

Count by detection is not useful

SEPARATION OF HARMONIC STRUCTURES BASED ON TIED GAUSSIAN MIXTURE
MODEL AND INFORMATION CRITERION FOR CONCURRENT SOUNDS

Auditory scene analysis based on time-frequency integration of shared FM and AM

 # counting

 discuss that music signals lack a proper source definition. Therefore counting on music signals in ill defined. However, it may work on some specific cases. We tried on ... but it didn't work.

# Literatur zu Anwendung von Modulationen für Audio Anwendungen

* https://hal.archives-ouvertes.fr/hal-01316485/document durchgehen nach Referenzen
* aus ewert: https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/15689/Ewert%20Template-Based%20Vibrato%20Analysis%202016%20Accepted.pdf?sequence=1
* aus jon barkers PHD thesis

* add sampling reference paper from ismir 2018 tutorial slides
