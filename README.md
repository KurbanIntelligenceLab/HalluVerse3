# HalluVerse3: A Fine-Grained Multilingual Benchmark for Hallucination Detection in LLMs

**Authors**: Samir Abdaljalil, Hasan Kurban, Erchin Serpedin

**Paper Link**: [Under Review](https://arxiv.org/abs/2503.07833)

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

## 🚀 Getting Started

Follow these steps to use the dataset and run benchmarks.

### 1. Clone the Repository

```bash
git clone https://github.com/sabdaljalil2000/HalluVerse3.git
cd HalluVerse3
```

### 1. Clone the Repository

Download all required dependencies 


### 2. Download the Dataset

```bash
mkdir data
```
Download the dataset files and place them in the \data directory 

### 3. Run Benchmark Tasks

- Task 1: LLM Benchmarking

  ```bash
  cd Tasks/Task 1
  python llm_benchmarking.py
  ```

- Task 2: Detection Model Evaluation

  - SelfCheckGPT:
    ```bash
    cd Tasks/Task 2
    python SelfCheck_Detection.py
    ```
  - HaloCheck:
    ```bash
    cd Tasks/Task 2
    python HaluScope_Detection.py
    ```
