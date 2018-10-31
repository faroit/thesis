
## Chapter 4 (challenges)

## why isn't there more research on on modulation based processing

Humans use amplitude modulation for their common grouping procedure.

> ~\cite{dau99}: It appears that the auditory system is very sensitive to slow modulations. Slow modulations are associated with the perception of rhythm. Samples of running speech, for example, show distributions of modulation frequencies with peaks around 3-4 Hz, approximately corresponding to the sequence rate of syllables (Plomp, 1983). Results from physiological studies have shown that, at least in mammals, the auditory cortex seems to be limited in its ability to follow fast temporal changes.

depending on the carrier frequency and the modulation frequency, humans describe modulations differently as fluctuation, roughness, or residue pitch (See Figure 2 in~\cite{joris04}).

~\cite{bacon89, dau99} showed that human perceptual limits of amplitude modulations can be modeled...

~\cite{mcadams89} showed that modulation cues are used to group sounds. 
--> Common fate

--> challanges

* tracking modulations is hard, because f0 estimation doesn't easily work on mixtures. Reason is that crossing partials is a big problem for sinusoidal modeling~\cite{viste03}

* modulations are not present in all signal types. so you need to be lucky 
* * Papers with detecting vibrato?
* Representations are now easily invertible

~\cite{scheirer99}
> technique  operates  by  discovering  common  modulation  behavior among groups of frequency subbands in the autocorrelogram domain.  

separating without understanding

Modulations spectrogram for speech are usually calibrated to 4 Hz modulation rate also from 

> ~\cite{greenberg96} the energy in the modulation spectrum may be derived from syllabic segmentation. This association is of interest in light of recent demonstrations that speech intelligibility is crucially dependent on the preservation of the portion of the modulation spectrum between 2 and 10 Hz

### Analysis Methods

Feature design ~\cite{lagrange10} for discriminative speech features

joint AM/FM method for CASA for\cite{abe98}

> Zwicker (324) showed that the threshold for detecting AM is very small at low modulation frequencies

Modulation based filterbanks are used for different purposes than vibrato. \cite{barker13} was tuned to medium rate modulations of speech

as seen in ~\cite{barker13}
1. filterbank
2. generate modulation for each filterbank channel (HWR?)
3. spectrum


~\cite{greenberg96}

> The modulation spectrum for an octave-wide channel, arithmetically centered at 1.5 kHz, computed from a single speaker's discourse over a two-minute interval is shown and compared with that of the distribution of syllable durations (transformed into equivalent modulation frequencies). The similarity between the two measurements suggests that much of the energy in the modulation spectrum may be derived from syllabic segmentation. This association is of interest in light of recent demonstrations that speech intelligibility is crucially dependent on the preservation of the portion of the modulation spectrum between 2 and 10 Hz.

TODO: ~\cite{betser08}...

TODO: [40] 40. Sukittanon, S., Atlas, L.E., Pitton, J.W.: Modulation-scale analysis for content identiﬁcation. IEEE Trans. Signal Process. 52(10), 3023–3035 (Oct 2004)

> \cite{sturm12} Modulation representations of acoustic signals describe the variation of spectral power in scale, rate, time and frequency. This approach has been motivated by the human auditory and visual systems [44, 15, 36, 40, 24].


### Separation Methods

*Common Amplitude Modulation*: the amplitude envelopes of different harmonics of the same source tend to be similar. ~\cite{bregman, wang06}

Virtanen Sinuoidal modeling
Separation using sinusoidal modeling is well suitable for vibrato
~\cite{virtanen00}

~\cite{creager16} VibratoNTF uses DOA 

~\cite{li09}, exploitung common amplitude modulation for source separation

### \cite{viste03}

> harmonic relation, the common onset, offset, amplitude modulation (AM), and frequency modulation (FM).These are all important cues for grouping.

## Chapter 8

Everything fits together:

## Analysis

