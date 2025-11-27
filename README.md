# crochet-motif-detection-thesis
# Crochet Motif Detection – Bachelor's Thesis (Image Processing & Deep Learning)

This repository contains the complete documentation and source code of my Bachelor's Thesis, which has the automatic detection and classification of crochet/knitting motifs using image processing methods and convolutional neural networks. The project explores the potential of deep learning–based pattern recognition in textile crafts, a domain where structured motif identification still remains largely manual.

## 🎓 Thesis Overview

Handcrafted crochet motifs exhibit rich visual variability in terms of texture, geometry, and structural complexity. Manual identification of these motifs requires domain expertise and is prone to errors.  
The aim of this thesis is to develop a computational pipeline capable of:

1. **Preprocessing motif images** (contrast enhancement, denoising, segmentation)  
2. **Extracting discriminative visual features**  
3. **Classifying motifs** using Convolutional Neural Networks  
4. Providing users with the corresponding **motif name** and a **guide to reproduce it**

## 🧠 Research Motivation

Although deep learning is widely applied in object recognition, medical imaging, and scene understanding, there is limited academic work on **structured textile motif analysis**.  
The research addresses the following questions:

- *Can convolutional neural networks reliably identify handcrafted crochet motifs?*  
- *Which preprocessing methods improve recognition accuracy for textured, repetitive patterns?*  
- *How transferable are architectures such as ResNet to this domain?*  

The study situates itself at the intersection of **computer vision**, **pattern recognition**, and **traditional craft digitization**.

---

## 🔬 Methodology

### **1. Data Preparation**
- Creating database from independent research
- Image normalization  

### **2. Model Architecture**
The backbone of the system is a **ResNet-based Convolutional Neural Network**, chosen for its proven performance in hierarchical feature extraction.  
Transfer learning was employed to leverage pretrained ImageNet weights, followed by fine-tuning on motif-specific data.

### **3. Evaluation Metrics**
- Accuracy  
- Precision / Recall  
- Confusion matrices  
- Feature visualization via activation maps  

### **4. Implementation Tools**
- **Python**  
- **googlecolab**  
- **PyTorch**  
- **NumPy / SciPy**  



