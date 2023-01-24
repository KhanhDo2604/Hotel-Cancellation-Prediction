from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve(strict=True).parent
with open(f"{BASE_DIR}/model.pkl", "rb") as f:
    clf = pickle.load(f)

def predict(no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, required_car_parking_space, lead_time, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled):
    input = [no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, required_car_parking_space, lead_time, repeated_guest, no_of_previous_cancellations, no_of_previous_bookings_not_canceled]
    return clf.predict([input])[0]



