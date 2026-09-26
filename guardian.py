import subprocess
import re


AZURE_NETWORK = "10.1.0.0/16"
CAMPUS_NETWORK = "10.20.0.0/24"


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


def check_vpn():
    status = run_command("sudo ipsec statusall")
    xfrm = run_command("sudo ip xfrm policy")

    print("\n======================================")
    print("       CAMPUSVPN GUARDIAN")
    print("======================================\n")

    # -----------------------------
    # IKE CHECK
    # -----------------------------
    if "ESTABLISHED" in status:
        print("IKE Status          : ✓ ESTABLISHED")
    else:
        print("IKE Status          : ✗ NOT ESTABLISHED")

    # -----------------------------
    # IPsec CHECK
    # -----------------------------
    if "INSTALLED, TUNNEL" in status:
        print("IPsec Status        : ✓ INSTALLED")
    else:
        print("IPsec Status        : ✗ NOT INSTALLED")

    # -----------------------------
    # TRAFFIC CHECK
    # -----------------------------
    traffic = re.findall(
        r"(\d+) bytes_i.*?(\d+) bytes_o",
        status
    )

    if traffic:
        incoming, outgoing = traffic[-1]

        print(f"Traffic In          : {incoming} bytes")
        print(f"Traffic Out         : {outgoing} bytes")

        if int(incoming) > 0 and int(outgoing) > 0:
            print("Traffic Status      : ✓ ACTIVE")
        else:
            print("Traffic Status      : ⚠ NO TRAFFIC")
    else:
        print("Traffic Status      : ⚠ UNKNOWN")

    # -----------------------------
    # XFRM OUTBOUND POLICY
    # -----------------------------
    outbound = (
        f"src {CAMPUS_NETWORK} dst {AZURE_NETWORK}"
        in xfrm
        and "dir out" in xfrm
    )

    # -----------------------------
    # XFRM INBOUND POLICY
    # -----------------------------
    inbound = (
        f"src {AZURE_NETWORK} dst {CAMPUS_NETWORK}"
        in xfrm
        and "dir in" in xfrm
    )

    print("\n---------- ROUTING / IPSEC POLICY ----------")

    print(f"Campus Network      : {CAMPUS_NETWORK}")
    print(f"Azure Network       : {AZURE_NETWORK}")

    if outbound:
        print("Outbound Policy     : ✓ VALID")
    else:
        print("Outbound Policy     : ✗ MISSING")

    if inbound:
        print("Inbound Policy      : ✓ VALID")
    else:
        print("Inbound Policy      : ✗ MISSING")

    # -----------------------------
    # DIAGNOSIS
    # -----------------------------
    logs = run_command(
        "sudo journalctl -u strongswan-starter -n 100 --no-pager"
    )

    print("\n---------- DIAGNOSTIC ----------")

    if "NO_PROPOSAL_CHOSEN" in logs:
        print("Problem             : IKE/IPsec Proposal Mismatch")
        print("Recommendation      :")
        print("  Align encryption, integrity and DH group.")

    elif "AUTHENTICATION_FAILED" in logs:
        print("Problem             : Authentication Failure")
        print("Recommendation      :")
        print("  Verify PSK and IKE identity.")

    elif not outbound or not inbound:
        print("Problem             : IPsec Routing Policy Missing")
        print("Recommendation      :")
        print("  Check the campus and Azure network selectors.")

    elif (
        "ESTABLISHED" in status
        and "INSTALLED, TUNNEL" in status
        and outbound
        and inbound
    ):
        print("Problem             : None detected")
        print("Recommendation      : VPN tunnel and policies are operational.")

    else:
        print("Problem             : VPN state requires investigation")
        print("Recommendation      : Check VPN status, logs and routing.")


if __name__ == "__main__":
    check_vpn()
