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

# Functions for Sale Management
def create_sale(data):
    response = requests.post(f"{API_URL}/sales", json=data)
    return response.json()

def get_sales():
    response = requests.get(f"{API_URL}/sales")
    return response.json()

def get_sale_by_id(sale_id):
    response = requests.get(f"{API_URL}/sales/{sale_id}")
    return response.json()

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

elif selected_category == "Sales Management":
    st.subheader("Sales Management")
    endpoint = st.selectbox("Options", options=["Record New Sale", "Get All Sales", "Get Sale by ID"])

    # Record a new sale
    if endpoint == "Record New Sale":
        st.header("Record a New Sale")
        with st.form("sale_form"):
            car_id = st.text_input("Car ID", placeholder="Enter Car ID")
            seller_id = st.text_input("Seller ID", placeholder="Enter Seller ID")
            buyer_id = st.text_input("Buyer ID", placeholder="Enter Buyer ID")
            sale_date = st.date_input("Sale Date")
            price = st.number_input("Price", min_value=0.0, format="%.2f", placeholder="Enter Sale Price")
            submitted = st.form_submit_button("Submit Sale")
            
            if submitted:
                sale_data = {
                    "car_id": car_id,
                    "seller_id": seller_id,
                    "buyer_id": buyer_id,
                    "sale_date": sale_date.isoformat(),  # Convert to ISO format for API
                    "price": price,
                }
                result = create_sale(sale_data)
                st.success("Successfully added sale: {}".format(result))

    # Retrieve all sales
    elif endpoint == "Get All Sales":
        st.header("All Sales Records")
        if st.button("Get All Sales"):
            sales = get_sales()
            if sales:
                st.write(sales)
            else:
                st.error("No sales records found.")

    # Retrieve a sale by ID
    elif endpoint == "Get Sale by ID":
        st.header("Get Sale by ID")
        sale_id = st.text_input("Enter Sale ID", placeholder="Sale ID")
        if st.button("Get Sale"):
            if sale_id:
                sale = get_sale_by_id(sale_id)
                if sale:
                    st.write(sale)
                else:
                    st.error("Sale not found.")

# Exit button
if st.button("Exit"):
    st.write("👋 Thank you for using the E-Commerce System!")
