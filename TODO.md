### Dead or Alive

## FR

* [X] Aktuelle Version Stibie
* [X] Aktuelle Version Thomas
* [X] Introduction, Conclusion

## Samstag

* [X] Politur Intro, Conclusion
* [X] Einmal kurz überfliegen

## Sonntag

* [X] Zu Bernd
* [X] Abstract, Intro, Conclusions -> Antoine
* [X] Christophe
* [X] Abstract deutsch
* [X] Abstract Annika
* [X] Fehlende Plots machen
* [X] Mail an Promotionsbüro

## Montag

* [X] TODOs killen
* [X] Korrekturen einbauen
* [X] Intro, Conclusion Patricio

* [X] Vollständig lesen
* [X] Korrekturen einbauen

## Dienstag

* [X] abbreviations? fuckit
* [ ] Randnotizen ergänzen
* [ ] Korrekturen einbauen
* [ ] Layout und quirks
* [X] Vollständig lesen
* [X] Test-Druck und Bindung

## Mittwoch

* [ ] Thomas
* [ ] Christophe
* [ ] Antoine
* [ ] Rohlinge kaufen
* [ ] Zwei Einfache USB sticks (marke: kingston, sandisk)

* [ ] Vollständig lesen

## Donnerstag

* [ ] Drucken
* [ ] Durchsehen
* [ ] Abschicken

## Druckliste

* [ ] Lebenslauf MIT Foto
* [ ] sämtliche Anträge
* [ ] 5 Arbeiten!
* [ ] 
* [ ] Unterschrieben!!!!


### If I have time...

% TODO: without any overlap, count estimation would be useless... counting is a quantification of overlap

% TODO: discuss that music signals lack a proper source definition. Therefore counting on music signals in ill defined. However, it may work on some specific cases. We tried on ... but it didn't work.

# Bernd 19.10.2018

* [X] noch mal den Titel checken, deutsche Variante, vielleicht doch mehr in Richtung Modulation?
* [X] Dataset Kapitel ok oder überflüssig --appendix?

* [X] Tables und Figures in Appendix?
* [X] Common Fate interpretation mit plots (siehe fatimeh poster), aber future work
* [X] Grafiken aus IEEE publikationen übernehmen? nur hinweis bei IEEE und AES?
* [ ] Bei der vorstellung der Paper... alle Autoren inklusive Bernd?
* [X] Citation Style numerisch oder alphanumerisch ok?
* [X] Release WICE dataset
* [X] Commonfate: parafac2 fast release von Jeremy?
* [X] Fragen, ob Korrekturen später möglich sind und in welchem Umfang?
* [X] Publikationsliste inklusive neuer Publikationen! Auch in Thesis?

# General status

* [ ] reference all datasets
* [ ] appendix, filter plots from countnet
* [ ] Figures durchgehen
* [ ] Grafiken IEEE in Captions
* [ ] Literatur durchgehen (PAPERS folder! und löschen)
* [ ] Check website availability
* [ ] add gap statistics and elbow method and other clustering shit from wolfgangs diplomarbeit

# Fragen an Antoine

* Chapter 2 is a mix between a literature overview and a fundamentals chapter
* Why doesn't shift-invariant NMF solve the vibrato case? or does it?

# Is deep learning a black box?

No, but From Chollet
> The same is true of backprop in deep learning -- knowing how to code up backprop by hand gives you no useful knowledge wrt deep learning, and inversely, developing powerful mental models for deep learning does not in any way require knowing the algorithmic details of backprop

# Defense

## Questions

- What is common fate (read paper)

## Modulation

- why does FM cause AM?

## Count Estimation

- explain how to count
- gap statistics, elbow, BIC

## time warping by applying non-linear resampling

- normally its x(n) := f[n*t], how does it work for invariant pitch
- introducing a `timeScaleFactor = 1.0/targetPitch` so that we get a constant pitch

## Wackelkandidaten

- * For the linear mixing case, the process can be transferred to the frequency domain as the Fourier transform is a linear operator.
% However, since we are normally dealing with the non-negative magnitude representation this is only an approximation~\cite{klapuri06book}.

### NMF, NTF

- explain the beta divergence
- how to derive the cost functions
- Erklärung von Antoine/Vincent
- understand HR-NMF, shift-invariant-nmf, hennquin10
- warum kein WDO auf CFT? Siehe pardo journal oder response

### Separation

- Warum wiener filter für power spectrum?

### Backprop

- How does Guided Backpropagation work?
- http://blog.qure.ai/notes/deep-learning-visualization-gradient-based-methods

# Random s*** for my presentation

* [x] example that works quite nice... http://sisec17.audiolabs-erlangen.de/#/listen/20/STO1?mode=embed

# BEYOND EQUAL-LENGTH SNIPPETS: HOW LONG IS SUFFICIENT TO RECOGNIZE AN AUDIO SCENE? &* https://arxiv.org/pdf/1811.01095.pdf
