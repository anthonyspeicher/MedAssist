# random placeholder analysis
import random

def analyze_image(file_obj):
    # conditions in NIH dataset
    conditions = [
        "Atelectasis", "Consolidation", "Infiltration", "Pneumothorax",
        "Edema", "Emphysema", "Fibrosis", "Effusion",
        "Pneumonia", "Pleural_thickening", "Cardiomegaly",
        "Nodule", "Mass", "Hernia"
    ]

    # super secret selection process, very optimized
    condition = random.choice(conditions)
    confidence = round(random.uniform(0.6, 0.99), 2)

    return {"condition": condition, "confidence": confidence}
