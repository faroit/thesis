### MY THESIS

humans are not good a counting larger numbers. So its easy for machines to improve on this. This is not AI!

Problem statement or Hypothesis
Why is this a Hard Problem
Approach or Methodology 
Why is this Innovative
Assumptions and Constraints
Initial Results (Promise of Great Things to Come) 
Validation Plan
Limitations and Applicability
Expected Contributions
What’s beyond this thesis
Roadmap of Thesis

### Generalized Wiener Filter Reconstruction

$$
\begin{array} { c } { \text { which are applied to the complex mixture spectrogram } \mathbf { X } ^ { * } \text { with elementwise } } \\ { \text { multiplication, so produce the speech spectrogram } \mathbf { S } ^ { * } } \\ { \mathbf { S } ^ { * } = \mathbf { X } ^ { * } \otimes \frac { \mathbf { Y } _ { s } } { \mathbf { Y } _ { s } + \mathbf { Y } _ { n } } } \end{array}
$$

# Add research questions

## why monoaural?

* Make sure that modulation are also used to analyze time frequency
* why counting
* Separation has relevancy for audio coding~\cite{herre12}

## Random shit

* add liutkus15c reference for wiener filtering
* common fate plots from https://www.researchgate.net/profile/Fatemeh_Pishdadian/publication/328540398_MULTI-RESOLUTION_COMMON_FATE_TRANSFORM/links/5bd34823299bf1124fa62805/MULTI-RESOLUTION-COMMON-FATE-TRANSFORM.pdf

# Bernd 19.10.2018

* [X] noch mal den Titel checken, deutsche Variante, vielleicht doch mehr in Richtung Modulation?
* [X] Dataset Kapitel ok oder überflüssig --appendix?

* [X] Tables und Figures in Appendix?
* [X] Common Fate interpretation mit plots (siehe fatimeh poster), aber future work
* [X] Grafiken aus IEEE publikationen übernehmen? nur hinweis bei IEEE und AES?
* [X] Bei der vorstellung der Paper... alle Autoren inklusive Bernd?
* [X] Citation Style numerisch oder alphanumerisch ok?
* [X] Release WICE dataset
* [ ] Commonfate: parafac2 fast release von Jeremy?
* [X] Fragen, ob Korrekturen später möglich sind und in welchem Umfang?
* [X] Publikationsliste inklusive neuer Publikationen! Auch in Thesis?

# General status

* [X] NMF Example + Figures --> Mathieu
* [X] Add chapter summaries --> Stibie, Patricio, Thomas

* [ ] Table 2.1, Introduction, Fundamentals, NMF, Conclusion --> Patricio
* [ ] remove numbering from contributions
* [ ] Write Introduction --> Christophe, Antoine
* [ ] Countnet nochmal lesen
* [ ] add negative log likelihood
* [ ] add pescador training to count net paper.
* [ ] reference all datasets
* [ ] appendix, filter plots from countnet
* [X] check the wording for magnitude spectrogram (check mainards book)
* [ ] add step-count plot
* [ ] Figures durchgehen
* [ ] Grafiken IEEE
* [ ] Tabelltenverzeichnis, Figureverzeichnis etc
* [ ] Check website availability
* [ ] add gap statistics and elbow method and other clustering shit from wolfgangs diplomarbeit

# Allgemeine Fragen


# Fragen an Antoine

* Chapter 2 is a mix between a literature overview and a fundamentals chapter
* For the linear mixing case, the process can be transferred to the frequency domain as the Fourier transform is a linear operator.
% However, since we are normally dealing with the non-negative magnitude representation this is only an approximation~\cite{klapuri06book}.
* Aim, Objective?
* Why doesn't shift-invariant NMF solve the vibrato case? or does it?
* Do you think I should add the SiSEC 2018 paper?
* Every chapter conclusion should be read so that it does't steal from the final conclusion. If a sentence in a chapter conclusion is not close enough bounded to the actual chapter topic, it should better go into the --> final conclusion
* 

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

# binary mask:

# ON THE DISJOINTESS OF SOURCES IN MUSIC USING DIFFERENT TIME-FREQUENCY
REPRESENTATIONS
Dimitrios Giannoulis, Daniele Barchiesi, Anssi Kliapuri and Mark D. Plumbley

# Cocktail Party Separation stuff

