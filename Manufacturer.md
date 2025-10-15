# 🏭 Naphome Phase II Manufacturing Specifications
**Document Version:** 1.0  
**Date:** October 2025  
**Target Volume:** 10,000 units  
**BOM Target:** $40 (Base) / $55 (Premium)

---

## 📋 Executive Summary

**Product:** Naphome Smart Sleep Device  
**Architecture:** ESP32-S3 + Cloud AI + Custom Audio/Lighting  
**Manufacturing:** Full turnkey production (PCB → Assembly → Housing → QA)  
**Certification:** FCC/CE compliant using pre-certified ESP32-S3 module  

---

## 🎯 Product Overview

The Naphome is a premium smart sleep companion that combines:
- **Voice AI** (cloud-based speech recognition and response)
- **Premium Audio** (ND65/ND90 stereo speakers with passive radiators)
- **Dynamic RGB Lighting** (circadian lighting with 10-16 WS2812B LEDs)
- **Environmental Sensing** (6 sensors for bedroom optimization)
- **IoT Control** (IR blaster for AC/TV control)

---

## 🔧 Technical Specifications

### Core Hardware Requirements

| Component | Specification | Notes |
|-----------|---------------|-------|
| **MCU** | ESP32-S3-WROOM-1 (8MB PSRAM) | Pre-certified module (FCC/CE) |
| **Audio Amplifier** | TAS5825M (I²S, 2×20W) | TI digital amplifier |
| **Speakers** | ND65 (Base) / ND90 (Premium) + Passive Radiators | Dual acoustic chambers |
| **Microphones** | 2-3× Digital I²S MEMS | Far-field, noise-canceling |
| **RGB LEDs** | 10× WS2812B (Base) / 16× WS2812B (Premium) in ring configuration | Addressable, 5V |
| **Display** | 256×64 OLED (SSD1322 or equivalent) | SPI interface, 3.3V |
| **Power** | USB-C PD 12V + Li-ion backup | 2-3 hours battery runtime |
| **Connectivity** | Wi-Fi 2.4GHz + BLE | Dual-band support |

### Sensor Suite (6 Total)

| Sensor | Part Number | Interface | Purpose |
|--------|-------------|-----------|---------|
| **Temperature/Humidity** | SHTC3 | I²C | Environmental monitoring |
| **VOC/CO₂** | SGP30 (Base) / SCD41 (Premium) | I²C | Air quality |
| **Ambient Light** | VEML7700 | I²C | Circadian lighting control |
| **PM2.5 Air Quality** | PMS5003 | UART | Air quality monitoring |
| **Sound Level** | MEMS Microphone | Analog | Noise monitoring |
| **Display** | 256×64 OLED (SSD1322) | SPI | Status, time, visual feedback |
| **IR Transmitter** | Custom IR LED + Driver | GPIO | IoT device control |

### Audio Specifications

| Parameter | Base SKU | Premium SKU |
|-----------|----------|-------------|
| **Drivers** | ND65 + Passive Radiators | ND90 + Passive Radiators |
| **Frequency Response** | 60Hz - 20kHz | 50Hz - 20kHz |
| **THD** | <1% @ 1W | <0.5% @ 1W |
| **Sensitivity** | 85dB @ 1W/1m | 88dB @ 1W/1m |
| **Power Handling** | 2×10W RMS | 2×20W RMS |
| **Acoustic Design** | Dual chamber, ported | Dual chamber, tuned |
| **LED Ring** | 10× WS2812B in ring configuration | 16× WS2812B in ring configuration |

### RGB Lighting Specifications

| Parameter | Base SKU | Premium SKU |
|-----------|----------|-------------|
| **LED Count** | 10× WS2812B | 16× WS2812B |
| **Power** | 5V, 0.3W per LED | 5V, 0.3W per LED |
| **Diffusion** | Frosted acrylic dome | Enhanced diffuser + light pipe |
| **Control** | ESP32-S3 PWM | ESP32-S3 PWM |
| **Configuration** | Ring layout around device perimeter | Ring layout with enhanced spacing |
| **Features** | Circadian lighting, visual feedback | Enhanced diffusion, color accuracy |

---

## 📐 Mechanical Specifications

### Enclosure Requirements

| Parameter | Specification |
|-----------|---------------|
| **Material** | PC/ABS blend (UL94 V-0) |
| **Dimensions** | ~150×150×200mm (TBD) |
| **Weight** | <1.5kg |
| **Finish** | Matte white/black, soft-touch |
| **Assembly** | Snap-fit + screws (serviceable) |
| **IP Rating** | IP20 (indoor use) |

### Acoustic Design

| Component | Specification |
|-----------|---------------|
| **Speaker Enclosure** | Dual acoustic chambers, ported |
| **Mic Array** | 2-3 mics, 120° spacing, acoustic isolation |
| **Vibration Isolation** | Rubber feet, internal damping |
| **Thermal Management** | Passive cooling, thermal pads |

