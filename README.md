# NEROVA
### EEG-Based Pain Detection System for Non-Verbal Patients

[![Status](https://img.shields.io/badge/status-active%20research-brightgreen)]()
[![Hardware](https://img.shields.io/badge/hardware-Muse%202%20EEG-blue)]()
[![Language](https://img.shields.io/badge/python-3.12-blue)]()
[![License](https://img.shields.io/badge/license-MIT-lightgrey)]()

---

## The Problem

One of the most persistent challenges in clinical care is accurately assessing pain in patients who cannot speak for themselves — individuals on ventilators, patients with late-stage dementia, infants in neonatal units, and those recovering from strokes or traumatic brain injuries.

The standard pain scale ("rate your pain from 1 to 10") is completely inaccessible to these patients. Existing alternatives like the Critical Care Pain Observation Tool (CPOT) rely on nurses manually observing facial expressions and body movements — subjective, inconsistent, and unable to run continuously.

**Patients can experience significant pain between check-ins with no way to signal it.**

---

## The Solution

Neurova is a prototype system that uses a consumer-grade EEG headset to monitor a patient's brainwave activity in real time and translate that neural data into a continuous, objective pain indicator delivered through a live visualization dashboard.

The system requires no patient cooperation. It works passively and continuously.

---

## The Science

Pain produces measurable and reproducible changes in EEG frequency bands:

| Band | Frequency | Pain Response |
|------|-----------|--------------|
| Theta | 4–8 Hz | Increases during pain processing in the anterior cingulate cortex |
| Alpha | 8–12 Hz | Suppressed when pain is present |
| Gamma | 30–100 Hz | Spikes during acute pain stimuli |

Validated in peer-reviewed research by Ploner et al. (2017), Gram et al. (2017), and Peng et al. (2019).

---

## Hardware

- Muse 2 EEG Headset — 4 channels (TP9, AF7, AF8, TP10), 256 Hz sampling rate
- Windows 10/11 laptop with Bluetooth

---

## Software Stack

| Tool | Purpose |
|------|---------|
| `muselsl` | Bluetooth streaming from Muse 2 via LSL |
| `numpy` / `pandas` | Signal processing and data handling |
| `matplotlib` / `scipy` | Visualization and frequency analysis |
| `jupyter` | Analysis notebooks |

---

## Repository Structure
