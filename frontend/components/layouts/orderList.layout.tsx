import Order from "../ui/order.component"
async function getOrders() {
    const response = await fetch("http://localhost:8000/api/orders");
    const orders = await response.json();
    return orders;
}

export default async function OrderList() {
    const orders = await getOrders();
    console.log(orders);
    return (
        <div>
            <div className="text-center text-3xl">Order List</div>
            <div className="flex h-screen flex-row flex-wrap justify-around content-around">

                {orders.map((order: any) => (
                    <Order key={order.email_id} orderId={order.order_number} name={order.customer_name} />
                ))}
            </div>
        </div>
    );
}