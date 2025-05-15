# HalluVerse3: A Fine-Grained Multilingual Benchmark for Hallucination Detection in LLMs

**Authors**: Samir Abdaljalil, Hasan Kurban, Erchin Serpedin

**Paper Link**: Under Review

---

**HalluVerse3** is a multilingual benchmark dataset designed to advance hallucination detection research in large language models, featuring fine-grained, human-annotated hallucinations in English, Arabic, and Turkish across entity, relation, and sentence levels.

> ⚠️ **Note**: Experiment codes are currently under development. For support or implementation help, contact `sabdaljalil@tamu.edu` and include `[HalluVerse3 Request]` in the subject line.

---

## 🧾 Overview

- **Dataset Size**: ~3,200 entries  
- **Languages**: English, Arabic, Turkish 
- **Data Type**: Biographical Sentence-Level 
- **Hallucination Types**: Entity, Relation, Sentence

---

## 📥 Data Access

Download the full dataset here: [HalluVerse3 Download Link](https://huggingface.co/datasets/sabdalja/HalluVerse3) <!-- Replace with actual link -->


---

## 📂 Dataset Structure

```text
HalluVerse3/
├── en_final_data.csv
├── ar_final_data.csv
├── tr_final_data.csv
```
Create a **/dataset** directory in the root directory and place the files. 

---

## 🧠 Benchmark Tasks

HalluVerse3 supports multiple tasks regarding hallucination detection

### 🔹 Task 1: LLM Benchmarking on Fine-grained Multilingual Hallucination

- **Objective**: Identify the type of hallucination in multilingual data
- **Input**: Original Sentence + Edited Hallucinated Sentence
- **Output**: Class label ('Entity', 'Relation', 'Sentence')

### 🔹 Task 2: Hallucination Detection (Binary Classification)

- **Objective**: Predict likelihood of hallucination 
- **Input**: Original Sentence + Edited Hallucinated Sentence
- **Output**: Hallucination Score

---

