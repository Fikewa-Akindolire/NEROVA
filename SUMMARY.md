# Neurova — Project Summary
**EEG-Based Pain Detection for Non-Verbal Patients**
Morgan State University | Researcher: Fikewa Akindolire | May 2026

---

## Problem

Millions of clinical patients cannot communicate pain. Current tools like CPOT require nurses to manually observe patients — subjective, inconsistent, and unable to run continuously. Patients suffer silently between check-ins.

---

## Solution

Neurova is a prototype EEG-based pain monitoring system that reads brainwave activity in real time and translates neural signals into a continuous, objective pain indicator. Using a consumer-grade Muse 2 EEG headset ($250), the system streams four channels of brainwave data at 256 Hz, processes the signal for pain-associated frequency patterns, and displays a live visualization.

The system requires no patient cooperation. It works passively and continuously.

---

## The Science

Alpha wave activity (8–12 Hz), dominant during rest, becomes suppressed when pain is present. Theta wave activity (4–8 Hz) increases during pain processing in the anterior cingulate cortex. These markers are validated in peer-reviewed research by Ploner et al. (2017), Gram et al. (2017), and Peng et al. (2019).

---

## Methodology

**Hardware:** Muse 2 EEG headset, Windows laptop with Bluetooth
**Software:** muselsl, Python (numpy, pandas, matplotlib, scipy), Jupyter
**Experiment:** Cold Pressor Task — validated laboratory pain stimulus using brief ice water exposure
**Protocol:** 2-minute resting baseline → pain stimulus recording → frequency band analysis comparing baseline vs pain window

---

## Current Results

Live EEG streaming from all four Muse 2 channels successfully established. Clean signal acquisition with visible response to physical stimuli demonstrated. Analysis pipeline built in Jupyter. Cold pressor experiment in progress.

---

## Why It Matters

This project sits at the intersection of neurotechnology, machine learning, and clinical AI. The deliverable is a working prototype demonstrating EEG signals can detect physiological responses to pain using affordable hardware. Next phase involves machine learning classification and an AI layer generating plain-language clinical summaries for nursing staff.

---

## Research Question

Can consumer-grade EEG technology provide a reliable and continuous objective pain indicator for non-verbal patients as a viable alternative to behavioral observation scales?

---

*Built with Muse 2 EEG · muselsl · Python · Jupyter*
