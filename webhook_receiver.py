# -*- coding: utf-8 -*- 
from flask import Flask, request, jsonify 
from trader import execute_trade 
 
app = Flask(__name__) 
 
@app.route("/webhook", methods=["POST"]) 
def webhook(): 
    data = request.get_json() 
    if not data or "signal" not in data: 
        return jsonify({"error": "Se¤al no encontrada"}), 400 
    signal = data["signal"].upper() 
    if signal in ["CALL", "PUT"]: 
        print(f"? Se¤al recibida desde TradingView: {signal}") 
        execute_trade(signal) 
        return jsonify({"status": "Operaci¢n ejecutada"}), 200 
    else: 
        return jsonify({"error": "Se¤al inv lida"}), 400 
 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000) 
