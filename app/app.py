#with open("/data/log.txt", "a") as f:
 #    f.write("Devops Day 8 learning\n")

#print("Message written to volume")
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps pipeline deployed on AWS!"

app.run(host="0.0.0.0", port=5000)
