from flask import Flask, render_template, request

app = Flask(__name__)

translate = {
    "A": "U", "F": "E", "K": "I", "P": "M", "U": "R", "Z": "V", "B": "J", "G": "A",
    "L": "X", "Q": "F", "V": "O", "C": "N", "H": "D", "M": "P", "R": "K", "W": "B",
    "D": "W", "I": "C", "N": "Y", "S": "G", "X": "Z", "E": "L", "J": "H", "O": "S",
    "T": "Q", "Y": "T"
}

def translate_str(input_str):
    new_str = ""
    for letter in input_str.upper():
        if letter == " ":
            new_str += " "
        elif letter in translate:
            new_str += translate[letter]
        else:
            new_str += letter
    return new_str

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['input_string']
        translated_output = translate_str(user_input)
        return render_template('index.html', input_string=user_input, translated_output=translated_output)
    return render_template('index.html', input_string="", translated_output="")

if __name__ == '__main__':
    app.run(debug=True)
