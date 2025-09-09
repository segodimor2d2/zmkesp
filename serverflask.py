from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receber():
    data = request.get_json()  # pega JSON enviado pelo ESP32
    print(data)

    # responde para o ESP32
    return jsonify({"serverflask": "reseived"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)  # acessível na rede local


# python serverflask.py
# post_data("http://192.168.31.100:5000/api/teste", {"msg": "olá ESP32", "valor": 42})
