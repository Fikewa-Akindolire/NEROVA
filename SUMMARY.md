# Neurova — Project Summary
**EEG-Based Pain Detection for Non-Verbal Patients**
Morgan State University | Fikewa Akindolire | May 2026

---

## The Problem I Was Trying to Solve

There's a group of patients that medicine has always struggled to help — people who are in pain but have no way to tell anyone. Patients on ventilators. People in late-stage dementia. Stroke survivors. Premature infants. For these patients, the standard "rate your pain from 1 to 10" question is completely useless.

The tools we currently use aren't much better. Nurses observe facial expressions and body movements and make a judgment call. That judgment varies between staff members, it can only happen during scheduled check-ins, and it relies entirely on the patient showing visible signs at exactly the right moment. A patient can be in serious pain for an hour between rounds and nobody knows.

That bothered me. And I wanted to build something that addressed it.

---

## What Neurova Is

Neurova is a prototype pain monitoring system that uses a consumer-grade EEG headset to read brainwave activity in real time and translate it into a continuous, objective pain score — no patient input required.

The idea is simple: pain changes your brain. Alpha waves, the calm resting rhythm your brain produces when you're relaxed, get suppressed when pain is present. Theta waves, associated with pain processing in the anterior cingulate cortex, increase. These changes are measurable, reproducible, and documented in peer-reviewed neuroscience research. Neurova captures those changes passively and continuously and turns them into a number a clinician can actually act on.

The hardware is a Muse 2 EEG headset — four electrodes, 256 samples per second, about $250. The entire software stack is open source. No specialized clinical equipment. No proprietary systems.

---

## Features

- **Live EEG Streaming** — Real-time brainwave data streamed from the Muse 2 via Bluetooth at 256 Hz across four channels covering the forehead and ears
- **Personal Baseline Calibration** — The system establishes your individual resting state first and measures all pain readings as deviations from your personal baseline, not a universal average
- **Frequency Band Analysis** — Alpha (8–12 Hz) and theta (4–8 Hz) power extracted using Fast Fourier Transform applied in sliding windows across the full recording
- **Continuous Pain Score** — A normalized 0–10 score derived from how far your brain activity has deviated from your own resting state, updated continuously
- **Alert Threshold** — A configurable threshold that flags when the pain score reaches a clinically meaningful level
- **Side by Side Visualization** — Resting baseline and pain session plotted together with the pain window annotated so the difference is immediately visible
- **CSV Data Export** — Every recording saved as a timestamped CSV for analysis, reproducibility, and future model training
- **Open Source Stack** — Everything built on free tools so anyone can replicate, extend, or build on this work

---

## The Science Behind It

The foundation here isn't new — it's established neuroscience. Pain produces consistent, measurable changes in EEG frequency bands documented across multiple peer-reviewed studies.

Alpha wave activity (8–12 Hz) dominates when the brain is relaxed. When pain is present that signal gets suppressed — the brain shifts out of its resting rhythm. Theta wave activity (4–8 Hz) increases during pain processing, particularly in the anterior cingulate cortex, a region closely tied to how the brain perceives and responds to pain stimuli.

These markers have been validated by Ploner et al. (2017), Gram et al. (2017), and Peng et al. (2019). Neurova applies those findings using accessible hardware to see if they hold up in a real prototype environment.

---

## How I Built It

**Hardware:** Muse 2 EEG headset connected via Bluetooth to a Windows laptop

**Software:** muselsl for streaming, Python (numpy, pandas, matplotlib, scipy) for analysis, Jupyter for the notebook pipeline

**Experiment:** I used the Cold Pressor Task as my pain stimulus — submerging a hand in ice water. It's a widely accepted and ethically sound laboratory pain method used in hundreds of published pain studies. It produces a reliable, controllable pain response without any lasting harm.

**Protocol:** Two minute resting baseline with eyes closed → three minute pain stimulus recording with a 30 second rest window before the stimulus begins → frequency band analysis comparing the two sessions

The personal baseline calibration was important to me. Brainwave patterns vary significantly between individuals. Rather than comparing someone against a population average, Neurova measures each person against themselves. That makes the system more accurate and more honest about what it's actually detecting.

---

## What I Built and What I Found

Here's what I actually completed on this project:

- Got the Muse 2 streaming live EEG data via Bluetooth using muselsl and confirmed clean signal acquisition across all four channels
- Built a full Python analysis pipeline in Jupyter covering data loading, raw signal visualization, FFT-based frequency extraction, and pain score computation
- Recorded real human EEG data across two experimental conditions — resting baseline and cold pressor pain stimulus
- Ran the analysis on real data and found that the pain score crossed the alert threshold of 5 out of 10 multiple times during the stimulus window, peaking at 9 and 10 during moments of highest discomfort
- Validated that the EEG signal shows a measurable, visible physiological response to pain stimulus even with consumer-grade hardware
- Documented the full protocol so it can be replicated
- Built and published this repository with the full codebase and setup instructions

The results aren't clinical validation — this is one subject, one session, a consumer device. But they are a proof of concept. The signal responds. The system detects it. That's what this phase was designed to show.

---

## Why This Matters

Pain is universal. The inability to communicate it shouldn't determine whether you receive treatment. The current standard of care for non-verbal patients relies on human observation that is inherently limited — it can only happen when someone is in the room, it varies between observers, and it can't run continuously.

A passive, continuous, objective signal changes that equation. This project demonstrates that the technology to build it exists, it's affordable, and it works well enough at the prototype level to justify the next phase of development.

The next phase is machine learning classification trained across multiple subjects and a conversational AI layer that generates plain-language summaries for clinical staff. Instead of a chart, a nurse gets a message: patient in bed 4 has shown elevated pain indicators for the past 15 minutes. That's the vision.

---

## Research Question

Can consumer-grade EEG technology, combined with signal processing and personal baseline calibration, provide a reliable and continuous objective pain indicator for non-verbal patients as a viable alternative to behavioral observation scales?

---

## References

- Ploner, M., et al. (2017). Brain Rhythms of Pain. *Trends in Cognitive Sciences.*
- Gram, M., et al. (2017). Prediction of postoperative opioid analgesia using clinical-experimental parameters and electroencephalography. *European Journal of Pain.*
- Peng, W., et al. (2019). Alpha transcranial alternating current stimulation modulates pain anticipation and perception in a context-dependent manner. *PubMed.*

---

*Built with Muse 2 EEG · muselsl · Python · Jupyter*
