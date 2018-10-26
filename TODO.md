# Motivation

## why monoaural

Everything fits together:

Speech ~4Hz
Violon Vibraot ~5Hz

from Greenberg97
> It has been previously suggested that the broad peak at 4 Hz in the modulation spectrum corresponds to the average syllable rate [8].

[8] => ~\cite{Houtgast85}

Modulations spectrogram for speech are usually calibrated to 4 Hz modulation rate.

also from ~\cite{greenberg96}

> The modulation spectrum for an octave-wide channel, arithmetically centered at 1.5 kHz, computed from a single speaker's discourse over a two-minute interval is shown and compared with that of the distribution of syllable durations (transformed into equivalent modulation frequencies). The similarity between the two measurements suggests that much of the energy in the modulation spectrum may be derived from syllabic segmentation. This association is of interest in light of recent demonstrations that speech intelligibility is crucially dependent on the preservation of the portion of the modulation spectrum between 2 and 10 Hz.

* Because it allows to...

## why isn't there more research on on modulation based processing

* tracking modulations is hard, because f0 estimation doesn't easily work on mixtures. Reason is that crossing partials is a big problem for sinusoidal modeling~\cite{viste03}
* modulations are not present in all signal types. so you need to be lucky 
* * Papers with detecting vibrato?
* Representations are now easily invertible

## Gute Methode um Paper einzubetten... siehe \dau99

> Modied version of the paper \Modeling auditory processing of amplitude modulation: I. Detection and masking with narrowband carriers", written together with Birger Kollmeier and Armin Kohlrausch, submitted to J. Acoust. Soc. Am.

# Bernd 19.10.2018

- [ ] Begründung warum analyse nach synthese

* [ ] Common Fate interpretation
* [ ] NMF

- [ ] paper from fatimah nach referencen durchforsten


# introducing NMF like Dittmar:

> When using NMF for ADT, it is essential to choose a suitable rank R ∈ N of the approximation (i.e., number of components) and to provide a good initialization for W. One popular choice (see for example [7, 37, 158, 160]) is to set R to the number of distinct drum instruments and to initialize individual columns W (:, r) with averaged spectra of isolated drum sound events. The rationale is to let the NMF component updates start from a point in the parameter space that is already close to a meaningful local optimum.

# Software releases

* [ ] Release WICE dataset
* [ ] Commonfate: parafac2 release

# Bernd Fragen

* [ ] Parafac veröffentlichen
* [ ] Release common fate?

# General status

* [X] Write Common Fate DNN Section
* [X] Merge Counting Papers
* [ ] Redo Dataset Chapter
* [X] Fix bibliography of chapter 05 and 06
* [ ] NMF Example
* [X] Add CountNet
* [ ] add negative log likelihood
* [ ] add pescador training to count net paper.
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

Aus Justin Salamon und Sundberg 95

```
Vibrato rate V r : the frequency of pitch modulation, indicated by the location of the prominent peak of |P(k)| within the expected vibrato range (in Hz).

• Vibrato extent V e : the magnitude of said peak (in cents).

• Vibrato coverage V c : the ratio of samples with vibrato to the total number of samples in the contour (ranges between 0–1).
```

### Greenberg 97

2-12Hz: -> Smith93
<20Hz> -> Schreiner86

#### Schreiner86

Christoph Schreiner and John V. Urbas. Representation of amplitude modulation in the auditory cortex 

#### Smith93

kein plan

### Lagrange10

Instrument discriminitation

### Sturm2012~\cite{sturm12}

```
Sturm, B. L. (2012). On automatic music genre recognition by sparse representation classiﬁcation using auditory temporal modulations. In 9th Int. Symp. on Computer Music Modeling and Retrieval, pp. 379–394. London, UK. 157
```

> Modulation representations of acoustic signals describe the variation of spectral power in scale, rate, time and frequency. This approach has been motivated by the human auditory and visual systems [44, 15, 36, 40, 24].

Diverse Literatur aus Sturm:

[44] Wang, K., Shamma, S.A.: Spectral shape analysis in the central auditory system.
IEEE Trans. Speech Audio Process. 3(5), 382–395 (Sep 1995)

