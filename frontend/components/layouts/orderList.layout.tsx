import Order from "../ui/order.component";

interface OrderListProps {
    orders: OrderProps[];
    onSelectOrder: (id: string) => void;
};

const OrderList: React.FC<OrderListProps> = ({ orders, onSelectOrder }) => {

    return (
        <div className=" p-10">
            <div className="text-center text-3xl mb-10">ORDERS</div>
            <div className="flex h-screen flex-col">

                {orders.map((order: any) => (
                    <Order key={order.email_id} order_number={order.order_number} address={order.address} customer_name={order.customer_name} changeClick={onSelectOrder} />
                ))}
            </div>
        </div>
    );
}

export default OrderList;