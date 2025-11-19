from datetime import datetime, timedelta

import pytz
from bs4 import BeautifulSoup

from .models import OperationDate

diff = {
    "sunday": 13.5,
    "monday": 15,
    "tuesday": 15,
    "wednesday": 15,
    "thursday": 15,
    "friday": 16,
    "saturday": 16,
}


def operational_start():
    today = datetime.now(pytz.utc).astimezone(pytz.timezone("US/Eastern"))
    print("today day", today.strftime("%A"))
    minute = 0
    if today.strftime("%A") == "Sunday":
        minute = 30
    today_open = datetime(today.year, today.month, today.day, hour=10, minute=minute)
    print("Today open", today_open)
    today_open = today_open.astimezone(pytz.timezone("US/Eastern"))
    print("Today open after timezone aware", today_open)
    return today_open


def kitchen_ticket_number():
    if not OperationDate.objects.first():

        OperationDate.objects.create(date=operational_start(), counter=1600)
    # the last date saved
    prev_op_date = OperationDate.objects.first()
    prev_date = prev_op_date.date
    # timezone aware now
    now_utc = datetime.now(pytz.utc)
    eastern = pytz.timezone("US/Eastern")
    now_date = now_utc.astimezone(eastern)
    prev_date = prev_date.astimezone(eastern)
    now_day = datetime.now().strftime("%A")
    print(now_date, prev_date, diff[now_day.lower()], now_date - prev_date)
    if now_date - prev_date <= timedelta(hours=diff[now_day.lower()]):
        print("Today")
        prev_op_date.counter += 1
        prev_op_date.save()
        return prev_op_date.counter
    else:
        print("Set new day")
        OperationDate.objects.first().delete()
        OperationDate.objects.create(date=operational_start(), counter=1600)
        return 1600


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
        "address": address if address != None else "",
        "time": formatted_time,
        "status": "pending",
        "blocked": False,
        # TODO: Re-enable kitchen ticket number after fixing overflow issue
        # "kitchen_number": kitchen_ticket_number(),  # Temporarily disabled due to integer overflow
        "kitchen_number": 1,  # Temporary default value
    }
