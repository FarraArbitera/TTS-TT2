from flask import Flask, redirect, url_for, request, jsonify
from flask import send_file
#from text_to_speech import text_to_speech_process
app = Flask(__name__)

@app.route('/text-to-speech/<sentence>',methods = ['POST', 'GET'])
def text_to_speech(sentence):

    #sentence = request.json['sentence']
    request.args.get('sentence')

    path_to_file = "audio/2.wav" # ganti dengan text_to_speech_process()

    
    return send_file(
    path_to_file, 
    mimetype="audio/wav", 
    as_attachment=True, 
    download_name="2.wav")

    
    

    
    return jsonify({"response": "Hi " + sentence})


if __name__ == '__main__':
   app.run(debug = True)