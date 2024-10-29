import streamlit as st
import requests

API_URL = "http://localhost:8000"

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
categories = ["Buyer Management", "Car Inventory Management", "Seller Management", "Sales Management"]
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
