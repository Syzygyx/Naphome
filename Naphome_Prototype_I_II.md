# 🌙 Naphome Smart Sleep Device – Phases 0.9, I & II Proposal
**Updated:** October 2025  

---

## 1. Overview

**Naphome** is a next-generation smart sleep companion that unites **light, sound, and environmental sensing** to create a restorative bedroom ecosystem.  
All AI and logic reside in the **cloud**, while an ultra-efficient **ESP32-S3** handles real-time wake-word detection, RGB lighting, audio playback, and sensor telemetry.

The system evolves from **Prototype 0 (Raspberry Pi 5 + WM8960 HAT)** to a **cost-optimized, cloud-connected ESP32-S3 platform** with in-house far-field microphones, stereo sound, and integrated RGB lamp.

### Prototype 0 (P0) – Achievements

**Current Hardware:** Raspberry Pi 5 + WM8960 Audio HAT  
**Status:** Fully functional proof-of-concept with cloud integration

**Implemented Features:**
- ✅ Voice input/output with WM8960 HAT (mic + speaker)
- ✅ LLM integration (cloud-based conversation processing)
- ✅ Voice-to-voice capability via ElevenLabs TTS
- ✅ Addressable LED strip control with dynamic feedback
- ✅ Temperature & humidity sensor → AWS IoT telemetry
- ✅ AWS IoT MQTT control (lights, sound, TTS actuation)
- ✅ IR blaster for AC control (optimal sleep temperature)
- ✅ Spotifyd integration for music streaming
- ✅ Access Point mode for device provisioning
- ✅ User registration flow (first-time setup)
- ✅ Backend scheduler for routine automation
- ✅ Python service architecture (auto-start on boot)
- ✅ OTA-ready architecture

**Transition Goal:** Migrate P0 functionality to ESP32-S3 for cost reduction and mass production.

---

## 2. System Architecture

| Layer | Function |
|-------|-----------|
| **Cloud Layer** | Handles speech recognition, LLM processing, TTS (ElevenLabs), user routines, Spotify streaming, and OTA management via AWS IoT Core. |
| **Device MCU (ESP32-S3)** | Local wake-word detection, I²S audio streaming, RGB lighting control, sensor polling, IR blaster control, and MQTT messaging. |
| **Audio Subsystem** | Custom far-field 2–3 mic array → ESP-SR AFE + WakeNet model → TAS5825M DSP amp → stereo ND65 drivers + passive radiators. Premium audio (Nest/Bose class). |
| **Lighting** | 10–12 × WS2812B addressable RGB LEDs under a frosted diffuser for circadian lighting and visual feedback. |
| **Sensors (7 Total)** | SHTC3 (Temp/Humidity), SGP30 or SCD41 (VOC/CO₂), VEML7700 (Ambient Light), PIR (Motion), PMS5003 (PM2.5 Air Quality), MEMS Sound Sensor. |
| **Controls** | Capacitive touch buttons + rotary encoder (volume knob). |
| **Power** | USB-C PD 12 V primary + Li-ion battery backup (2–3 hrs). |
| **Connectivity** | Wi-Fi 2.4 GHz, BLE provisioning, secure OTA updates, **IR transmitter for IoT control**. |

---

## 3. Phase 0.9 – COTS Validation (10–25 Units)

### Purpose
Phase 0.9 bridges the proven Prototype 0 (Raspberry Pi 5) and Phase I (custom PCB) by validating core functionality using **Commercial Off-The-Shelf (COTS)** ESP32 development boards and Grove sensor modules. This rapid prototype phase allows firmware development, cloud integration testing, and sensor validation without custom PCB investment.

### Hardware (All COTS)
- **ESP32-S3 DevKit** (e.g., ESP32-S3-DevKitC-1 or similar) with 8 MB PSRAM
- **Grove Base Shield** or breadboard with Grove connectors
- **Grove Sensors (7 Total):**
  - Grove Temperature & Humidity Sensor (SHTC3 or DHT20)
  - Grove Air Quality Sensor (SGP30 or equivalent)
  - Grove PM2.5 Sensor (PMS5003 compatible)
  - Grove Light Sensor (VEML7700 or TSL2561)
  - Grove PIR Motion Sensor
  - Grove Sound Sensor (MEMS microphone module)
  - Grove CO₂ Sensor (SCD30 or SCD40, optional)
