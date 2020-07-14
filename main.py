"""NAPALM WEB APP."""

import xmltodict
# import flask
from flask import Flask, render_template, request, jsonify
from napalm import get_network_driver

# create an app instance
app = Flask(__name__)


# at the end point /
@app.route("/")
def main():
    """Return or render main html page."""
    # returns main.html if __name__ == "__main__":
    # on running python main.py
    return render_template("menu.html")
    # run the flask app
    app.run(debug=True)


# at the end point /
@app.route("/get_facts", methods=['GET', 'POST'])
def get_facts():
    """Call get_facts method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_facts()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_interfaces", methods=['GET', 'POST'])
def get_interfaces():
    """Call get_interfaces method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_interfaces()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_interfaces_counters", methods=['GET', 'POST'])
def get_interfaces_counters():
    """Call get_interfaces_counters method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_interfaces_counters()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_interfaces_ip", methods=['GET', 'POST'])
def get_interfaces_ip():
    """Call get_interfaces_ip method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_interfaces_ip()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_arp_table", methods=['GET', 'POST'])
def get_arp_table():
    """Call get_arp_table method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_arp_table()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_mac_address_table", methods=['GET', 'POST'])
def get_mac_address_table():
    """Call get_mac_address_table method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_mac_address_table()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_environment", methods=['GET', 'POST'])
def get_environment():
    """Call get_environment method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_environment()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_users", methods=['GET', 'POST'])
def get_users():
    """Call get_users method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_users()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_ntp_peers", methods=['GET', 'POST'])
def get_ntp_peers():
    """Call get_ntp_peers method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_ntp_peers()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_ntp_servers", methods=['GET', 'POST'])
def get_ntp_servers():
    """Call get_ntp_servers method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_ntp_servers()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_ntp_stats", methods=['GET', 'POST'])
def get_ntp_stats():
    """Call get_ntp_stats method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_ntp_stats()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_bgp_config", methods=['GET', 'POST'])
def get_bgp_config():
    """Call get_bgp_config method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_bgp_config()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_bgp_neighbors", methods=['GET', 'POST'])
def get_bgp_neighbors():
    """Call get_bgp_neighbors method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_bgp_neighbors()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_bgp_neighbors_detail", methods=['GET', 'POST'])
def get_bgp_neighbors_detail():
    """Call get_bgp_neighbors_detail method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_bgp_neighbors_detail()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_lldp_neighbors", methods=['GET', 'POST'])
def get_lldp_neighbors():
    """Call get_lldp_neighbors method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_lldp_neighbors()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_lldp_neighbors_detail", methods=['GET', 'POST'])
def get_lldp_neighbors_detail():
    """Call get_lldp_neighbors_detail method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_lldp_neighbors_detail()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_probes_config", methods=['GET', 'POST'])
def get_probes_config():
    """Call get_probes_config method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_probes_config()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_probes_results", methods=['GET', 'POST'])
def get_probes_results():
    """Call get_probes_results method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_probes_results()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_snmp_information", methods=['GET', 'POST'])
def get_snmp_information():
    """Call get_snmp_information method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_snmp_information()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/is_alive", methods=['GET', 'POST'])
def is_alive():
    """Call is_alive method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.is_alive()
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_route_to", methods=['GET', 'POST'])
def get_route_to():
    """Call get_route_to method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        ip_address = request.form["route"]
        protocol = request.form["protocol"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_route_to(ip_address, protocol)
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/traceroute", methods=['GET', 'POST'])
def traceroute():
    """Call traceroute method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        ip_address = request.form["route"]
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.traceroute(ip_address)
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_running_config", methods=['GET', 'POST'])
def get_running_config():
    """Call get_running_config method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_config(retrieve="running")["running"]
        if network_driver == "iosxr_netconf":
            return jsonify(xmltodict.parse(result))
        return jsonify(result)
    # run the flask app
    app.run()

# at the end point /
@app.route("/get_candidate_config", methods=['GET', 'POST'])
def get_candidate_config():
    """Call get_candidate_config method."""
    if request.method == "POST":
        network_driver = request.form["ndriver"]
        host_name = request.form["hname"]
        username = request.form["uname"]
        password = request.form["pwd"]
        port = request.form["port"]
        optional_args = {}
        if port:
            optional_args = {'port': port}
        driver = get_network_driver(network_driver)
        device = driver(host_name, username, password, optional_args=optional_args)
        device.open()
        result = device.get_config(retrieve="candidate")["candidate"]
        if network_driver == "iosxr_netconf":
            return jsonify(xmltodict.parse(result))
        return jsonify(result)
    # run the flask app
    app.run()


if __name__ == "__main__":
    app.run()
