from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        
        # Create 'static' folder if not exists
        os.makedirs("static", exist_ok=True)
        
        filepath = "static/input.jpg"
        file.save(filepath)

        img = cv2.imread(filepath)
        stylized = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
        cv2.imwrite("static/output.jpg", stylized)

        return render_template("index.html", output="static/output.jpg")

    return render_template("index.html", output=None)

if __name__ == "__main__":
    app.run(debug=True)
