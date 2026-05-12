# Neurova - EEG Pain Detection Analysis
# =======================================
# Morgan State University | Fikewa Akindolire | 2026

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# -----------------------------------------------
# STEP 1: Load Data
# -----------------------------------------------
# Replace with your actual recorded file paths

BASELINE_FILE = "baseline.csv"
PAIN_FILE = "pain_stimulus.csv"

def load_muse_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()
    return df

# Uncomment when you have real data:
# baseline_df = load_muse_data(BASELINE_FILE)
# pain_df = load_muse_data(PAIN_FILE)

# -----------------------------------------------
# STEP 2: Simulate Data (for testing)
# -----------------------------------------------

SAMPLE_RATE = 256
DURATION_BASELINE = 120
DURATION_PAIN = 180

def simulate_eeg(duration, pain_start=None, pain_end=None, sample_rate=256):
    t = np.linspace(0, duration, duration * sample_rate)
    alpha = np.sin(2 * np.pi * 10 * t)
    theta = np.sin(2 * np.pi * 6 * t)
    noise = np.random.normal(0, 0.3, len(t))
    signal_data = alpha + 0.3 * theta + noise
    if pain_start and pain_end:
        pain_mask = (t >= pain_start) & (t <= pain_end)
        signal_data[pain_mask] = (
            0.3 * alpha[pain_mask] +
            1.8 * theta[pain_mask] +
            np.random.normal(0, 0.6, pain_mask.sum())
        )
    return t, signal_data

t_baseline, baseline_signal = simulate_eeg(DURATION_BASELINE)
t_pain, pain_signal = simulate_eeg(DURATION_PAIN, pain_start=30, pain_end=150)

# -----------------------------------------------
# STEP 3: Visualize Raw Signal
# -----------------------------------------------

fig, axes = plt.subplots(2, 1, figsize=(14, 8))
fig.suptitle("Neurova — EEG Signal Comparison", fontsize=16, fontweight='bold')

axes[0].plot(t_baseline, baseline_signal, color='black', linewidth=0.5)
axes[0].set_title("Baseline (Resting State)")
axes[0].set_xlabel("Time (seconds)")
axes[0].set_ylabel("Amplitude (µV)")

axes[1].plot(t_pain, pain_signal, color='black', linewidth=0.5)
axes[1].axvspan(30, 150, alpha=0.15, color='red', label='Pain Stimulus Window')
axes[1].set_title("Cold Pressor Task (Pain Stimulus)")
axes[1].set_xlabel("Time (seconds)")
axes[1].set_ylabel("Amplitude (µV)")
axes[1].legend()

plt.tight_layout()
plt.show()

# -----------------------------------------------
# STEP 4: Frequency Band Analysis
# -----------------------------------------------

def extract_band_power(signal_data, sample_rate, low_freq, high_freq):
    freqs = fftfreq(len(signal_data), 1/sample_rate)
    fft_vals = np.abs(fft(signal_data))**2
    band_mask = (freqs >= low_freq) & (freqs <= high_freq)
    return np.mean(fft_vals[band_mask])

def analyze_window(signal_data, sample_rate, window_size=256):
    alpha_power = []
    theta_power = []
    timestamps = []
    for i in range(0, len(signal_data) - window_size, window_size // 2):
        window = signal_data[i:i+window_size]
        alpha_power.append(extract_band_power(window, sample_rate, 8, 12))
        theta_power.append(extract_band_power(window, sample_rate, 4, 8))
        timestamps.append(i / sample_rate)
    return np.array(timestamps), np.array(alpha_power), np.array(theta_power)

t_base_bands, alpha_base, theta_base = analyze_window(baseline_signal, SAMPLE_RATE)
t_pain_bands, alpha_pain, theta_pain = analyze_window(pain_signal, SAMPLE_RATE)

# -----------------------------------------------
# STEP 5: Pain Score Visualization
# -----------------------------------------------

def compute_pain_score(alpha_power, theta_power, alpha_baseline, theta_baseline):
    alpha_ratio = alpha_power / np.mean(alpha_baseline)
    theta_ratio = theta_power / np.mean(theta_baseline)
    pain_score = (1 - alpha_ratio) + (theta_ratio - 1)
    pain_score = np.clip(pain_score, 0, 1) * 10
    return pain_score

pain_scores = compute_pain_score(alpha_pain, theta_pain, alpha_base, theta_base)

plt.figure(figsize=(14, 4))
plt.plot(t_pain_bands, pain_scores, color='black', linewidth=1.5)
plt.axvspan(30, 150, alpha=0.1, color='red', label='Pain Stimulus Window')
plt.axhline(y=5, color='red', linestyle='--', alpha=0.5, label='Alert Threshold')
plt.fill_between(t_pain_bands, pain_scores, alpha=0.1, color='red')
plt.title("Neurova — Continuous Pain Score (0–10)", fontsize=14, fontweight='bold')
plt.xlabel("Time (seconds)")
plt.ylabel("Pain Score")
plt.ylim(0, 10)
plt.legend()
plt.tight_layout()
plt.show()