- **Audio:** Generic I²S MEMS microphone breakout + MAX98357A I²S amp module + small speaker
- **RGB Lighting:** WS2812B LED strip or ring (10–12 LEDs)
- **IR Transmitter:** Grove IR Emitter module or generic IR LED + transistor circuit
- **Power:** USB-C cable (5V) to ESP32 DevKit
- **Controls:** Tactile push buttons or capacitive touch breakout module

### Firmware Goals
- Port P0 functionality to ESP-IDF + ESP-ADF
- Local wake-word detection (ESP-SR WakeNet)
- MQTT connection to AWS IoT Core
- Sensor telemetry publishing (temperature, humidity, VOC, PM2.5, light, motion, sound)
- RGB LED control via cloud commands
- IR blaster control for AC/TV (test LIRC or ESP32-IR library)
- OTA firmware updates
- Wi-Fi provisioning (Access Point mode)

### Validation Objectives
1. Confirm ESP32-S3 can handle simultaneous I²S audio, sensor polling, RGB control, and MQTT
2. Test Grove sensor accuracy and I²C/UART communication reliability
3. Validate IR transmitter range and command database
4. Measure power consumption and thermal behavior
5. Finalize firmware architecture before custom PCB design
6. Confirm cloud latency and MQTT message throughput

### Estimated BOM (Phase 0.9, per unit)
**Components include:** ESP32-S3 DevKit, Grove sensors (temperature, humidity, air quality, PM2.5, light, motion, sound), I²S audio modules, RGB LED strip, IR transmitter, and power supply.

**Estimated cost:** ~$90 per unit (varies with supplier and volume)

**Timeline:** 2–3 weeks for assembly, firmware porting, and validation testing (concurrent with manufacturer negotiations).

**Outcome:** A fully functional COTS prototype that validates all Phase I features before committing to custom PCB manufacturing.

---

## 4. Phase I – Retrofit Pilot (≈ 200 Units)

### Purpose
Phase I aims to validate end-to-end cloud interactions, lighting, sensing, and acoustics by retrofitting 200 existing speaker or lamp units with an **ESP32-S3 retrofit module**. **The donor devices already have built-in speakers and RGB lighting**, which will be integrated with the retrofit control module.

### Hardware
- ESP32-S3 WROOM (8 MB PSRAM) on custom 2–4 layer PCB.  
- 2–3 digital I²S far-field microphones with custom placement and isolation.  
- **Utilizes existing RGB lighting and speakers from donor device** (speaker/lamp units with built-in audio and lighting).  
- **7 Sensors:** SHTC3 (Temp/Humidity), SGP30 (VOC/eCO₂), VEML7700 (Light), PIR (Motion), PMS5003 (PM2.5), MEMS Sound Sensor (no display).  
- Capacitive touch buttons + rotary encoder (volume control).
- **IR LED transmitter** for IoT device control (AC, TV, etc.).
- Battery backup: 18650 Li-ion cell (2–3 hrs runtime).
- Powered by USB-C PD (12 V primary).  

### Firmware
- Built on **ESP-IDF + ESP-ADF + ESP-SR**.  
- Local wake-word recognition, cloud-based speech streaming.  
- MQTT for routines, telemetry, and RGB control.  
- OTA update pipeline with dual partitioning.  
- Access Point Wi-Fi setup and persistent credentials.  

### Pilot Goals
1. Validate far-field mic performance in real bedrooms.  
2. Measure latency for cloud-based voice interaction.  
3. Evaluate RGB diffusion and ambient brightness.  
4. Gather sensor and thermal behavior data.  
5. Finalize firmware and network stack for mass production.  

### BOM Overview (Phase I – Retrofit Pilot, 200 units)

**Key Components:**
- ESP32-S3 WROOM-1 with power management
- 3× Digital I²S MEMS microphones
- 7× Environmental sensors (temperature, humidity, air quality, PM2.5, light, motion, sound)
- IR transmitter and capacitive touch controls
- Custom 4-layer PCB with assembly
- Retrofit housing using donor speaker/lamp units

**Estimated cost:** ~$95 per unit (includes packaging and shipping)

**Note:** Cost savings from using donor device speakers and RGB lighting.

---

## 5. Phase II – Full Production (10,000 Units)

