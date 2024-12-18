from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define an endpoint to retrieve user data
# The URL pattern has a typo (missing "<" for user_id variable in route definition).
@app.route("/get-user/<user_id>")
def get_user(user_id):
    # Simulate user data with a hardcoded dictionary
    user_data = {
        "user_id": user_id,
        "name": "Mahesh",
        "email": "mahesh.k@example.com"
    }
    
    # Check for optional query parameter 'extra'
    extra = request.args.get("extra")
    if extra:
        # Add 'extra' to the user_data dictionary if present
        user_data["extra"] = extra

    # Return the user data as a JSON response with HTTP 200 status code
    return jsonify(user_data), 200

# Define an endpoint to create a new user
# This endpoint expects a POST request with JSON payload
@app.route("/create-user", methods=["POST"])
def create_user():
    # Retrieve JSON data from the incoming request
    data = request.get_json()

    # Respond with the same data and an HTTP 201 status code
    return jsonify(data), 201

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
