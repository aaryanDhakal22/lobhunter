import { useEffect } from "react";
import Order from "../ui/order.component";
import { connectWebSocket, sendMessage } from "../hooks/websocket";

interface OrderListProps {
    orders: OrderProps[];
    onSelectOrder: (id: string) => void;
};


const OrderList: React.FC<OrderListProps> = ({ orders, onSelectOrder }) => {
    useEffect(() => {
        const socket = connectWebSocket((kitchenTicket: KitchenTicket) => {
            return
        })
        return () => {
            if (socket) socket?.close
        }
    }, [])

    const handleAccept = (order_number: string) => {
        sendMessage(order_number)
    }



    const filtered_orders = orders.filter((item) => {
        return item.status == "pending" && item.payment == "Card";
    });
    filtered_orders.sort((a, b) => {
        const dateObject1 = new Date(a.date + ' ' + a.time)
        const dateObject2 = new Date(b.date + ' ' + b.time)
        return dateObject2.getTime() - dateObject1.getTime()
    })
    return (
        <div className=" p-10">
            <div className="text-center text-3xl mb-10">ORDERS</div>
            <div className="flex h-screen flex-col">

                {filtered_orders.map((order: any) => (
                    <Order key={order.email_id} acceptHandler={handleAccept} blocked={order.blocked} order_number={order.order_number} address={order.address} customer_name={order.customer_name} changeClick={onSelectOrder} />
                ))}
            </div>
        </div>
    );
}

export default OrderList;