### Objectives
- Transition to **fully custom housing and board**.  
- Integrate **in-house far-field mic array** and RGB light dome.  
- Achieve **$40 BOM (base)**, **$55 BOM (premium)**.  
- Establish scalable manufacturing and QA pipeline.  

### Hardware Design
- ESP32-S3 + TAS5825M on single 4-layer PCB.  
- Integrated microphone array with acoustic isolation geometry.  
- ND65 stereo drivers + passive radiators in dual acoustic chambers.  
- 10–12 WS2812B LEDs with internal diffuser and light pipe integration.  
- Molded PC/ABS shell with sensor and mic apertures.  

### Firmware Enhancements
- Optimized AEC and beamforming (ESP-SR AFE).  
- MQTT connection resilience and watchdog.  
- Adaptive LED states (sleep, wake, alert).  
- Local cache for routines to operate if offline.  
- Secure OTA with fail-safe rollback.  

### BOM Overview (10k Volume)

**Key Subsystems:**
- ESP32-S3 MCU with TAS5825M audio amplifier
- ND65/ND90 stereo speakers with passive radiators
- Environmental sensors (temperature, humidity, air quality, light, motion)
- RGB LED ring with diffuser
- USB-C power management and custom enclosure

**Estimated costs:**
- **Base SKU:** ~$40 per unit
- **Premium SKU:** ~$55 per unit (enhanced audio + CO₂ sensor)

---

## 6. Manufacturing Partners

**All partners listed below are capable of end-to-end turnkey manufacturing** (PCB sourcing → PCBA → speaker/LED assembly → plastic housing → final QA → packaging).

