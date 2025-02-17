from flask import Flask, render_template, request
from mcstatus import JavaServer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def function1():
    output = ""
    if request.method == "POST":
        javaserver = request.form.get("javaserver")
        javaserverdata = JavaServer.lookup(javaserver)
        javaserverstatus = javaserverdata.status()
        javaserverping = javaserverdata.ping()

        

        output= f"Players online: {javaserverstatus.players.online}/{javaserverstatus.players.max}\n Ping1:{round(javaserverstatus.latency)}ms\n Ping2:{round(javaserverping)}ms\n Version: {javaserverstatus.version.name} ({javaserverstatus.version.protocol})\n Host: {javaserverdata.address.host}\n IP-address: {javaserverdata.address._cached_ip}\n Port: {javaserverdata.address.port}"

    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=20006, debug=True)