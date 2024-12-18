from django.test import TestCase, Client
from .models import Order, PhoneBlockList, AddressBlockList


# class SyncUpTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.blocked_phone = 9876543210
#         self.blocked_address = "Blocked Address"
#         self.test_data = {
#             "email_id": "test@example.com",
#             "order_number": 1,
#             "customer_name": "John Doe",
#             "date": "2024-12-08",
#             "phone": 1234567890,
#             "total": 100.50,
#             "payment": "Paid",
#             "ticket": "Some ticket information",
#             "address": "123 Test Street",
#             "time": "14:30:00",
#         }
#         self.raw_order_data = [
#             """<html>
# <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
# </head>
# <body>
# <table border="0" cellpadding="0" cellspacing="0" width="100%">
# <tr align='center' valign='top'><td colspan='4'><h1>Online Order (Delivery)</h1></td></tr>
# <tr align='center' valign='bottom'><td colspan='4'><b><font size='+1'>LOMBARDI’S PIZZA</font></b></td></tr>
# <tr><td colspan='2'><b>Order#56181176</b></td>
# <td align='right' colspan='2'><b>Placed On: Sat, Dec 7 2024 @ 9:58 PM</b></td>
# </tr>
# <tr><td colspan='4'><b>Customer Name: PAGE, DONTE</b></td></tr>
# <tr><td colspan='4'><font size='+1'><b>Phone: 410-925-8932</b></font></td></tr>
# <tr><td colspan='4'><b>Email: DONTEPAGE2019@GMAIL.COM</b></td></tr>
# <tr><td colspan='4'><font size='+1'><b>Street: 7820 HILLSWAY AVE.</b></font></td></tr>
# <tr><td colspan='4'><font size='+1'><b>City/State:</b> PARKVILLE, MD  21234</font></td>
# </tr>
# <tr><td colspan='4'><hr></td></tr>
# <tr align='center'><td colspan='4'><b>PAYMENTS</b></td></tr>
# <tr><td colspan='3'><b>Payment Type: Pay with Cash</b></td><td>&nbsp;</td></tr>
# <tr><td colspan='4'>&nbsp;</td></tr>
# <tr><td colspan='4'><b>Balance Owing:</b> $66.75</td></tr>
# <tr><td colspan='4'><table border='0' cellpadding='0' cellspacing='0' width='100%'>
# <tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td width='5%'><b>Qty</b></td><td width='12%'></td><td width='5%' nowrap align='right'>&nbsp;</td><td width='63%' align='left'><b>Item</b>  </td><td width='15%' align='right'><b>Price</b>     </td></tr>
# <tr><td colspan='5'><table border='1' cellpadding='2' cellspacing='2' width='100%' bgcolor='#CCCCCC'><tr><td><table border='0' cellpadding='0' cellspacing='0' width='100%' bgcolor='#FFFFFF'><tr valign='middle'><td width='5%'  valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='12%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='5%'  valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='63%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='15%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td></tr><tr valign='top'><td colspan='5' height='19' align='center'><b>Two Large Pizza Special</b></td></tr><tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>1</td><td></td><td>&nbsp;</td><td>(1st) 14'' Large - Regular Tomato & Cheese    <br>Size: Serving</td><td align='right'>$23.99  </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Pepperoni&nbsp;</td><td align='right'>$0.00      </td></tr>
# <tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$23.99</i></td></tr>
# <tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>1</td><td></td><td>&nbsp;</td><td>(2nd) 14'' Large - Regular Tomato & Cheese    <br>Size: Serving</td><td align='right'>$0.00   </td></tr>
# <tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$0.00</i></td></tr>
# </table></td></tr></table></td></tr><tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>1</td><td></td><td>&nbsp;</td><td>Whole Wings Only      <br>Size: 10 Piece</td><td align='right'>$18.99 </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Mild Flavor&nbsp;</td><td align='right'>$1.00        </td></tr>
# <tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$19.99</i></td></tr>
# <tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>1</td><td></td><td>&nbsp;</td><td>Jumbo Party Wings     <br>Size: Serving</td><td align='right'>$0.00   </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Breaded&nbsp;</td><td align='right'>$0.00    </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>6 Piece&nbsp;</td><td align='right'>$7.99    </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Southern-Style  Flavor&nbsp;</td><td align='right'>$0.00     </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Ranch Dip&nbsp;</td><td align='right'>$0.00  </td></tr>
# <tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$7.99</i></td></tr>
# <tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>2</td><td></td><td>&nbsp;</td><td>2 Liter Soda  <br>Size: Serving</td><td align='right'>$3.25   </td></tr>
# <tr>
# <td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Ginger Ale&nbsp;</td><td align='right'>$0.00 </td></tr>
# <tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$6.50</i></td></tr>
# <tr align='center'><td colspan='5'><hr></td></tr>
# <tr><td>&nbsp;</td><td colspan='3' align='right'>Delivery Charge:&nbsp;</td><td align='right'>$4.00</td></tr>
# <tr><td>&nbsp;</td><td colspan='3' align='right'>Service Charge:&nbsp;</td><td align='right'>$0.50</td></tr>
# <tr><td>&nbsp;</td><td colspan='3' align='right'>Subtotal:&nbsp;</td><td align='right'>$62.97</td></tr>
# <tr><td>&nbsp;</td><td colspan='3' align='right'>Sales Tax (6.0%):&nbsp;</td><td align='right'>$3.78</td></tr>
# <tr><td>&nbsp;</td><td colspan='3' align='right'><b>Order Total:</b>&nbsp;</td><td align='right'><b>$66.75</b></td></tr>
# </table></td></tr>
# <tr align='center'><td colspan='4'><b>LOMBARDIS-PIZZA.COM (P: 410-321-9288, F: 443-841-7170)</b><br><b>Please call 866-4-BRYGID if you have any questions about this service.</b><br><font size='-1'><i><b>Powered by BRYGID (www.brygid.com)</b></i></font></td></tr>
# </table>
# <!--
# Form Code: Z-1
# IP: 173.64.116.68
# Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1
# Recalled From Order:
# Order Date: 12/07/2024 21:58
# Order For Date:
# -->
# </body></html>
#                 """
#         ]
#         # Setup blocklist data
#         PhoneBlockList.objects.create(phone=self.blocked_phone, reason="Spam")
#         AddressBlockList.objects.create(phone=1234567890, reason="Fraudulent")

