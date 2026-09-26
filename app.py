from flask import Flask, render_template
import subprocess
import re

app = Flask(__name__)


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=15
        )
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)


def get_vpn_status():

    status = run_command("sudo ipsec statusall")
    xfrm = run_command("sudo ip xfrm policy")

    ike = "ESTABLISHED" in status
    ipsec = "INSTALLED, TUNNEL" in status

    traffic = re.findall(
        r"(\d+) bytes_i.*?(\d+) bytes_o",
        status
    )

    if traffic:
        traffic_in = int(traffic[-1][0])
        traffic_out = int(traffic[-1][1])
    else:
        traffic_in = 0
        traffic_out = 0

    traffic_active = traffic_in > 0 and traffic_out > 0

    outbound = (
        "src 10.20.0.0/24 dst 10.1.0.0/16" in xfrm
        and "dir out" in xfrm
    )

    inbound = (
        "src 10.1.0.0/16 dst 10.20.0.0/24" in xfrm
        and "dir in" in xfrm
    )

    if ike and ipsec and traffic_active and outbound and inbound:
        diagnosis = "VPN tunnel is operational."
        severity = "success"

    elif not ike:
        diagnosis = "IKE negotiation is not established."
        severity = "danger"

    elif not ipsec:
        diagnosis = "IPsec tunnel is not installed."
        severity = "danger"

    elif not outbound or not inbound:
        diagnosis = "Possible asymmetric routing or missing IPsec policy."
        severity = "warning"

    else:
        diagnosis = "VPN requires investigation."
        severity = "warning"

    return {
        "ike": ike,
        "ipsec": ipsec,
        "traffic_in": traffic_in,
        "traffic_out": traffic_out,
        "traffic_active": traffic_active,
        "outbound": outbound,
        "inbound": inbound,
        "diagnosis": diagnosis,
        "severity": severity
    }


@app.route("/")
def dashboard():
    status = get_vpn_status()
    return render_template("dashboard.html", status=status)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
