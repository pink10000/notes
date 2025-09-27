---
tags:
  - CSE_127
---
---

---

## **Overview and Context**  
In the previous class, we covered isolation and privilege levels to implement **privilege separation**, **least privilege**, and **complete mediation**. The primary goal was to **protect sensitive information** so that it is inaccessible across trust boundaries.

- **Trust Boundary**: The assumption is that we understand the trust boundaries within a system and can identify access points.

---

## **Side Channels**  
### **Understanding Side Channels**  
A system is often thought of as a **black box** with input and output. However, **side channels** can leak information through indirect means not captured by direct output.

- **Side Channel** is an **unintentional information leak** through **non-output behaviors** like timing, power usage, temperature, etc.

### **Types of Side Channels**  
1. **Consumption Side Channels**: Resource usage reveals information.
   - Examples: Time, power, memory, network activity
2. **Emission Side Channels**: External signals reveal information.
   - Examples: Electromagnetic radiation, sound, movement, error messages

### **Examples of Side Channel Attacks**  
1. **Tenex Password Verification (1974)**:
   - An attack exploiting **character-at-a-time comparisons** in password verification by using **memory faults**.

2. **Power Analysis Attacks**:
   - **Simple Power Analysis (SPA)** and **Differential Power Analysis (DPA)** analyze power consumption to reveal sensitive data, especially cryptographic keys.

3. **Timing Attacks**:
   - Observing **timing of keystrokes** or **packet timings** over protocols like **SSH** to recover information.

4. **Web Application Side-Channel Leaks**:
   - Monitoring **response sizes over HTTPS** to infer input data (e.g., search terms).

5. **Acoustic Emanations**:
   - Recovering **keyboard input** by analyzing the sound produced by each keystroke.

6. **Remote LCD Reading via RF (2004)** and **Optical Domain Emanations**:
   - **Light or RF** emissions from screens can be remotely analyzed to reconstruct screen content.

---

## **Active Side Channels and Fault Injection Attacks**  
Faults induced in systems can reveal or alter sensitive data.

- **Fault Injection**: Using **power glitches**, **voltage changes**, **temperature variations**, or **light exposure** to manipulate hardware behavior.
- **Covert Channels**: A type of side channel intentionally designed to leak information in ways that evade detection, commonly by **encoding information** into subtle variations (e.g., timing, resource usage).

---

## **Mitigation Strategies for Side Channels**  
### **Eliminate Dependencies**  
1. **Constant Resource Use**:
   - Operate at **worst-case performance** always to prevent leakage through variations.
2. **Blinding**:
   - Certain algorithms can mask secret data by transforming it (e.g., RSA).
3. **Random Noise**:
   - Can deter attackers, though they may overcome it with sufficient data.

---

## **Cache Side Channels**  
### **Cache Structure and Organization**  
- **Cache Levels**: Caches near the processor are faster but smaller, with multiple levels for balancing speed and capacity.
- **Cache Lines and Sets**: Data in memory is split into **cache lines**, grouped by **set associativity**. This helps in **avoiding cache misses**.

### **Cache Side Channel Techniques**  
1. **Evict and Time**:
   - Evict specific data from the cache and monitor if victim actions slow down.
2. **Prime and Probe**:
   - Prime the cache with known data, run victim code, and then **retest cache timings** to see if the victim’s actions replaced data.
3. **Flush and Reload**:
   - Remove specific lines from cache, run victim code, and then **check if data was reloaded** by the victim.

### **Cache Side Channel Threats**  
- **Cross-Domain Attack**: Attacks on shared caches between processes or privilege levels, exploiting **timing variations**.
- **High Accuracy Needed**: Requires **precise timing measurements** and repeated runs to filter out noise.

---

## **Rowhammer**  
### **DRAM Vulnerability**  
Repeatedly accessing (or “hammering”) a memory row can cause **disturbance errors** in adjacent rows, leading to **unintended bit flips** in nearby memory.

- **Attack Scenario**: Manipulate memory to induce bit flips, potentially altering data or gaining control.
- **Mitigations**:
  - **Error-Correcting Code (ECC)** memory to detect and correct flips.
  - **Memory Controller Restrictions** on hammering, though these can impact performance.

---

## **Meltdown and Spectre Attacks**  
### **Understanding Speculative Execution**  
**Speculative Execution** and **Out-of-Order Execution** are optimizations that can cause data leakage.

- **Meltdown**: Exploits inadequate privilege checks in speculative execution, enabling attackers to access kernel memory.
  - **Mitigation**: Remove kernel memory mappings from user space or use newer processors with hardware fixes.
  
- **Spectre**: Manipulates **branch prediction** to induce speculative execution that leaks information.
  - **Mitigation**: Selectively disable speculation, use microcode patches, or implement architectural changes in new hardware.

### **Microarchitectural Side-Channel Risks**  
- **Modern Security Challenges**: Microarchitectural optimizations (like speculative execution) are under scrutiny as they may create new side channels.
- **Recent Exploits**: Include **L1TF, MDS, TAA,** and **iTLB multihit**, reflecting evolving attack vectors targeting these optimizations.

---

## **Summary**  
### Key Points  
- **Side Channels** reveal information via **resource usage** or **system emanations**.
- **Cache Side Channels** exploit shared cache timings to infer data usage.
- **Rowhammer** manipulates DRAM via disturbance errors to alter memory.
- **Speculative Execution Attacks** (Meltdown, Spectre) utilize modern CPU optimizations to leak protected information.

**Resources** for further reading:
- **Google Project Zero** (Rowhammer, Spectre/Meltdown)
- **TU Graz** and **VUSec** research teams on side channels and speculative execution.

---