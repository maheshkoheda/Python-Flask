
## Testing the Basicwith URL Application

### Test Static Routes
1. Open a web browser or an API client like [Postman](https://www.postman.com/) or use `curl`.
2. Access the following URLs:
   - **Admin Route**:  
     ```
     http://127.0.0.1:5000/admin
     ```
     **Expected Response**: `This is admin`
   - **Student Route**:  
     ```
     http://127.0.0.1:5000/student
     ```
     **Expected Response**: `This is student`
   - **Staff Route**:  
     ```
     http://127.0.0.1:5000/staff
     ```
     **Expected Response**: `This is staff`

### Test Dynamic Routes
1. **Test `/hello/<int:sub>`**:
   - Replace `<int:sub>` with any integer.
   - Example:  
     ```
     http://127.0.0.1:5000/hello/123
     ```
     **Expected Response**: `Please subscribe = 123`

2. **Test `/user/<name>`**:
   - Replace `<name>` with one of the following:
     - `admin`: Redirects to `/admin`.
     - `student`: Redirects to `/student`.
     - `staff`: Redirects to `/staff`.
   - Example:  
     ```
     http://127.0.0.1:5000/user/admin
     ```
     **Expected Result**: Redirects to `http://127.0.0.1:5000/admin` with the response `This is admin`.

### Test Invalid Routes
- Access an undefined route, such as:
  ```
  http://127.0.0.1:5000/unknown
  ```
- **Expected Response**: A `404 Not Found` error.

--- 

This provides clear steps for testing FlaskAPIMethods.
------
# Flask API: User Management

This Flask application provides two endpoints to manage user data:

- **GET /get-user/<user_id>**: Retrieve user data.
- **POST /create-user**: Create a new user.

---

## Prerequisites

1. Install Python (version 3.6 or higher).
2. Install the required Python package:
   ```bash
   pip install flask
   ```

---

## Running the Application

1. Start the Flask app by running the following command:
   ```bash
   python app.py
   ```

2. The app will start on `http://127.0.0.1:5000/` (default localhost and port).

---

## API Endpoints

### 1. **GET /get-user/<user_id>**

#### Description
Retrieves user data based on the `user_id` provided in the URL. Optionally, you can include an `extra` query parameter to add additional information.

#### Example Request

Using `curl`:
```bash
curl -X GET "http://127.0.0.1:5000/get-user/123?extra=admin"
```

Using Postman:
- Set the request type to **GET**.
- URL: `http://127.0.0.1:5000/get-user/123?extra=admin`

#### Example Response
```json
{
  "user_id": "123",
  "name": "Mahesh",
  "email": "mahesh.k@example.com",
  "extra": "admin"
}
```

### 2. **POST /create-user**

#### Description
Creates a new user with the data provided in the JSON body of the request.

#### Example Request

Using `curl`:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_id": "456", "name": "John Doe", "email": "john.doe@example.com"}' http://127.0.0.1:5000/create-user
```

Using Postman:
- Set the request type to **POST**.
- URL: `http://127.0.0.1:5000/create-user`
- Go to the **Body** tab and select **raw** and set it to `JSON`.
- Enter the JSON data:
  ```json
  {
    "user_id": "456",
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

#### Example Response
```json
{
  "user_id": "456",
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

---

## Notes

1. Ensure the `user_id` provided in the URL for **GET** requests is valid.
2. The `create-user` endpoint does not currently validate the input. Consider adding input validation to ensure the JSON body contains all required fields.

