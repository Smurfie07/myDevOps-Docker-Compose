from flask import Flask
import random
import prometheus_client
from flask import Response

app = Flask(__name__)

rCode = prometheus_client.Counter(
    "rCode",
    "R: "
)

gCode = prometheus_client.Counter(
    "gCode",
    "G: "
)

bCode = prometheus_client.Counter(
    "bCode",
    "B: "
)

@app.route("/")
def Body():
    return "Hello DevOps World!"

@app.route("/newPage")
def newPage():
    rdec = random.randint(0,255)
    gdec = random.randint(0,255)
    bdec = random.randint(0,255)
    rgddec = [rdec, gdec, bdec]

    rCode = rdec
    gCode = gdec
    bCode = bdec

    return ("{} \t R: {},\n G: {},\n B: {},\n").format(rgddec, rCode, gCode, bCode)

@app.route("/metrics")
def getMetrics():
    return Response(
        response = prometheus_client.generate_latest(),
        mimetype = "text/plain",
    )

if __name__ == "__main__":
    Flask.run(app, host = "0.0.0.0", port = 3300)