### Connectors & Controls

| Component | Specification |
|-----------|---------------|
| **Power Input** | USB-C PD (12V, 3A) |
| **Touch Controls** | 3× capacitive touch buttons |
| **Volume Control** | Rotary encoder (360°, detented) |
| **Display** | 256×64 OLED (status, time, feedback) |
| **Status LEDs** | Power, Wi-Fi, RGB feedback |
| **Reset Button** | Recessed, factory reset |

---

## 🔌 PCB Specifications

### Board Requirements

| Parameter | Specification |
|-----------|---------------|
| **Layers** | 4-layer PCB |
| **Thickness** | 1.6mm |
| **Material** | FR4, Tg 150°C |
| **Finish** | HASL or ENIG |
| **Size** | ~80×100mm (TBD) |
| **Assembly** | SMT + selective hand assembly |

### Component Placement

| Zone | Components |
|------|------------|
| **MCU Zone** | ESP32-S3, crystal, flash, PSRAM |
| **Audio Zone** | TAS5825M, audio connectors, filtering |
| **Sensor Zone** | I²C sensors, level shifters, pull-ups |
| **Display Zone** | OLED display, SPI interface, level shifters |
| **Power Zone** | USB-C controller, buck/boost, battery management |
| **Interface Zone** | Connectors, buttons, LEDs |

### Power Management

| Rail | Voltage | Current | Components |
|------|---------|---------|------------|
| **VBUS** | 12V (USB-C PD) | 3A | Input from USB-C |
| **VCC_3V3** | 3.3V | 1A | ESP32-S3, sensors |
| **VCC_5V** | 5V | 2A | RGB LEDs, audio amp |
| **VCC_3V3_DISP** | 3.3V | 100mA | OLED display |
| **VBAT** | 3.7V | 2A | Li-ion battery |

---

## 🧪 Testing & Quality Assurance

### Electrical Testing

| Test | Specification | Method |
|------|---------------|--------|
| **Power Consumption** | <15W @ 12V | Digital multimeter |
| **Display Brightness** | 100-300 cd/m² | Luminance meter |
| **Audio THD** | <1% @ 1W | Audio analyzer |
| **Wi-Fi Range** | >30m @ 2.4GHz | RF chamber |
| **Battery Runtime** | >2 hours | Load testing |
| **Sensor Accuracy** | ±2% (temp), ±5% (humidity) | Calibrated references |

### Acoustic Testing

| Test | Specification | Method |
|------|---------------|--------|
| **Frequency Response** | 60Hz-20kHz (Base), 50Hz-20kHz (Premium) | Anechoic chamber |
| **Wake Word Detection** | >95% @ 3m, 60dB ambient | Controlled environment |
| **Microphone Sensitivity** | -26dBV @ 1kHz | Audio analyzer |
| **Audio Latency** | <100ms (cloud round-trip) | Network testing |

### Environmental Testing

| Test | Condition | Duration | Pass Criteria |
|------|-----------|----------|---------------|
| **Temperature** | -10°C to +50°C | 24h | Full functionality |
| **Humidity** | 10% to 90% RH | 24h | No condensation |
| **Vibration** | 5-500Hz, 1g | 2h | No mechanical failure |
| **Drop Test** | 1m onto concrete | 3 drops | Cosmetic damage only |

### RGB Lighting Testing

| Test | Specification | Method |
|------|---------------|--------|
| **Color Accuracy** | CRI >90 | Spectrophotometer |
| **Brightness** | 100-1000 lux @ 1m | Lux meter |
| **Diffusion** | Uniform light distribution | Visual inspection |
| **Power Consumption** | <3W @ full brightness | Power meter |

### Display Testing

| Test | Specification | Method |
|------|---------------|--------|
| **Resolution** | 256×64 pixels | Visual inspection |
| **Contrast Ratio** | >1000:1 | Contrast meter |
| **Viewing Angle** | >160° horizontal, >120° vertical | Goniometer |
| **Response Time** | <1ms | Oscilloscope |
| **Power Consumption** | <50mW @ full brightness | Power meter |

---

## 📦 Packaging & Labeling

### Packaging Requirements

| Component | Specification |
|-----------|---------------|
| **Box Material** | Recycled cardboard, FSC certified |
| **Box Size** | ~200×200×250mm |
| **Protection** | EPE foam inserts |
| **Accessories** | USB-C cable, quick start guide |
| **Labels** | FCC/CE marks, model number, serial |

### Documentation

| Document | Language | Content |
|----------|----------|---------|
| **Quick Start Guide** | English | Setup, Wi-Fi, basic usage |
| **User Manual** | English | Full feature documentation |
| **Safety Information** | English | Warnings, disposal, compliance |
| **Warranty Card** | English | 1-year limited warranty |

---

## 🏭 Manufacturing Process

### Production Flow

1. **PCB Assembly**
   - SMT placement (pick & place)
   - Reflow soldering
   - AOI inspection
   - ICT testing

