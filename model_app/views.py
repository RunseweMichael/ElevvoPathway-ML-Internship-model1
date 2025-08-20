from django.shortcuts import render
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../student_score_prediction_model")
model = joblib.load(MODEL_PATH)

def home(request):
    prediction = None

    if request.method == "POST":
        hours = float(request.POST.get("hours"))
        prediction = model.predict([[hours]])[0]

    return render(request, "model_app/home.html", {"prediction": prediction})


def custom_404(request, exception):
    return render(request, '404.html', status=404)