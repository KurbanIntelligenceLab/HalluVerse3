import pandas as pd
import glob
import os

path = "dataset/*.xlsx"
list_paths = glob.glob(path)

!pip install git+https://github.com/EngSalem/HaLo.git

!pip install --upgrade transformers huggingface_hub

import os
import openpyxl
import HaloCheck as checker
import nltk
nltk.download('punkt_tab')
scorer = checker.HaloCheck(device='cuda', granularity='sentence', nli_model='mnli')

for l in list_paths:

  lang = l.split('/')[-1].split('_')[0]
  print(f'{lang} started')
  df = pd.read_excel(l)

  ground_truths = list(df['orig_sentence'][:500])
  hal_data = list(df['edited_sentence'][:250])
  nonhal = list(df['edited_sentence'][250:500])

  all_data = hal_data + nonhal
  labels = [1] * 250 + [0] * 250


  excel_name = f"{lang}_haluscope.xlsx"
  if os.path.exists(excel_name):
    x = pd.read_excel(excel_name, sheet_name="QA_Log")
  else:
      x = pd.DataFrame(columns=["statement", "score", "label"])
      x.to_excel(excel_name, index=False, sheet_name="QA_Log")

  for q in range(len(all_data)):
    question = all_data[q]
    ground = ground_truths[q]
    label = labels[q]
    if question in x['statement'].values:
        print(f"Skipping duplicate question: {question}")
        continue

    # score = selfcheck(ground,[question])
    score = scorer.score([ground,question])
    new_data = pd.DataFrame([[question, score, label]], columns=["statement", "score", "label"])
    with pd.ExcelWriter(excel_name, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
        sheet_name = "QA_Log"
        new_data.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=writer.sheets[sheet_name].max_row)
  print(f'{lang} finished')
  


from sklearn.metrics import roc_auc_score, roc_curve
import pandas as pd
import glob
import matplotlib.pyplot as plt

# Path pattern for input files
path = "*haluscope.xlsx"
list_paths = glob.glob(path)

# Language colors matching example style
color_map = {
    'en': 'navy',    # assumed "best"
    'tr': 'darkorange',  # "better"
    'ar': 'green'    # "good"
}

# Plot order for the legend and plot lines
plot_order = ['en', 'tr', 'ar']

# Store plot data
plot_data = {}

# Collect ROC curves
for l in list_paths:
    lang = l.split('/')[-1].split('_')[0]
    if lang not in plot_order:
        continue

    df = pd.read_excel(l)
    y_true = df['label']
    y_score = df['score']
    roc_auc = roc_auc_score(y_true, y_score)
    fpr, tpr, _ = roc_curve(y_true, y_score)
    plot_data[lang] = (fpr, tpr, roc_auc)

# Plotting
plt.figure(figsize=(8, 6))

for lang in plot_order:
    if lang in plot_data:
        fpr, tpr, auc = plot_data[lang]
        # Thicker line for 'en' as in the example
        # linewidth = 2.5 if lang == 'en' else 1.8
        plt.plot(fpr, tpr, label=f'{lang} (AUC = {auc:.2f})', color=color_map[lang], linewidth=1.5)

# Chance diagonal line (red dashed)
plt.plot([0, 1], [0, 1], linestyle='--', color='darkred', linewidth=2, label='random')

# Axes formatting
plt.xlabel('False positive rate', fontsize=13)
plt.ylabel('True positive rate', fontsize=13)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Legend formatting
plt.legend(loc='lower right', fontsize=15)

plt.tight_layout()


# Save the plot
output_path = "combined_haluscope_roc_curves.png"
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()