### 🔧 1. **Zhuhai DB-Way Technology Co., Ltd.**
**Capabilities:** Full turnkey manufacturing including PCBA, audio integration, RGB assembly, plastic housing, and end-of-line testing.  
**Specialization:** EMS with IoT device experience.  
**Relevant Product:** [Wake-up Light Alarm Clock with FM Radio Speaker](https://www.alibaba.com/x/B0uBjo?ck=pdp) - Bedside lamp with RGB lighting, touch control, USB rechargeable. Demonstrates capability in audio + lighting integration.

![DB-Way Wake-up Light Alarm Clock](images/db-way-wake-up-light.png)

---

### 💡 2. **Shanghai Kaiji Lighting Technology Co., Ltd.**
**Capabilities:** Full turnkey manufacturing with enhanced RGB lighting and diffuser expertise.  
**Specialization:** Smart lighting products; in-house optical design and light pipe molding.  
**Relevant Product:** [Bluetooth Speaker with RGB Dynamic Lighting](https://www.alibaba.com/x/B0uBjy?ck=pdp) - Portable bedside table lamp with RGB atmosphere lighting, Bluetooth speaker, rechargeable. Shows expertise in RGB lighting + audio integration (10k units @ $8.29).

![Kaiji RGB Bluetooth Speaker Lamp](images/kaiji-rgb-bluetooth-speaker.png)

---

### ⚙️ 3. **Shenzhen Xiteyou Electronic Technology Co., Ltd.**
**Capabilities:** Full turnkey manufacturing with strong component sourcing network.  
**Specialization:** Consumer electronics; competitive pricing on sensors, mics, and ICs.  
**Relevant Product:** [Smart Sleep Monitor with 32 Soothing Sounds](https://www.alibaba.com/x/B0uBI9?ck=pdp) - Rechargeable nightlight with RGB lighting (7 colors), Bluetooth speaker, white noise machine (105×105×150mm, 8-10hr battery, $19.99 retail). Lead time: 15-35 days for 100-1800 units. Demonstrates strong cost optimization and experience with sleep/audio devices.

![Xiteyou Smart Sleep Monitor](images/xiteyou-smart-sleep-monitor.png)

---

### 🧱 4. **Dongguan Compro Electronic Technology Co., Ltd.**
**Website:** [www.comproelec.com](http://www.comproelec.com)  
**Capabilities:** Full OEM/ODM turnkey manufacturing with certification support.  
**Specialization:** Smart speakers and IoT audio devices; established supply chain for acoustic components.

---

## 7. NRE and Certification

| Item | Cost (USD) |
|------|-----------:|
| Enclosure Tooling (2-cavity mold + diffuser dome) | 18,000 |
| Test Fixtures / QA Jigs | 6,000 |
| Compliance Testing & DoC (using pre-certified ESP32 module) | 2,500 |
| Engineering Samples & Validation | 4,000 |
| **Total NRE** | **≈ $30,500 (≈ $3.05/unit @ 10k)** |

**Note:** Using pre-certified ESP32-S3-WROOM-1 module eliminates the need for full FCC/CE certification. Only Declaration of Conformity (DoC) and basic compliance testing required.

---

## 8. Timeline

| Phase | Duration | Key Deliverables |
|--------|-----------|-----------------|
| **Phase 0.9 (COTS Validation)** | 2–3 weeks | ESP32-S3 DevKit + Grove sensors, firmware porting (ESP-IDF + ESP-ADF), MQTT + AWS IoT integration, sensor validation (concurrent with manufacturer negotiations) |
| **Phase I (Retrofit Pilot)** | 12–16 weeks | Custom PCB design, 200 retrofit units, far-field mic array, sensor integration, IR blaster validation |
| **EVT (Engineering Validation)** | 8 weeks | PCB Rev A + mic validation + RGB firmware demo |
| **DVT (Design Validation)** | 6 weeks | Mold T0 samples + acoustic tuning + sensor calibration |
| **PVT (Production Validation)** | 4 weeks | 300–500 unit pilot run + certification testing |
| **MP (Mass Production)** | 3–4 months | 10k units + QA inspection |

---

## 9. SKU Summary

| SKU | Audio | Sensors | Lighting | BOM | MSRP |
|------|--------|----------|----------|-----:|-----:|
| **Base** | ND65 + PR | SHTC3 + SGP30 + PIR + VEML7700 | 10 × WS2812B | $40 | $129 |
| **Premium** | ND90 + PR | SHTC3 + SGP30 + SCD41 + PIR + VEML7700 | 16 × WS2812B + enhanced diffuser | $55–58 | $199 |

---

## 10. Advantages

- **ESP32-S3 Efficiency:** Simultaneous I²S, Wi-Fi, LED, and sensor processing.  
- **Cloud Architecture:** Offloads heavy LLM/TTS for low-cost hardware.  
- **Custom Mic Array:** In-house beamforming and AEC tuning for wake accuracy.  
- **Dynamic RGB Lighting:** Circadian lighting and responsive visual feedback.  
- **Flexible Vendor Network:** Five capable partners for risk-mitigated scaling.  

---

## 11. Consulting Services

### Technical Consulting Services (Daniel McShane)

**Hardware/Firmware Development Lead**

**Scope of Services:**
- Phase 0.9 COTS prototype development and firmware porting (ESP-IDF + ESP-ADF)
- Phase I custom PCB design, schematic review, and component selection
- ESP32-S3 firmware architecture (wake-word detection, MQTT, OTA, sensor integration)
- Cloud integration and AWS IoT Core configuration
- Manufacturer liaison and technical specifications documentation
- Acoustic design consultation and microphone array optimization
- IR transmitter implementation and device control database
- Quality assurance planning and test fixture specifications

**Rate Structure:**
- **Manufacturing Consultation:** $500 per week (liaison with Chinese manufacturers, specifications, quality control)
- **Firmware Development:** $100 per hour (ESP32-S3 development, testing, debugging, optimization)

**Note:** Hardware and manufacturing costs are negotiated directly with manufacturers (DB-Way, Kaiji, Xiteyou, etc.) and vary based on volume, specifications, and market conditions.

---

## 12. Next Steps

1. **Phase 0.9:** Procure COTS ESP32-S3 DevKit and Grove sensors, begin firmware porting (2–4 weeks).
2. Finalize Phase I PCB design (ESP32-S3 + mic array + sensor integration).  
3. Send RFQs and NDAs to DB-Way, Kaiji, Xiteyou, Yingke, and Compro.  
4. Build 25–50 COTS validation units for firmware and cloud integration testing.  
5. Transition to custom PCB pilot (200 units) for acoustic and thermal validation.  
6. Lock enclosure design and begin tooling for Phase II mass production.  
7. Conduct PVT (500 units) and transition to 10k MP.

---

**Result:**  
A scalable, cloud-connected smart sleep device with a **$40 BOM**, full RGB lighting, custom audio design, and multi-partner manufacturing capability — ready for global deployment.