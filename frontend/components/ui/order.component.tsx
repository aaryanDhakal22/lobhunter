import Link from "next/link";

interface OrderProps {
    orderId: string;
    name: string;
}

async function getOrders(order_id: string) {
    const response = await fetch(`http://localhost:8000/api/orders/${order_id}`);
    const orders = await response.json();
    return orders;
}

const Order: React.FC<OrderProps> = ({ orderId, name }) => {
    return (
        <Link href={`/orders/${orderId}`}>
            <div className="bg-green-500 p-3">
                <div className="text-center text-2xl">Order No:{orderId}</div>
                <div className="text-center text-xl">{name}</div>

            </div>
        </Link>
    );
};

export default Order;