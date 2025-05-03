
from flask import Flask, request

app = Flask(__name__)

def multiply(value, multiplier):
    return f"{value}*{multiplier}", value*multiplier

def powered(value, power):
    return f"{value} to the power {power}", value**power

@app.route("/value=<int:value>&multi=<int:multi>", methods = ['GET'])
def counter(value, multi):
    string_, output_ = multiply(value, multi)
    return { "operation": string_, "output": output_  }

@app.route("/value=<int:value>&power=<int:power>", methods = ['GET'])
def expon(value, power):
    string_, output_ = powered(value, power)
    return { "operation": string_, "output": output_  }

@app.route("/calculate",methods = ['GET', 'POST'])
def calci():
    value = request.args.get('value', default=1, type=int)
    multi = request.args.get('multi', type=int)
    power = request.args.get('power', type=int)

    if (multi is not None) & (power is not None):
        return {"message": "This method is not allowed."}
    
    if multi:
        return counter(value, multi)
    
    if power:
        return expon(value, power)
    
    return {"message": "Operation failed."}

if __name__ == "__main__":
    app.run(debug=True)