* [ ] Haykin, S. & Chen, Z. (2005). The cocktail party problem. Neural Comput., 17(9), 1875–902.
* [ ] originally by  Cherry, E. C. (1957). On human communication: A review, survey, and a criticism. Cambridge, MA: MIT Press.]]

# Perception

* [ ] Bregman book
* [ ] CASA Buch
* [ ] Moore, B. C. J. (2012). An Introduction to the Psychology of Hearing. Brill, Leiden, The Netherlands, 6th edition.

# Signal Processing Basics

## separation

Goto, M. (2007). Active music listening interfaces based on signal processing. In Acoustics, Speech and Signal Processing, 2007. ICASSP 2007. IEEE International Conference on, vol. 4, pp. IV–1441. IEEE. [Cited on pages 3 and 12.]

# NMF Literature
Daniel D. Lee and H. Sebastian Seung. Algorithms for non-negative matrix factorization. In Proceedings of the Neural Information Processing Systems (NIPS), pages 556–562, Denver, CO, USA, 2000.

# Warping based Warped Separation

\cite{wang95} is using frequency warping to

> Frequency-warped signal processing is useful for the analysis of sinusoidal signals with varying frequency.
> Frequency warping a signal p(t) is nothing more than multiplying it by a unit amplitudee phase factor p(t). To invert the frequency warping we simply multiply the result.

```
...as discussed in Section 2.1, the Fourier transform is ill-suited for analyzing signals with rapidly varying parameters. By frequency warping a signal, i.e., selectively frequency modulating it, it may be possible to transform it so that the resulting signal is stationary and has a simplied spectrum which is more amenable to analysis. Frequency warping may be thought of as attempting to \straighten out" nonstationarities due to continuous variations in the instantaneous frequency of a signal.
```

taking the idea from \cite{wulich92} which make use of time warping to analyze FM signals using variable rate sampling.


## time warping by applying non-linear resampling

- normally its x(n) := f[n*t], how does it work for invariant pitch
- introducing a `timeScaleFactor = 1.0/targetPitch` so that we get a constant pitch

# Counting

% @article{KREMS2018,
% title = "Why are conversations limited to about four people? A theoretical exploration of the conversation size constraint",
% journal = "Evolution and Human Behavior",
% year = "2018",
% issn = "1090-5138",
% doi = "https://doi.org/10.1016/j.evolhumbehav.2018.09.004",
% url = "http://www.sciencedirect.com/science/article/pii/S1090513818301491",
% author = "Jaimie Arona Krems and Jason Wilkes"
% }

HURON, D. (1989a). Characterizing musical textures. In T. Wells
& D. Butler (Eds.), Proceedings of the 1989 international computer music conference (pp. 131–134). San Francisco, CA:
Computer Music Association.

Musical textures

Broze, Y., Paul, B., Allen, E., & Guarna, K. (2014). Polyphonic Voice Multiplicity, Numerosity, and Musical Emotion Perception. Music Perception: An Interdisciplinary Journal, 32(2), 143-159. doi:10.1525/mp.2014.32.2.143

> The excerpts’ short length could create further problems, as stream segregation appears to be cumulative (see Bregman, 1978):
listeners tend to hear one stream at first before subsequently resolving more. In all, because our stimuli are both short and isotextural, counting would not be expected to be a successful strategy in the present denumeration task.

# Is deep learning a black box? 

No, but From Chollet
> The same is true of backprop in deep learning -- knowing how to code up backprop by hand gives you no useful knowledge wrt deep learning, and inversely, developing powerful mental models for deep learning does not in any way require knowing the algorithmic details of backprop

# * add sampling reference paper from ISMIR 2018 tutorial slides

# Outlook

BEYOND EQUAL-LENGTH SNIPPETS: HOW LONG IS SUFFICIENT TO RECOGNIZE AN AUDIO SCENE? https://arxiv.org/pdf/1811.01095.pdf


# Defense 

## Wackelkandidaten


### NMF, NTF

- how to derive the cost functions
- Erklärung von Antoine/Vincent

### Backprop

- Guided Backpropagation
- http://blog.qure.ai/notes/deep-learning-visualization-gradient-based-methods

# Random s*** for my presentation

* [x] example that works quite nice... http://sisec17.audiolabs-erlangen.de/#/listen/20/STO1?mode=embed
