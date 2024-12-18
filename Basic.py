# Import necessary modules from Flask
from flask import Flask, request, jsonify

# Create an instance of the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")  # This binds the function to the URL "/"
def home():
    # Return a simple response when the home page is accessed
    return "Home"

# Run the application only if this script is executed directly
if __name__ == "__main__":
    # Start the Flask development server in debug mode
    app.run(debug=True)
