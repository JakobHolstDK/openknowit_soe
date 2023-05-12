from flask import Flask, request, jsonify
import consul

app = Flask(__name__)

@app.route('/services', methods=['GET'])
def get_services():
    # Connect to Consul
    c = consul.Consul()

    # Get all keys under the 'services' prefix
    _, services = c.kv.get('services/', keys=True)

    # Extract service names from the keys
    service_names = [key.split('/')[-1] for key in services]

    return jsonify(service_names)

@app.route('/services/<service_name>', methods=['GET'])
def get_service(service_name):
    # Connect to Consul
    c = consul.Consul()

    # Get service data from Consul
    key = f'services/{service_name}/data'
    _, service_data = c.kv.get(key)

    # Return data as JSON
    return jsonify(service_data)

@app.route('/services', methods=['POST'])
def add_service():
    # Connect to Consul
    c = consul.Consul()

    # Get data from request
    service_name = request.json.get('name')
    service_data = request.json.get('data')

    # Add service data to Consul
    key = f'services/{service_name}/data'
    c.kv.put(key, service_data)

    return '', 201

@app.route('/services/<service_name>', methods=['PUT'])
def update_service(service_name):
    # Connect to Consul
    c = consul.Consul()

    # Get data from request
    service_data = request.json.get('data')

    # Update service data in Consul
    key = f'services/{service_name}/data'
    c.kv.put(key, service_data)

    return '', 204

@app.route('/services/<service_name>', methods=['DELETE'])
def delete_service(service_name):
    # Connect to Consul
    c = consul.Consul()

    # Delete service data from Consul
    key = f'services/{service_name}/data'
    c.kv.delete(key)

    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

