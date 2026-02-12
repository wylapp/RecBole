from recbole.quick_start.quick_start import load_data_and_model
from recbole.trainer import Trainer

# Load saved data and model
config, model, dataset, train_data, valid_data, test_data = load_data_and_model(
    model_file='saved/NARM-Jan-30-2026_10-59-11.pth'  # Replace with your model path
)

# Initialize trainer with loaded model
trainer = Trainer(config, model)

# Perform evaluation on test data (no training needed)
result = trainer.evaluate(test_data, load_best_model=False, show_progress=True)
print(result)  # Outputs metrics like recall@10, ndcg@10, etc.