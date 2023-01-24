from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f"{BASE_DIR}/model.pkl", "rb") as f:
    clf = pickle.load(f)

def predict(adults, children, parking, repeated_guest, lead_time, weekend, weekday, prev_cancel):
    input = [adults, children, parking, repeated_guest, lead_time, weekend, weekday, prev_cancel]
    return clf.predict([input])[0]

