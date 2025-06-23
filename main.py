from flask import Flask, request, jsonify
from controller import *
app = Flask(__name__)

@app.route('/automate_azure_pricing', methods=['POST'])
def TranscribeSummary():
    try:
        data = request.get_json()
        response = Controller(data)
        return jsonify(response)
    except Exception as e:
        print(f"Error in Transcribe Summary: {str(e)}")
        return jsonify({
                "Error":str(e),
                "statusCode":500
            })
   


if __name__ == "__main__":
    app.run(debug=True , port="8080",host="0.0.0.0")