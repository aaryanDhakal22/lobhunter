from bs4 import BeautifulSoup

from datetime import datetime

def parser(html_content):
    
    soup = BeautifulSoup(html_content, "html.parser")

    def safe_find_and_split(search_text, split_delimiter):
        """Find text safely and split it; return None if not found."""
        result = soup.find(text=lambda t: t and search_text in t)
        return result.split(split_delimiter)[-1].strip() if result else None

    total_element = soup.find(text="Order Total:")
    order_total = total_element.find_next("b").text.strip() if total_element else None
    order_total = float(order_total.replace("$", "")) if order_total else None

    # Extract and format the date
    date_text = safe_find_and_split("Placed On:", "Placed On: ")
    try:
        date_object = datetime.strptime(date_text, "%a, %b %d %Y @ %I:%M %p")
        formatted_date = date_object.strftime("%Y-%m-%d")
    except ValueError:
        formatted_date = None  # Fallback in case the format doesn't match


    # Extract and format the time
    time_text = safe_find_and_split("Placed On:", " @ ")
    try:
        time_object = datetime.strptime(time_text, "%I:%M %p")
        formatted_time = time_object.strftime("%H:%M:%S")
    except ValueError:
        formatted_time = None


    # Check if topic mentions delivery
    topic = soup.find("h1")
    address = None
    if topic and topic.get_text() and "delivery" in topic.get_text().lower():
        # Extract address details
        street = soup.find(["font", "b"], string=lambda s: s and "Street" in s)
        if street:
            street_text = street.get_text(strip=True).replace("Street:", "").strip()
            address = f"{street_text}"
            address = address.split(",")[0]


    # Extract details
    order_number = safe_find_and_split("Order#", "#")
    customer_name = safe_find_and_split("Customer Name:", ": ")
    phone_number = safe_find_and_split("Phone:", ": ")
    if phone_number:
        phone_number = phone_number.replace("-", "").replace("-", "")
    payment_type = safe_find_and_split("Payment Type:", "Payment Type: ")

    # Adjust payment type
    if payment_type == "Pay with Cash":
        payment_type = "Cash"
    elif payment_type is None:
        payment_type = "Card"

    # Return the extracted details
    return {
        "order_number": order_number,
        "customer_name": customer_name,
        "date": formatted_date,
        "phone": phone_number,
        "total": order_total,
        "payment": payment_type,
        "ticket": html_content,
        "address": address,
        "time": formatted_time,
    }
