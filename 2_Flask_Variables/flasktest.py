from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  
  username = "BobTheBuilder"
  user_age = 40
  fruit_list = ['apple', 'orange', 'pear']
  
  return render_template(
    "./basic.html",
    name = username,
    age = user_age,
    fruits = fruit_list
  )

app.run(host="127.0.0.1", port=4444)

if __name__ == "__main__":
  app.run(debug=True)
