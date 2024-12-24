from django.test import TestCase, Client
from .models import Order, PhoneBlockList, AddressBlockList
from datetime import date
from unittest.mock import patch


class OrderModelTest(TestCase):
    def setUp(self):
        # Setting up initial test data
        self.order_data = {
            "email_id": "aha7h92h972",
            "order_number": 1,
            "customer_name": "John Doe",
            "date": "2024-12-08",
            "phone": 1234567890,
            "total": "100.50",
            "payment": "Paid",
            "ticket": "Some ticket information",
            "address": "123 Test Street",
            "time": "14:30:00",
        }

    def test_add_order(self):
        # Test adding an order
        order = Order.objects.create(**self.order_data)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(order.email_id, "aha7h92h972")
        self.assertEqual(order.order_number, 1)

    def test_delete_order(self):
        # Test deleting an order
        order = Order.objects.create(**self.order_data)
        order.delete()
        self.assertEqual(Order.objects.count(), 0)


class NinjaAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.order_data = {
            "email_id": "test@example.com",
            "order_number": 1,
            "customer_name": "John Doe",
            "date": "2024-12-08",
            "phone": 1234567890,
            "total": 100.50,
            "payment": "Paid",
            "ticket": "Some ticket information",
            "address": "123 Test Street",
            "time": "14:30:00",
        }
        self.blocked_phone = 4437208747
        self.blocked_address = "1625 E NORTHERN PARKWAY"
        # Add phone and address to blocklists
        PhoneBlockList.objects.create(phone=self.blocked_phone, reason="Spam")
        AddressBlockList.objects.create(
            address=self.blocked_address, reason="Fraudulent"
        )

    def mock_fetcher():
        return [
            {
                "email_id": "193a4a6cf401a487",
                "data": "<html>\r\n<head><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\r\n</head>\r\n<body>\r\n<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\">\r\n<tr align='center' valign='top'><td colspan='4'><h1>Online Order (Delivery)</h1></td></tr>\r\n<tr align='center' valign='bottom'><td colspan='4'><b><font size='+1'>LOMBARDI’S PIZZA</font></b></td></tr>\r\n<tr><td colspan='2'><b>Order#56182206</b></td>\r\n<td align='right' colspan='2'><b>Placed On: Sun, Dec 8 2024 @ 12:02 AM</b></td>\r\n</tr>\r\n<tr><td colspan='4'><b>Customer Name: BLAKE, ANTHONY</b></td></tr>\r\n<tr><td colspan='4'><font size='+1'><b>Phone: 410-736-3846</b></font></td></tr>\r\n<tr><td colspan='4'><b>Email: ANTHONYBLAKE2013@GMAIL.COM</b></td></tr>\r\n<tr><td colspan='4'><font size='+1'><b>Street: 1625 E NORTHERN PARKWAY</b></font></td></tr>\r\n<tr><td colspan='4'><b>Cross Street: 1625 E NORTHERN PARKWAY</b></td></tr>\r\n<tr><td colspan='4'><font size='+1'><b>City/State:</b> BALTIMORE, MD  21239</font></td>\r\n</tr>\r\n<tr><td colspan='4'><hr></td></tr>\r\n<tr align='center'><td colspan='4'><b>PAYMENTS</b></td></tr>\r\n<tr><td colspan='4'>Pay Now (Credit Card): xxxxxxxxxxxxx068</td></tr>\r\n<tr><td colspan='4'>Auth# 013620</td></tr>\r\n<tr><td colspan='4'>Amount: $29.03</td></tr>\r\n<tr><td colspan='4'>***PAID ONLINE***</td></tr>\r\n<tr><td colspan='4'>&nbsp;</td></tr>\r\n<tr><td colspan='4'><b>Balance Owing:</b> $0.00</td></tr>\r\n<tr><td colspan='4'><table border='0' cellpadding='0' cellspacing='0' width='100%'>\r\n<tr align='center'><td colspan='5'><hr></td></tr>\r\n<tr><td width='5%'><b>Qty</b></td><td width='12%'></td><td width='5%' nowrap align='right'>&nbsp;</td><td width='63%' align='left'><b>Item</b>\t</td><td width='15%' align='right'><b>Price</b>\t</td></tr>\r\n<tr><td colspan='5'><table border='1' cellpadding='2' cellspacing='2' width='100%' bgcolor='#CCCCCC'><tr><td><table border='0' cellpadding='0' cellspacing='0' width='100%' bgcolor='#FFFFFF'><tr valign='middle'><td width='5%'  valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='12%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='5%'  valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='63%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td><td width='15%' valign='top' height='1'><img src='/zgrid/images/spacer.gif' width='1' height='1'></td></tr><tr valign='top'><td colspan='5' height='19' align='center'><b>8'' Sub Special</b></td></tr><tr align='center'><td colspan='5'><hr></td></tr>\r\n<tr><td>1</td><td></td><td>&nbsp;</td><td>8'' Sub\t<br>Size: Serving</td><td align='right'>$12.99\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Shrimp Chicken Cheesesteak Sub&nbsp;</td><td align='right'>$1.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>With Provolone Cheese&nbsp;</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Tomatoes&nbsp;</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Fried Onions&nbsp;</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Mayo&nbsp;</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Extra Meat&nbsp;</td><td align='right'>$2.49\t</td></tr>\r\n<tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$16.48</i></td></tr>\r\n<tr align='center'><td colspan='5'><hr></td></tr>\r\n<tr><td>1</td><td></td><td>&nbsp;</td><td>Small - French Fries\t<br>Size: Serving</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Add Honey BBQ Sauce&nbsp;</td><td align='right'>$0.75\t</td></tr>\r\n<tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$0.75</i></td></tr>\r\n<tr align='center'><td colspan='5'><hr></td></tr>\r\n<tr><td>1</td><td></td><td>&nbsp;</td><td>12 oz  - Can Soda\t<br>Size: Serving</td><td align='right'>$0.00\t</td></tr>\r\n<tr>\r\n<td>&nbsp;</td><td>&nbsp;</td><td align='right' nowrap>&nbsp;</td><td align='left'>Orange Soda&nbsp;</td><td align='right'>$0.00\t</td></tr>\r\n<tr><td colspan='4' align='right'>Sum:&nbsp;</td><td align='right'><i>$0.00</i></td></tr>\r\n</table></td></tr></table></td></tr><tr align='center'><td colspan='5'><hr></td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Delivery Charge:&nbsp;</td><td align='right'>$4.00</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Service Charge:&nbsp;</td><td align='right'>$0.50</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Subtotal:&nbsp;</td><td align='right'>$21.73</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Sales Tax (6.0%):&nbsp;</td><td align='right'>$1.30</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Total:<b>&nbsp;</b></td><td align='right'>$23.03</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'>Gratuity:<b>&nbsp;</b></td><td align='right'>$6.00</td></tr>\r\n<tr><td>&nbsp;</td><td colspan='3' align='right'><b>Order Total:</b>&nbsp;</td><td align='right'><b>$29.03</b></td></tr>\r\n</table></td></tr>\r\n<tr align='center'><td colspan='4'><b>LOMBARDIS-PIZZA.COM (P: 410-321-9288, F: 443-841-7170)</b><br><b>Please call 866-4-BRYGID if you have any questions about this service.</b><br><font size='-1'><i><b>Powered by BRYGID (www.brygid.com)</b></i></font></td></tr>\r\n</table>\r\n<!--\r\nForm Code: Z-1\r\nIP: 73.213.250.21\r\nAgent: Mozilla/5.0 (iPhone; CPU iPhone OS 18_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/131.0.6778.103 Mobile/15E148 Safari/604.1\r\nRecalled From Order: \r\nOrder Date: 12/08/2024 00:02\r\nOrder For Date:\r\n-->\r\n</body></html>\r\n",
            }
        ]

    # # @patch("lobhunter.api.fetcher", side_effect=mock_fetcher)
    # def test_sync_creates_order_and_no_blocks(self):
    #     response = self.client.get("/api/sync", {"fetcher": self.mock_fetcher})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Order.objects.count(), 1)
    #     self.assertEqual(Order.objects.first().email_id, "193a4a6cf401a487")
    #     self.assertEqual(response.json()["blocked"], 0)

    # @patch("lobhunter.api.fetcher", side_effect=mock_fetcher)
    # def test_sync_blocks_order_with_phone(self,mock_fetcher):
    #     response = self.client.get("/api/sync")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Order.objects.count(), 1)  # Order is still created with status BLOCKED
    #     self.assertEqual(Order.objects.first().status, "BLOCKED")
    #     self.assertEqual(response.json()["blocked"], 1)

    # @patch("lobhunter.api.default_fetcher", side_effect=mock_fetcher)
    # def test_sync_blocks_order_with_address(self,mock_fetcher):
    #     response = self.client.get("/api/sync")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(Order.objects.count(), 1)  # Order is still created with status BLOCKED
    #     self.assertEqual(Order.objects.first().status, "BLOCKED")
    #     self.assertEqual(response.json()["blocked"], 1)

    def test_get_all_orders(self):
        Order.objects.create(**self.order_data)
        response = self.client.get("/api/orders")
        self.assertEqual(response.status_code, 200)
        orders = response.json()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["email_id"], "test@example.com")

    def test_get_order_by_id(self):
        Order.objects.create(**self.order_data)
        response = self.client.get(
            f"/api/order/detail/{self.order_data['order_number']}"
        )
        self.assertEqual(response.status_code, 200)
        order = response.json()
        self.assertEqual(len(order), 1)
        self.assertEqual(order[0]["email_id"], "test@example.com")

    def test_get_orders_by_date(self):
        Order.objects.create(**self.order_data)
        response = self.client.get(f"/api/order/date/{self.order_data['date']}")
        self.assertEqual(response.status_code, 200)
        orders = response.json()
        self.assertEqual(len(orders), 1)
        self.assertEqual(orders[0]["email_id"], "test@example.com")