[15] Greenberg, S., Kingsbury, B.E.D.: The modulation spectrogram: in pursuit of an invariant representation of speech. In: Proc. IEEE Int. Conf. Acoust., Speech, Signal Process. pp. 1647–1650. Munich, Germany (Apr 1997)

[40] 40. Sukittanon, S., Atlas, L.E., Pitton, J.W.: Modulation-scale analysis for content identiﬁcation. IEEE Trans. Signal Process. 52(10), 3023–3035 (Oct 2004)

[28] Panagakis, Y., Benetos, E., Kotropoulos, C.: Music genre classiﬁcation: A multilinear approach. In: Proc. ISMIR. pp. 583–588. Philadelphia, PA (Sep 2008)
-> the first work where modulation characteristics where used 


### Scheirer99

Scheirer, E. D. (1999). Towards music understanding without separation: Segmenting music with correlogram comodulation. In IEEE Worksh. on Apps. of Signal Processing to Audio and Acoustics (WASPAA), pp. 99102. New Paltz, New York, USA. 18

### Sundberg 95

Sundberg, J. (1995). Acoustic and psychoacoustic aspects of vocal vibrato.
In P. Dejonckere, M. Hirano, & J. Sundberg (Eds.) Vibrato, pp. 35–62. San Diego: Singular Publishing Group. 84, 159

Very extensive study on vocal vibrato. of all different fazentten

### Betser

~\cite{betser08}

### \cite{viste03}

> harmonic relation, the common onset, offset, amplitude modulation (AM), and frequency modulation (FM).These are all important cues for grouping.

### Li Wang alias ~\cite{li09}

# DAU ~\cite{dau99} Dissertation

Humans use amplitude modulation for their common grouping procedure.

> It appears that the auditory system is very sensitive to slow modulations. Slow modulations are associated with the perception of rhythm. Samples of running speech, for example, show distributions of modulation frequencies with peaks around 3-4 Hz, approximately corresponding to the sequence rate of syllables (Plomp, 1983). Results from physiological studies have shown that, at least in mammals, the auditory cortex seems to be limited in its ability to follow fast temporal changes

model is for modulation > 10 hz.
in the input signal but, on the other hand, the cortex is capable of processing rhythm-like envelope uctuations.

Modeling auditory processing of amplitude modulation. 



### Summary
Modulation based filterbanks are used for different purposes than vibrato. \cite{barker13} was tuned to medium rate modulations of speech

## Joris

Joris, P. X., Schreiner, C. E., and Rees, A., “Neural processing of amplitude-modulated sounds,” Physiological Reviews, vol. 84, no. 2, pp. 541–577, 2004. [Online]. Available: http://physrev.physiology.org /content/84/2/541

## Virtanen Sinuoisdal modeling

~\cite{virtanen00}

# binary mask:

# ON THE DISJOINTESS OF SOURCES IN MUSIC USING DIFFERENT TIME-FREQUENCY
REPRESENTATIONS
Dimitrios Giannoulis, Daniele Barchiesi, Anssi Klapuri and Mark D. Plumbley

# Cocktail Party Separation stuff

* [ ] Haykin, S. & Chen, Z. (2005). The cocktail party problem. Neural Comput., 17(9), 1875–902.
* [ ] originally by  Cherry, E. C. (1957). On human communication: A review, survey, and a criticism. Cambridge, MA: MIT Press.]]

# Perception

* [ ] Bregman book
* [ ] CASA Buch
* [ ] Moore, B. C. J. (2012). An Introduction to the Psychology of Hearing. Brill, Leiden, The Netherlands, 6th edition.

# Signal Processing Basics

@book{Klapuri2006,
 author = {Klapuri, Anssi and Davy, Manuel},
 title = {Signal Processing Methods for Music Transcription},
 year = {2006},
 isbn = {0387306676},
 publisher = {Springer-Verlag},
 address = {Berlin, Heidelberg},
}

## DSP GURUS
A. V. Oppenheim and R. W. Schafer. Discrete-Time Signal Processing. Pearson, 3rd edition, 2009. ISBN 0131988425.

