from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_image():
    # Menerima file gambar dari request
    if "photo" not in request.files:
        return jsonify({"error": "No photo provided"}), 400

    photo = request.files["photo"]

    # Simpan file gambar di folder uploads
    photo_path = f"uploads/{photo.filename}"
    photo.save(photo_path)

    # Implementasi deteksi dan manipulasi gambar di sini
    # ...

    # Respon API dengan dua tempat
    response = {
        "result": "Tempat Pertama",
        "odontogram": "Tempat Kedua"
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
