# ResLysEmbed

**ResLysEmbed: A ResNet-Based Framework for Succinylated Lysine Residue Prediction**

---

### Framework
![View ResLysEmbed Framework](https://github.com/Sheldor7701/ResLysEmbed/blob/main/Results/Plots/New%20ResLysEmbed-1.png)


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
    ```plaintext
    numpy==1.26.4
    pandas==2.2.1
    transformers==4.33.2
    torch==2.0.1
    scikit-learn==1.3.2
    shap==0.42.1
    tensorflow==2.14.0
    ```

Install the required libraries using:
```bash
pip install -r requirements.txt
```

---

### How to Use

#### Reproduce Results
1. Clone this repository:
    ```bash
    git clone https://github.com/sheldor7701/ResLysEmbed.git
    cd ResLysEmbed
    ```
2. Prepare the environment by installing the required libraries.
3. Train the model:
    - Use the provided `Training_Code.ipynb` notebook to train the ResLysEmbed model.
    - Preprocessed input files are included in the `Dataset` folder.
4. Evaluate the model:
    - The notebook includes steps to evaluate metrics such as Accuracy, MCC, AUROC, and AUPRC.
5. Interpret predictions using SHAP:
    - Run the SHAP analysis script provided to generate interpretability plots.

---

### Prediction

#### Prerequisites
- Install transformers and PyTorch to extract ProtT5 embeddings.
- Refer to ProtT5-XL-U50 for embedding generation.

#### Steps
1. Generate ProtT5 embeddings for the input protein sequences.
2. Use the provided prediction script to run the ResLysEmbed model and make predictions.

---

### Reproduce Metrics from the Paper
To reproduce the metrics presented in the paper:
1. Follow the steps in the `Training_Code.ipynb`.
2. Metrics such as Accuracy, MCC, and F1 Score can be computed directly using the provided evaluation scripts.

---

### Repository Structure
- `Dataset`: Contains the preprocessed datasets used for training and testing. However for the full data containing language model embeddings please refer to the link [Google Drive Link](https://drive.google.com/drive/folders/1H14eUyk3WzSsnKJHOmxgueGysxC820TJ?usp=sharing)
- `Codes`: Notebooks for training the ResLysEmbed model and all other additional experiments done in the paper.
- `SHAP_analysis`: Stores precomputed SHAP values and scripts for interpretability analysis.
- `Results`: Stores precomputed plots that highlight the performance of the model and evaluation metrics.
- `Models`: Contains the saved model and model weights for ResLysEmbed.
- `Reproduced_Works`: Contains previous works like [LMSuccSite](https://github.com/KCLabMTU/LMSuccSite) and [Psuc-EDBAM](https://github.com/wugenqiang/pSuc-EDBAM) reproduced.
---

<!-- ### Citation
If you use this framework in your research, please cite:

```bibtex
@article{ResLysEmbed2024,
  title={ResLysEmbed: A ResNet-Based Framework for Succinylated Lysine Residue Prediction},
  author={Souvik Ghosh, Md Muhaiminul Islam Nafi, and M Saifur Rahman},
  journal={Submitted to Bioinformatics},
  year={2024}
}
``` -->

---

### Contact
For queries, please reach out to:

- Souvik Ghosh - [email@example.com]
- Md Muhaiminul Islam Nafi - [email@example.com]
