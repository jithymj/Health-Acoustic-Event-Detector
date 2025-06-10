# Health-Acoustic-Event-Detector

This project implements an acoustic event detection system for cough and sneeze classification using SSAST.

##  Model Architecture

- Pretrained Model: [SSAST-Base-Patch-400](https://drive.google.com/file/d/19mk5EPrfhFqtV2h1wx9eflYQr4SCqECs/view?usp=drive_link)
- Fine-tuned Model: [best_ssast_model.pth](https://drive.google.com/file/d/1O1L5r89LEm3pylf6uzkH90j6pG3pzk4s/view?usp=drive_link)

##  Download Models
## Project Structure
Health-Acoustic-Event-Detector/
├── models/
│ └── ast_models.py
├── python files/
│ ├── HAED.py
│ └── SSAST_finetune.py
├── download_models.py
├── README.md
└── .gitignore
```bash
python download_models.py
