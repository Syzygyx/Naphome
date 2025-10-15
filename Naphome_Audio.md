# Naphome-Audio  
### Smart Bedside + Slip-In Subwoofer System  
*(ESP32-based synchronized audio and lighting network)*

---

## 1. Overview
Naphome-Audio is a unified design for a **bedside smart audio system** featuring:

- High-quality **stereo speakers** on each nightstand  
- **Synchronized RGB or CCT lamps** (left + right)  
- An **under-mattress tactile subwoofer pad** for low-frequency vibration  
- Cloud and local playback via ESP32 (A2DP + Wi-Fi)  
- Full synchronization across audio and light using local multicast timing  

---

## 2. Bedside Speaker Targets

| Parameter | Spec |
|------------|------|
| Frequency range | 80 Hz – 18 kHz |
| SPL (listener @ 1 m) | 70 – 80 dB |
| Output Power | 5 W × 2 (10 W total) |
| Distortion | < 1 % THD typical |
| Supply | 12 V 2 A (24 W headroom) |
| Audio Input | I²S from ESP32 DAC |
| Connectivity | Wi-Fi + BT A2DP |
| Enclosure | 0.5 L × 2 sealed with passive radiator |

**Typical configuration**
```
ESP32-S3  →  I²S DAC (PCM5102A or ES8388)
            →  TPA3116D2 Amp (2 × 15 W)
            →  2 × 2.5″ 4 Ω full-range drivers + 3″ passive radiator
            →  12 V 2 A power brick
```

**Sound tuning**
- Gentle bass shelf +3 dB @ 120 Hz  
- Treble lift +2 dB @ 8 kHz  
- Gamma-corrected brightness curves for LED feedback  

---

## 3. Synchronized Lamp System

### Concept
Two matching bedside lamps operate in **phase-locked sync** over Wi-Fi.  
One ESP32 acts as the **master clock** and scene generator; peers render frames
based on timestamped packets.

### Clocking
- Multicast UDP beacons: `SYNC { master_time_us }` every 200 ms  
- Peers estimate offset + drift (ppm)  
- Animation frames carry `play_time_us`; peers render when local ≥ play_time  

### Modes
- **Mirror:** identical L/R effects  
- **Complementary:** 180° hue or +90° phase offset  
- **Stereo-linked:** each reacts to L/R audio energy  
- **Circadian:** auto CCT + brightness schedule  

### Hardware
| Component | Example | Notes |
|------------|----------|-------|
| LED engine | SK6812 RGBW strip or tunable CCT COB | RGBW preferred for accurate whites |
| Driver | PCA9685 + MOSFETs or dedicated CC LED driver | For CCT channels |
| Power | 12 V 3 A brick | Shared with speaker if co-located |
| Control | ESP32-S3 + rotary or capacitive touch | OTA-ready |
| Diffuser | Frosted acrylic / fabric shade | Even glow |

---

## 4. Under-Mattress Slip-In Subwoofer Pad

### Purpose
Provide **tactile low-frequency feedback** for music or ambient sound without audible rumble.  
All electronics remain outside the mattress; only a passive vibration pad sits between mattress and box spring.

### Structure
| Layer | Description |
|--------|-------------|
| **Top:** | Mattress |
| **Middle:** | Aluminum vibration plate (6–8 mm × 30 × 40 cm) |
| **Mounted:** | AuraSound AST-2B-4 or Dayton BST-1 tactile transducer |
| **Bottom:** | Sorbothane or neoprene isolation feet |
| **Output:** | 2-core speaker wire (16 AWG) to external amp |

### Placement
- Insert from **head of bed**, centered left/right, plate facing up.  
- Keep thickness ≈ 3–4 cm.  
- No electronics inside mattress stack.

### Amplification
| Component | Example | Notes |
|------------|----------|-------|
| Amp | TPA3116/3118 mono 50–100 W @ 4 Ω | Class-D, external |
| Power | 24 V 5 A supply | 120 W headroom |
| Filters | HP 25 Hz, LP 120 Hz | Protect and limit band |
| DAC source | PCM5102A / ES8388 from ESP32 | Line-level output |

### Wiring
```
Phone → BT → ESP32 (A2DP Sink)
ESP32 → I²S → DAC → Amp → Tactile Pad
Amp + PSU outside bed frame
Speaker wire only under mattress
```

---

## 5. Audio Synchronization Framework

### Overview
A single ESP32 (master) handles timing; all nodes subscribe to **multicast UDP** frames.

**Packet formats**
```c
struct Sync {
  uint16_t magic;        // 0x51NC
  uint32_t t_master_us;  // master timestamp
}

struct Frame {
  uint16_t magic;        // 0xFRAE
  uint32_t play_time_us; // scheduled playback time
  uint8_t  mode;         // animation / audio pattern id
  uint8_t  params[...];  // scene parameters
}
```

### Timing
- Beacons every 200 ms; frames buffered 30 ms ahead  
- Peers maintain jitter ≤ 2 ms  
- Sample clocks corrected via PLL or micro-resample  
- Suitable for both **audio** and **lamp** sync  

---

## 6. Safety & Comfort

| Concern | Mitigation |
|----------|-------------|
| Heat in bed | All active electronics external |
| Electrical isolation | Only passive wires under mattress |
| Volume / vibration | Start < 20 %, ramp gradually |
| Infant safety | Do *not* use in cribs or with infants |
| Overnight use | Moderate gain; allow airflow around amp/PSU |

---

## 7. Example BOM Snapshot (single bedside setup)

| Item | Example | Est. Cost (USD, 10k qty) |
|------|----------|---------------------------|
| ESP32-S3-WROOM-1 | — | 2.20 |
| PCM5102A DAC | — | 0.80 |
| TPA3116D2 Amp | — | 1.50 |
| 2 × 2.5″ Speakers + Radiator | Tang Band / Peerless | 3.00 |
| RGBW LED Module | SK6812 | 0.90 |
| 12 V 2 A PSU | — | 2.50 |
| Enclosure & Mounts | — | 2.00 |
| **Total (est.)** | | **≈ $13/unit** |

---

## 8. Expansion & Future Work
- Dual-pad stereo vibration with Wi-Fi clock sync  
- LE Audio support when ESP32-H4 releases  
- Integrated sensor feedback (CO₂, VOC, temp) for adaptive ambient scenes  
- Unified OTA update channel for all bedside nodes  

---

### Summary
> Naphome-Audio delivers a warm, synchronized sensory environment:
> balanced bedside audio, gentle light choreography, and silent tactile bass —
> all coordinated by the ESP32 platform with precise timing and safe design.

---

*Syzygy Labs — Naphome Prototype Audio System, 2025*
