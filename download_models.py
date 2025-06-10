import os
import gdown

pretrained_id = "19mk5EPrfhFqtV2h1wx9eflYQr4SCqECs"
finetuned_id = "1O1L5r89LEm3pylf6uzkH90j6pG3pzk4s"

pretrained_dir = "pretrained models"
finetuned_dir = "fine-tuned"

os.makedirs(pretrained_dir, exist_ok=True)
os.makedirs(finetuned_dir, exist_ok=True)

pretrained_output = os.path.join(pretrained_dir, "SSAST-Base-Patch-400.pth")
print(f"Downloading pretrained model to: {pretrained_output}")
gdown.download(id=pretrained_id, output=pretrained_output, quiet=False)

finetuned_output = os.path.join(finetuned_dir, "best_ssast_model.pth")
print(f"Downloading fine-tuned model to: {finetuned_output}")
gdown.download(id=finetuned_id, output=finetuned_output, quiet=False)

print("Download complete.")
