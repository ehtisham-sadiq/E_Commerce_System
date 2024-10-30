import streamlit as st
import requests

API_URL = "http://localhost:8000"


#Functions for user authentication
def user_register(name, password, email):
    payload = {
            "username": name,
            "password": password,
            "email": email
            }
    response=requests.post(f"{API_URL}/register", json=payload)
    return response
def user_login(name, password):
    payload = {
            "username": name,
            "password": password,
            }
    response=requests.post(f"{API_URL}/login", json=payload)
    return response

# Functions for Buyer Management
def create_buyer(name, contact):
    response = requests.post(f"{API_URL}/buyers", json={
        "name": name,
        "contact": contact
    })
    return response

def get_buyers():
    response = requests.get(f"{API_URL}/buyers")
    return response.json() if response.status_code == 200 else []

def get_buyer(buyer_id):
    response = requests.get(f"{API_URL}/buyers/{buyer_id}")
    return response.json() if response.status_code == 200 else None

def update_buyer(buyer_id, name, contact):
    response = requests.put(f"{API_URL}/buyers/{buyer_id}", json={
        "name": name,
        "contact": contact
    })
    return response

def delete_buyer(buyer_id):
    response = requests.delete(f"{API_URL}/buyers/{buyer_id}")
    return response

# Functions for Car Inventery Management

# Functions for Seller Management

# Functions for Sale Management


# Set page config
st.set_page_config(page_title="E-Commerce System", layout="wide")
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #4CAF50; /* Green color */
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #555555; /* Dark gray color */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>E-Commerce System</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>Select a category to manage</h2>", unsafe_allow_html=True)

# Sidebar for category selection
categories = ["Authentication", "Buyer Management", "Car Inventory Management", "Seller Management", "Sales Management"]
selected_category = st.sidebar.selectbox("Categories", categories)


if selected_category == "Buyer Management":
    st.subheader("Buyer Management")
    menu = ["Add Buyer", "View Buyers", "Update Buyer", "Delete Buyer"]
    choice = st.selectbox("Select an option", menu)

    if choice == "Add Buyer":
        st.subheader("Add New Buyer")
        name = st.text_input("Name")
        contact = st.text_input("Contact Number")

        if st.button("Submit"):
            result = create_buyer(name, contact)
            if result.status_code == 200:
                st.success("✅ Buyer added successfully!")
            else:
                st.error("❌ Error adding buyer: " + result.json().get('detail', 'Unknown error'))

    elif choice == "View Buyers":
        st.subheader("All Buyers")
        buyers = get_buyers()
        if buyers:
            for buyer in buyers:
                st.write(f"**ID:** {buyer['id']}, **Name:** {buyer['name']}, **Contact:** {buyer['contact']}")
        else:
            st.write("🚫 No buyers found.")

    elif choice == "Update Buyer":
        st.subheader("Update Buyer")
        buyer_id = st.number_input("Enter Buyer ID", min_value=1, step=1)
        buyer = get_buyer(buyer_id)

        if buyer:
            name = st.text_input("New Name", value=buyer['name'])
            contact = st.text_input("New Contact", value=buyer['contact'])

            if st.button("Update"):
                result = update_buyer(buyer_id, name, contact)
                if result.status_code == 200:
                    st.success("✅ Buyer updated successfully!")
                else:
                    st.error("❌ Error updating buyer: " + result.json().get('detail', 'Unknown error'))
        else:
            st.error("🚫 Buyer not found.")

    elif choice == "Delete Buyer":
        st.subheader("Delete Buyer")
        buyer_id = st.number_input("Enter Buyer ID to delete", min_value=1, step=1)

        if st.button("Delete"):
            result = delete_buyer(buyer_id)
            if result.status_code == 200:
                st.success("✅ Buyer deleted successfully!")
            else:
                st.error("❌ Error deleting buyer: " + result.json().get('detail', 'Unknown error'))

elif selected_category == "Authentication":
    # Tab structure to switch between Registration and Login
    tab1, tab2 = st.tabs(["Register", "Login"])

    # Registration Form
    with tab1:
        st.header("User Registration")
        username = st.text_input("Username (required)", key="reg_username")
        password = st.text_input("Password (required)", type="password", key="reg_password")
        email = st.text_input("Email (optional)", key="reg_email")
        if not email:
            email=None

        if st.button("Register"):
            # Check that required fields are filled
            if username and password:
                # Send POST request to FastAPI registration endpoint
                try:
                    response = user_register(username,password,email)
                    if response.status_code == 200:
                        data = response.json()
                        st.success(f"✅ User {data} registered successfully!")
                    else:
                        st.error(f"❌ Registration failed: {response.json().get('detail', 'Unknown error')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Connection error: {e}")
            else:
                st.warning("Please fill out all required fields.")

    # Login Form
    with tab2:
        st.header("User Login")
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            # Check that required fields are filled
            if login_username and login_password:
                # Send POST request to FastAPI login endpoint
                try:
                    response = user_login(login_username,login_password)
                    if response.status_code == 200:
                        data = response.json()
                        st.success("✅ Login successful!")
                        st.write(f"Welcome, {data['username']}!")
                        st.write(f"JWT Token: {data['token']}")
                    else:
                        st.error(f"❌ Login failed: {response.json().get('detail', 'Unknown error')}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Connection error: {e}")
            else:
                st.warning("Please enter both username and password.")
                
elif selected_category == "Car Inventory Management":
    st.subheader("Car Inventory Management")
    # Place code for car inventory management here

elif selected_category == "Seller Management":
    st.subheader("Seller Management")
    # Place code for seller management here

elif selected_category == "Sales Management":
    st.subheader("Sales Management")
    # Place code for sales management here

# Exit button
if st.button("Exit"):
    st.write("👋 Thank you for using the E-Commerce System!")
