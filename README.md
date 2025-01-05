# ResLysEmbed

**ResLysEmbed: A ResNet-Based Framework for Succinylated Lysine Residue Prediction**

---

### Framework
![ResLysEmbed](https://github.com/user-attachments/assets/f1a30878-0d3d-4f4c-9745-f6483fca0104)

ResLysEmbed is a novel deep learning framework designed to predict lysine succinylation sites with high accuracy and interpretability. This repository includes the implementation, preprocessed datasets, and instructions for reproducing the results from the accompanying paper.

---

### Key Features
- Hybrid architecture combining ResNet (for word embeddings) and MLP (for protein language model embeddings).
- Utilizes ProtT5 embeddings for robust contextual understanding.
- SHAP (SHapley Additive exPlanations) analysis for interpretability.
- Achieves state-of-the-art performance compared to existing methods.

---

### Data Availability
All training and independent datasets are provided in the [`Dataset`](Dataset) folder. The dataset includes preprocessed sequences, ProtT5 embeddings, and PSSM profiles as used in the paper.

---

### Environment Setup
- **OS**: Ubuntu 22.04.4 LTS
- **Python Version**: 3.9.19
- **Required Libraries**:
    ```
    numpy==1.26.4
    pandas==2.2.1
    transformers==4.33.2
    torch==2.0.1
    scikit-learn==1.3.2
    shap==0.42.1
    ```

Install the required libraries using:
```bash
pip install -r requirements.txt
```

## How to Use

### Reproduce Results

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Sheldor7701/ResLysEmbed.git
   cd ResLysEmbed
    ```