#     def mock_fetcher(self):
#         return [{"email_id": "183739374", "data": self.raw_order_data}]

#     def test_sync_creates_order(self):
#         response = self.client.get("/api/sync", fetcher=self.mock_fetcher)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(Order.objects.count(), 1)
#         self.assertEqual(Order.objects.first().email_id, "test@example.com")


# from django.test import TestCase, Client
# from .models import Order, PhoneBlockList, AddressBlockList
# from datetime import date


# class NinjaAPITestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         # Sample data
#         self.order_data = {
#             "email_id": "test@example.com",
#             "order_number": 1,
#             "customer_name": "John Doe",
#             "date": "2024-12-08",
#             "phone": 1234567890,
#             "total": 100.50,
#             "payment": "Paid",
#             "ticket": "Some ticket information",
#             "address": "123 Test Street",
#             "time": "14:30:00",
#         }
#         self.blocked_phone = 9876543210
#         self.blocked_address = "Blocked Address"
#         # Add phone and address to blocklists
#         PhoneBlockList.objects.create(phone=self.blocked_phone, reason="Spam")
#         AddressBlockList.objects.create(phone=1234567890, reason="Fraudulent")

#     def test_get_all_orders(self):
#         Order.objects.create(**self.order_data)
#         response = self.client.get("/api/orders")
#         self.assertEqual(response.status_code, 200)
#         orders = response.json()
#         self.assertEqual(len(orders), 1)
#         self.assertEqual(orders[0]["email_id"], "test@example.com")

#     def test_get_order_by_id(self):
#         Order.objects.create(**self.order_data)
#         response = self.client.get(f"/api/order/{self.order_data['order_number']}")
#         self.assertEqual(response.status_code, 200)
#         order = response.json()
#         self.assertEqual(len(order), 1)
#         self.assertEqual(order[0]["email_id"], "test@example.com")

#     def test_get_orders_by_date(self):
#         Order.objects.create(**self.order_data)
#         response = self.client.get(f"/api/order/{self.order_data['date']}")
#         self.assertEqual(response.status_code, 200)
#         orders = response.json()
#         self.assertEqual(len(orders), 1)
#         self.assertEqual(orders[0]["email_id"], "test@example.com")


# class OrderModelTest(TestCase):
#     def setUp(self):
#         # Setting up initial test data
#         self.order_data = {
#             "email_id": "test@example.com",
#             "order_number": 1,
#             "customer_name": "John Doe",
#             "date": "2024-12-08",
#             "phone": 1234567890,
#             "total": "100.50",
#             "payment": "Paid",
#             "ticket": "Some ticket information",
#             "address": "123 Test Street",
#             "time": "14:30:00",
#         }

#     def test_add_order(self):
#         # Test adding an order
#         order = Order.objects.create(**self.order_data)
#         self.assertEqual(Order.objects.count(), 1)
#         self.assertEqual(order.email_id, "test@example.com")
#         self.assertEqual(order.order_number, 1)

#     def test_delete_order(self):
#         # Test deleting an order
#         order = Order.objects.create(**self.order_data)
#         order.delete()
#         self.assertEqual(Order.objects.count(), 0)

#     def test_independent_databases(self):
#         # Ensure each test runs on an independent database
#         self.assertEqual(Order.objects.count(), 0)
