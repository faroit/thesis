# Modulations


AM is mostly analyed by the envelope
FM causes AM

rate, extend

# Aspects of modulations for audio signals

## Communications Engineering

textbook. Radio transmission...
transmission of a signal using a modulator/demodulator (modem) system

- rate: audio rate (up to 0-20 kHz or higher (example))
- source: any function, or audio signal
- target: amplitude, frequency, phase

### AM

### FM

In telecommunication, the modulator is a signal that modifies a carrier function for the purpose of carrying information. 
amplitude modulation, frequency modulation, phase modulation...

## Modulations in Music

modulations are a core part of mastering and instrument.

> a good vibrato in music is a periodic pulsation, generally involving pitch, intensity, and timbre, which produces a pleasing flexibility, mellowness and richness of tone. \cite{seashore31} 

### Traditional Instruments

~\cite{fletcher01}… “Vibrato is an oscillation in pitch, loudness or timbre of a musical performance” and it is produced by “conscious physical manipulation”.
5-8 Herz.
Usually a combination of AM and FM, depending on the instrument.

1st class: plucked, bowed strings and vocal folds, where the primary excitation oscillator is modulated in frequency.

2nd class: woodwind and brass sounds, where the resonator is modulated.

Carson bandwidth.

- rate: 5-8 Hz
- source: sinusoidal function
- target: amplitude, frequency, phase

## Electronic Instruments

LFO Synthesizers, FM Synthesis (~\cite{chowning73}), and also FM synthesis

However electric pianos like Rhodes or Wurlitzer can generate a tremolo effect which is just a different name for sinusoidal amplitude modulation.

often tremolo is used for AM vibrato, but for real instruments very rarely this is the case. Instead real instruments do use.

- rate: 0-20 kHz
- source: any periodic function
- target: oscillator frequency

## Singing Voice

vocal system is a pulsation of subglottal pressure. Itself some kind of AM
Vocal tract shape rhythmically moving

\cite{desain99}

\cite{sundberg94} Very extensive study on vocal vibrato. of all different fazentten

from \cite{sundberg94}
> The main perceptual effect of the vibrato is dependent upon the frequency modulation and it is generally quite hard to focus one's attention on the amplitude fluctuations.

~\cite{sundberg}
```
Vibrato rate, which is the frequency of modulation in Hz).
Vibrato extent, the magnitude of said peak (in cents).
```

General psychoacoustic theory: \cite{bregman}

Fletcher defiens vibrato as ``...an oscillation of pitch, loudness or timbre of a musical tone...''~\cite{fletcher01}.

* often modulations are combined.
* there are two ways to get a modulation index.

> sundberg: The vibrato tones were characterized by a fundamental frequency undulation at a rate of 5 to 7 undulations per second and an extent of about *1 semitone.

- rate: 5-7 Hz
- source: sinusoidal, triangular, trapezoidal
- target: frequency, amplitude

## Modulations in Speech

Speech ~4Hz

from Greenberg97

> It has been previously suggested that the broad peak at 4 Hz in the modulation spectrum corresponds to the average syllable rate [8].

[8] => ~\cite{plomp83, Houtgast85}

Humans use amplitude modulation for their common grouping procedure.

> ~\cite{dau99}: It appears that the auditory system is very sensitive to slow modulations. Slow modulations are associated with the perception of rhythm. Samples of running speech, for example, show distributions of modulation frequencies with peaks around 3-4 Hz, approximately corresponding to the sequence rate of syllables (Plomp, 1983). Results from physiological studies have shown that, at least in mammals, the auditory cortex seems to be limited in its ability to follow fast temporal changes.

depending on the carrier frequency and the modulation frequency, humans describe modulations differently as fluctuation, roughness, or residue pitch (See Figure 2 in~\cite{joris04}).

roughness and residue pitch can usually not considered as slow modulations but rather medium to fast modulations up to a few hundred Herz.

- rate: 2-10 Hz
- source: syllable durations, glottal pulse, 
- target: vocal folds

## physiological

\cite{zwicker52, plomp93, fastl90}
Deep neural study to analyse what is the reason why the human auditory system can detect amplitude modulations so well~\cite{joris04}.

The upper limit of modulation detection extends to 2.2 kHz

<20Hz -> ~\cite{schreiner88}

~\cite{plomp93} showed that the cortex is capable of processing rhythm-like envelope fluctuations.

## Pathological

* vocal tremor \cite{ramig87}
* Parkinson shaking~\cite{botzel14}
* Because it allows to...


## Chapter 4 (challenges)

## why isn't there more research on on modulation based processing

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

