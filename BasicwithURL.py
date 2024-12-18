# Import all required modules from Flask
from flask import *  # Import everything from Flask for simplicity

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the "admin" page
@app.route('/admin')
def admin():
    # Return a response indicating the admin section
    return "This is admin"

# Define a route for the "student" page
@app.route('/student')
def student():
    # Return a response indicating the student section
    return "This is student"

# Define a route for the "staff" page
@app.route('/staff')
def staff():
    # Return a response indicating the staff section
    return "This is staff"

# Define a route with a dynamic integer parameter
@app.route('/hello/<int:sub>')  # URL will accept an integer value after "/hello/"
def mahesh(sub):
    # Return a response displaying the integer value
    return 'Please subscribe = %d' % sub

# Define a route with a dynamic string parameter
@app.route('/user/<name>')  # URL will accept a string value after "/user/"
def user(name):
    # Check the value of the parameter and redirect accordingly
    if name == 'admin':
        return redirect(url_for('admin'))  # Redirect to the admin route
    if name == 'student':
        return redirect(url_for('student'))  # Redirect to the student route
    if name == 'staff':
        return redirect(url_for('staff'))  # Redirect to the staff route

# Run the Flask application when the script is executed directly
if __name__ == "__main__":
    # Start the Flask server in debug mode for development
    app.run(debug=True)
