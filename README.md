# ReRec-RecBole - A Modified Version of RecBole

This repository contains a modified version of the [RecBole](https://github.com/RUCAIBox/RecBole) framework, tailored for enhanced compatibility and performance with the **ReRec dataset**.

## Key Improvements

- **Enhanced Data Loading & Processing**:  
  Optimized dataloader and data processing scripts to handle the large-scale ReRec dataset reliably, addressing edge cases where the original RecBole modules might fail.

- **Updated Dependencies**:  
  Modernized package dependencies for improved performance on contemporary hardware. Minor adjustments were made to resolve compatibility issues.

## Getting Started

### 1. Environment Setup

Clone or download this repository to your local machine. Choose one of the following methods to set up your environment:

#### Using `pip`
```bash
pip install -r requirements.txt
```

#### Using `conda`
```bash
conda env create -f bole.yaml
conda activate recbole-env
```

> Ensure your GPU drivers are properly installed.  
> Our default environment: Debian 12 with PyTorch 2.2.1 + CUDA 12.1.

### 2. Data Preparation

1. Download the ReRec dataset from the [HuggingFace repository](https://huggingface.co/datasets/wyoul/ReRec) into the `dataset/ReRec` folder.
2. Decompress the files using `gunzip`.
3. Verify that the following files exist in the `dataset/ReRec` directory:
   ```
   ReRec_log_5core_ts.csv
   ReRec_metadata.csv
   ```

4. Use the provided format conversion script `ReRec_recbole_convert.ipynb` (from the [ReRec main repository](https://github.com/wylapp/ReRec)) to generate atomic files. Place the script in `dataset/ReRec` and execute it.

Upon completion, your `dataset/ReRec` folder should look like this:
```
dataset
└── ReRec
    ├── ReRec.inter
    ├── ReRec.item
    ├── ReRec_log_5core_ts.csv
    ├── ReRec_metadata.csv
    ├── ReRec_recbole_convert.ipynb
    ├── smap.json
    ├── umap.json
    └── valid_meta_index.pkl
```

---

### 3. Model Training & Testing

> ⚠️ **Important**: Do not install `recbole` via `pip` or `conda`. Ensure it is not already present in your environment.

#### Training
Prepare a configuration file for your desired model. While most models share common configurations, some may require model-specific settings. Refer to the [RecBole documentation](https://recbole.io/docs/v1.2.0/recbole/recbole.model.sequential_recommender.html) for details. A sample config template is available in the `props/` folder.

Start training with:
```bash
python run_recbole.py --model NARM --config_files ./props/Sample.yaml
```
This command initiates a training-evaluation loop, automatically proceeding to testing after the final epoch or early stopping.

#### Manual Testing
By default, the best-performing model checkpoints are saved in the `saved/` folder. To manually run testing:

1. Edit `run_test.py` to specify your checkpoint:
   ```python
   config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
       model_file='saved/NARM-Jan-30-2026_10-59-11.pth'  # Replace with your model path
   )
   ```

2. Execute the script:
   ```bash
   python run_test.py
   ```

## Additional Resources

- [ReRec Dataset on HuggingFace](https://huggingface.co/datasets/wyoul/ReRec)
- [ReRec Main Repository](https://github.com/wylapp/ReRec)
