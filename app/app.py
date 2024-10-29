import streamlit as st
import requests

API_URL = "http://localhost:8000"

# Functions for Seller Management
def create_seller(name, contact_details, address):
    response = requests.post(f"{API_URL}/sellers", json={
        "name": name,
        "contact_details": contact_details,
        "address": address
    })
    return response

def get_sellers():
    response = requests.get(f"{API_URL}/sellers")
    return response.json() if response.status_code == 200 else []

def get_seller(seller_id):
    response = requests.get(f"{API_URL}/sellers/{seller_id}")
    return response.json() if response.status_code == 200 else None

def update_seller(seller_id, name, contact_details, address):
    response = requests.put(f"{API_URL}/sellers/{seller_id}", json={
        "name": name,
        "contact_details": contact_details,
        "address": address
    })
    return response

def delete_seller(seller_id):
    response = requests.delete(f"{API_URL}/sellers/{seller_id}")
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

    # Seller Management Section
if selected_category == "Seller Management":
    st.subheader("Seller Management")
    menu = ["Add Seller", "View Sellers", "Update Seller", "Delete Seller"]
    choice = st.selectbox("Select an option", menu)

    if choice == "Add Seller":
        st.subheader("Add New Seller")
        name = st.text_input("Name")
        contact_details = st.text_input("Contact Details")
        address = st.text_input("Address")

        if st.button("Submit"):
            result = create_seller(name, contact_details, address)
            if result.status_code == 200:
                st.success("✅ Seller added successfully!")
            else:
                st.error("❌ Error adding seller: " + result.json().get('detail', 'Unknown error'))

    elif choice == "View Sellers":
        st.subheader("All Sellers")
        sellers = get_sellers()
        if sellers:
            for seller in sellers:
                st.write(f"**ID:** {seller['id']}, **Name:** {seller['name']}, **Contact:** {seller['contact_details']}, **Address:** {seller['address']}")
        else:
            st.write("🚫 No sellers found.")

    elif choice == "Update Seller":
        st.subheader("Update Seller")
        seller_id = st.number_input("Enter Seller ID", min_value=1, step=1)
        seller = get_seller(seller_id)

        if seller:
            name = st.text_input("New Name", value=seller['name'])
            contact_details = st.text_input("New Contact Details", value=seller['contact_details'])
            address = st.text_input("New Address", value=seller['address'])

            if st.button("Update"):
                result = update_seller(seller_id, name, contact_details, address)
                if result.status_code == 200:
                    st.success("✅ Seller updated successfully!")
                else:
                    st.error("❌ Error updating seller: " + result.json().get('detail', 'Unknown error'))
        else:
            st.error("🚫 Seller not found.")
    
    elif choice == "Delete Seller":
        # Logic for deleting a seller
        st.subheader("Delete Seller")
        seller_id = st.number_input("Enter Seller ID to delete", min_value=1, step=1)

        if st.button("Delete"):
            result = delete_seller(seller_id)
            if result.status_code == 200:
                st.success("✅ Seller deleted successfully!")
            else:
                st.error("❌ Error deleting seller: " + result.json().get('detail', 'Unknown error'))

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