% TODO: Voran, S., “Exploration of the additivity approximation for spectral magnitudes,” in 2015 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), Oct 2015, pp. 1–5.

## FFT:
J. W. Cooley and J. W. Tukey. An algorithm for the machine calculation of complex fourier series. Mathematics of Computation, 19(90):297–301, 1965.

## separation

Goto, M. (2007). Active music listening interfaces based on signal processing. In Acoustics, Speech and Signal Processing, 2007. ICASSP 2007. IEEE International Conference on, vol. 4, pp. IV–1441. IEEE. [Cited on pages 3 and 12.]

# NMF Literature
Daniel D. Lee and H. Sebastian Seung. Algorithms for non-negative matrix factorization. In Proceedings of the Neural Information Processing Systems (NIPS), pages 556–562, Denver, CO, USA, 2000.

# Modulation

# Warping based Warped Separation

\cite{wang95} is using frequency warping to

> Frequency-warped signal processing is useful for the analysis of sinusoidal signals with varying frequency.

> Frequency warping a signal p(t) is nothing more than multiplying it by a unit amplitudee phase factor p(t). To invert the frequency warping we simply multiply the result.

```
...as discussed in Section 2.1, the Fourier transform is ill-suited for analyzing signals with rapidly varying parameters. By frequency warping a signal, i.e., selectively frequency modulating it, it may be possible to transform it so that the resulting signal is stationary and has a simplied spectrum which is more amenable to analysis. Frequency warping may be thought of as attempting to \straighten out" nonstationarities due to continuous variations in the instantaneous frequency of a signal.
```

FM nach wang:

$ z ( t ) = A \exp \left\{ j 2 \pi f _ { 0 } t + j m \sin \left( 2 \pi f _ { m } t \right) \right\} $

where A is the amplitude, f_0 is the carrier frequency, f_m is the modulation frequency, and m is the modulation index dened as

$ m = \frac { d } { f _ { m } } $

It is well known that the Fourier spectrum of z(t) may be quite complex. The FM-synthesis algorithm by Chowning [32] takes advantage of this fact, providing a computationally ecient way of producing musical sounds. In particular, z(t) may be represented as a Fourier series expansion

$ \begin{aligned} z ( t ) & = A \exp \left( j 2 \pi f _ { 0 } t \right) \exp \left\{ j m \sin \left( 2 \pi f _ { m } t \right) \right\} \\ & = A \exp \left( j 2 \pi f _ { 0 } t \right) \sum _ { k = - \infty } ^ { \infty } J _ { k } ( m ) \exp \left( j 2 \pi k f _ { m } t \right) \end{aligned} $

taking the idea from \cite{wulich92} which make use of time warping to analyze FM signals using variable rate sampling.

durchsehen (aus Wang phd thesis, chapter separation):

[42] A. de Cheveigne, \Strategies for voice separation based on harmonicity." To be presented at ICSLP, Yokohama.

[43] A. de Cheveigne, \Separation of concurrent harmonic sounds: Fundamental frequency estimation and a time-domain cancellation model of auditory processing," J. Acoust. Soc. Am., vol. 93, pp. 3271{3290, June 1993.

[44] A. de Cheveigne, \Time-domain combltering for speech separation," Technical Report TRH-016, ATR Human Information Processing Research Laboratories, 2-2, Hikaridai, Seika-cho, Soraku-gun, Kyoto 619-02 Japan, July 1993.

[45] A. de Cheveigne, H. Kawahara, K. Aikawa, and A. Lea, \Speech separation for speech recognition," Journal de Physique IV, vol. 4, pp. C5{545{C5{548, May 1994.

[46] A. de Cheveigne, S. McAdams, J. Laroche, and M. Rosenberg, \Identication de voyelles simultanees harmoniques et inharmoniques," Journal de Physique IV, vol. 4, pp. C5{553{C5{ 556, May 1994.

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

# Random s*** for my presentation

* [x] example that works quite nice... http://sisec17.audiolabs-erlangen.de/#/listen/20/STO1?mode=embed
