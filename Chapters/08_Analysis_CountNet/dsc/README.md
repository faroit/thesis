# Single-Channel Number of Concurrent Speaker Estimation Using Supervised Learning

Using a deep neural network to improve the performance on audio source counting.
Use the trained features to transfer to different task like male/female speaker
or stringed non-stringed instrument.

[Latest Paper PDF  taslp](https://git.audiolabs.uni-erlangen.de/stf/pub_sourcecount/builds/artifacts/taslp/file/stoeter_sourcecount.pdf?job=test)

## Abstract

This work addresses the problem of estimating the maximum number of concurrent speakers from single channel mixtures in a “cocktail-party” scenario. A correct estimate has applications in blind source separation, speaker diarization, and  surveillance. Due to the complex nature of the problem and its relation to source separation, a data-driven approach is chosen in this work. First, the efficiency of different convolutional and recurrent neural network architectures is investigated for the task of source number estimation, and a convolutional recurrent neural network architecture is proposed that is shown to have better performance for the proposed task. Furthermore comprehensive experiments were carried out to investigate the influence of the choice of input feature representation and excerpt duration on the performance of the different neural network architectures. In addition, it is shown that the way in which the problem is formulated also has an influence on the performance of the different neural networks. To this end, three different ways of problem formulation, namely, classification, basic regression and Poisson regression are investigated in this work. Furthermore, comparative evaluation of different architectures on single channel mixtures are shown for short (up to ten seconds) segments. Finally results show that the proposed method can correctly estimate up to five speakers whereas humans are typically only be able to correctly estimate up to three speakers.

--------------------------------------------------------------

## 1. Introduction
- Introduce the task of estimating the maximum number of concurrent speakers in a single channel mixture.

__(Applications)__
* Source Separation (count estimate make blind SS fully blind)
* Speaker Diarization (who speaks when) requires number of sources
* Surveillance (mention only)

Transition: Describe two ways of getting the number of speakers:
* Counting (identify first, then add up all unique speakers)
* Estimating (directly infer a count)

* Briefly explain differences between counting by detection and directly estimate a count
with respect to regression or classification. We want to directly estimate the count!
* Explain how humans count/estimate.
* Indications that humans are able to do directly estimate vision.
* How do humans do count and why can't machines?

__State-of-the-art__
Reference counting methods with restrictions to audio and concurrent speech.
* Single-channel vs. multi-channel (harder problem is single channel)

__(What is the gap?)__
* Existing single-channel methods require segments where only a single speaker is active.
* Overlap detection addresses single frames but does not take context into account.

__(Relations to to other tasks and introduction to Speaker Count Estimation)__
* Speaker Count estimation is a very abstract representation of the input data. This is where Deep Learning excels.
* Supervised / Deep Learning approaches have also been used successfully in related tasks such a source-separation, diarization, overlap detection, speech recognition.
* Speaker Count estimation inspired by recent advances in determining the number of objects in images.

__(List of Contributions)__
* Defining the problem of Estimating Number of Concurrent Sources.
* Influence of three different problem formulations: regression, poisson regression. classification
* Solution: Investigation of several deep learning architectures.
* Experiments aim to identify the learned strategy.

__(Organisation)__
* ...

--------------------------------------------------------------

## 2. Problem Formulation
introduce

### 2.1. Signal model and basic notations.
* Define tf-input spectrogram and the single output variable (integer count)

### 2.2. Estimation in a deep learning framework
* Mathematical task formulation as classification, (gaussian) regression, poisson regression
* Inference is using a secondary function to map to integer output.
* Learning using sets of inputs and outputs.

--------------------------------------------------------------

## 3. Supervised Learning for Count Estimation
A short review of deep learning architectures used for related tasks and proposal for count estimate architectures.
Reference image object counting networks.

### 3.1. Objective Functions for Count Estimation
* Describe matching loss functions in detail.
Describe the DNN networks output layers.
* Regression+MSE
* Classification+Softmax  
* Regression+Poisson Loss

### 3.2. DNN Architectures
Introduce our five basic architectures. For all of them we:
* reference the use cases, and the strengths and weaknesses,
* explain why and how they can be used for count estimation

#### 3.2.1. CNN
* good for local structure
* often used with many layers for hierarchical learning (then also global structure can be modeled)

#### 3.2.2. Recurrent/LSTM
* good for temporal dependencies.
* State-of-the-art speech recognition, NLP, Diarisation

#### 3.2.3. CRNN
* Combination of CNN and Recurrent

#### 3.2.4. CNNF
* using full frequency band filters.
* Very few Parameters, easy to train.

#### 3.2.5. CRNNF
* Also add recurrent.

--------------------------------------------------------------

## 4. Training
### 4.1. Dataset and Annotation
* Libri Speech  
* Describe the used VAD

### 4.2. Training data creation
* Reduce redundancy in training data by stochastic dataset sampling

### 4.3. Parameters
* Optimizer
* Early Stopping Criteria
* Other training factors that are common to all the experiments

--------------------------------------------------------------

## 5. Experiments
### 5.1. Metrics
* Mean Speaker Count Distance
* Response
* Accuracy
* Accuracy +/- 1

### 5.2. Training and Evaluation on 0dB LIBRIC Mixtures
Describe popular Input representations and why MFCCs are not used in
experiments, MEL  STFT, LOG STFT

* All mixtures have the same 0dB SNR to all others
* Trained on 20.000 Libri Speech Mixtures
* Number Speakers [0, 1, 2, ..., 10]
* Temporal Context (5s)
* Different Input Representations (STFT 400, MEL40, log(STFT + 1)))
* Different Output Objectives (classification, regression, p-regression)

* --> Fix Input Representation to STFT because of little influence
* --> Fix Output Objective to Classification for best overall performance

### 5.3. Evaluation on (up to 12db) LIBRIC Mixtures
* Pick: STFT, Classification
* 0db =1.0 gain randomly varied between 0.5 and 2.0
* Performance drops slightly

* --> CNN and CRNN, are most robust to gain variation

### 5.4. Evaluation on other datasets
* Pick best: CRNN, STFT, Classification
* TIMIT (slight drop)
* German Dataset (medium drop)
* THCS Chinese (large drop)

### 5.5. Effect of Reverberated Signals
* Pick best: CRNN, STFT, Classification
* Generated simulated using @hab RIR Generator
* test room: [3.5, 4.5, 2.5]
* receiver position at [1, 1, 1]
* generating 350 RIRs for each room: between 100ms and 500ms
* generating 10 unique positions for each room: min distance 0.1 to walls
* --> Significant Performance Drop (diff 2.0 MAE)
* Retrained using train room: [3, 4, 2] and valid room: [4, 5, 3]
* Performance back to (0.6 MAE) 👍


### 5.6. Effect of Duration
* Pick best: CRNN, STFT, Classification
* (Re) Trained and evaluated on (1s...9s)
* Longer context 👍
* Shorter context 👎

### 5.6. Listening Test
* Reference existing listening tests which report the same thing
* Are we really doing it? We can decide on this once the first full draft is ready.

--------------------------------------------------------------

## 6. Visualisations
Select best performing system (CRNN, Classification, STFT) and analyse how it achieves the performance.

* Layer Outputs
* Saliency maps
* Explore Gender dependencies
* Show same-speaker mixture
* Show 1-10 curve example

--------------------------------------------------------------

## 7. Conclusion