2. **Audio Assembly**
   - Speaker mounting
   - Acoustic chamber assembly
   - Microphone array installation
   - Audio testing

3. **Sensor Integration**
   - Sensor mounting
   - Cable routing
   - Calibration
   - Functional testing

4. **Final Assembly**
   - PCB installation
   - Enclosure assembly
   - Button/control installation
   - Final testing

5. **Quality Control**
   - Electrical testing
   - Acoustic testing
   - Environmental testing
   - Packaging

### Yield Targets

| Stage | Target Yield | Action if Below |
|-------|--------------|-----------------|
| **PCB Assembly** | >98% | Rework/replace |
| **Audio Assembly** | >95% | Recalibrate |
| **Final Assembly** | >97% | Process improvement |
| **Final Testing** | >99% | Root cause analysis |

---

## 💰 Cost Targets & BOM

### Base SKU BOM Target: $40

| Category | Cost | Components |
|----------|------|------------|
| **MCU & Audio** | $15 | ESP32-S3, TAS5825M, ND65 speakers |
| **Sensors** | $8 | SHTC3, SGP30, VEML7700, PMS5003, MEMS mic |
| **Lighting** | $5 | 10× WS2812B, diffuser, driver |
| **Display** | $2 | 256×64 OLED, driver, mounting |
| **Mechanical** | $8 | Enclosure, buttons, connectors |
| **Power** | $4 | USB-C, battery, power management |
| **Total** | **$40** | |

### Premium SKU BOM Target: $55

| Category | Cost | Components |
|----------|------|------------|
| **MCU & Audio** | $20 | ESP32-S3, TAS5825M, ND90 speakers |
| **Sensors** | $12 | SHTC3, SGP30, SCD41, VEML7700, PMS5003, MEMS mic |
| **Lighting** | $8 | 16× WS2812B, enhanced diffuser, light pipe |
| **Display** | $2 | 256×64 OLED, driver, mounting |
| **Mechanical** | $10 | Enhanced enclosure, premium buttons |
| **Power** | $5 | Enhanced power management |
| **Total** | **$55** | |

---

## 📋 Compliance & Certification

### Required Certifications

| Standard | Scope | Method |
|----------|-------|--------|
| **FCC Part 15** | RF emissions | Pre-certified ESP32-S3 module |
| **CE EMC** | Electromagnetic compatibility | Declaration of Conformity |
| **CE LVD** | Low voltage directive | Internal testing |
| **RoHS** | Restriction of hazardous substances | Material declaration |
| **REACH** | Chemical safety | Material declaration |

### Testing Requirements

| Test | Standard | Pass Criteria |
|------|----------|---------------|
| **RF Emissions** | FCC Part 15 Class B | < FCC limits |
| **RF Immunity** | IEC 61000-4-3 | No degradation |
| **ESD** | IEC 61000-4-2 | ±8kV contact, ±15kV air |
| **Surge** | IEC 61000-4-5 | ±2kV differential |

---

## 🚀 Timeline & Milestones

### Phase II Production Timeline

| Milestone | Duration | Deliverables |
|-----------|----------|--------------|
| **Tooling** | 8 weeks | Injection molds, test fixtures |
| **EVT** | 4 weeks | Engineering validation units |
| **DVT** | 6 weeks | Design validation, acoustic tuning |
| **PVT** | 4 weeks | 500-unit pilot run |
| **MP** | 16 weeks | 10,000 units production |

### Key Deliverables

| Phase | Deliverable | Quantity |
|-------|-------------|----------|
| **EVT** | Engineering samples | 50 units |
| **DVT** | Design validation | 200 units |
| **PVT** | Production validation | 500 units |
| **MP** | Mass production | 10,000 units |

---

## 📞 Contact Information

### Technical Lead
**Daniel McShane**  
**Email:** dan@syzygyx.com  
**Services:** Hardware design, firmware development, manufacturing liaison  
**Rate:** $1,000/week (prototype), $400/week (production), $100/hour (firmware)

### Manufacturing Partners
- **DB-Way Technology** (Zhuhai) - Full turnkey manufacturing
- **Kaiji Lighting** (Shanghai) - RGB lighting expertise  
- **Xiteyou Electronic** (Shenzhen) - Cost optimization
- **Compro Electronic** (Dongguan) - Audio device experience

---

## 📝 Notes & Assumptions

### Key Assumptions
- ESP32-S3-WROOM-1 module is pre-certified (FCC/CE)
- 10,000 unit minimum order quantity
- 12-month production timeline
- Standard payment terms (30% deposit, 70% on delivery)
- 1-year warranty on all components

### Risk Mitigation
- Multiple supplier options for critical components
- Pre-production validation at each phase
- Comprehensive testing and quality control
- Experienced manufacturing partners with IoT device experience

---

**Document Status:** Ready for manufacturer review and quotation  
**Next Steps:** RFQ distribution, NDA execution, technical discussions
