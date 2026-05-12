## Getting Started

### 1. Install dependencies
```bash
pip install muselsl numpy pandas matplotlib scipy jupyter
```

### 2. Find your Muse 2
```bash
muselsl list
```

### 3. Start streaming
```bash
muselsl stream
```

### 4. Visualize live EEG (new terminal)
```bash
muselsl view
```

### 5. Record a session
```bash
cd Desktop
muselsl record --duration 120
```

---

## Experiment Protocol

### Baseline Recording
Participant sits still with eyes closed for 2 minutes. Establishes personal baseline for comparison.

### Pain Stimulus — Cold Pressor Task
30 seconds rest → submerge hand in ice water up to 2 minutes → 30 seconds recovery. Timestamps marked for pain window analysis.

### What to Look For
- Alpha suppression — calm resting rhythm drops
- Theta increase — pain processing activity rises
- Increased signal variance — signal becomes more chaotic

---

## Current Status

- [x] Hardware setup and Bluetooth streaming
- [x] Live EEG visualization (4 channels)
- [x] Baseline data collection protocol
- [x] Cold pressor pain stimulus recording
- [x] Frequency band analysis
- [x] Baseline vs pain window comparison
- [ ] AI interpretation layer

---

## References

- Ploner, M., et al. (2017). Brain Rhythms of Pain. *Trends in Cognitive Sciences.*
- Gram, M., et al. (2017). Prediction of postoperative opioid analgesia. *European Journal of Pain.*
- Peng, W., et al. (2019). Alpha transcranial alternating current stimulation modulates pain. *PubMed.*

---

## Author

**Fikewa Akindolire** — Morgan State University
Project developed as part of research into neurotechnology applications in clinical care.

---

*Neurova — A new frontier in neuroscience.*
