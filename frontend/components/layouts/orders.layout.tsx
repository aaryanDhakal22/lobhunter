'use client'
import React, { useState, useEffect } from 'react';
import OrderList from './orderList.layout';
import OrderDetail from '../ui/orderDetail.component';


const OrdersPage: React.FC = () => {
    const [orders, setOrders] = useState<OrderProps[]>([]);
    const [selectedOrder, setSelectedOrder] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    // Fetch orders from the API
    useEffect(() => {
        const fetchOrders = async () => {
            try {
                const response = await fetch('http://10.1.10.38:8000/api/orders');
                if (!response.ok) {
                    throw new Error('Failed to fetch orders');
                }
                const data: OrderProps[] = await response.json();
                setOrders(data);
            } catch (err) {
                setError((err as Error).message);
            } finally {
                setLoading(false);
            }
        };

        fetchOrders();
    }, []);

    if (loading) {
        return (
            <div className="container mx-auto p-4">
                <p>Loading orders...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="container mx-auto p-4">
                <p className="text-red-500">Error: {error}</p>
            </div>
        );
    }

    return (
        <div className="container mx-auto p-4">
            {selectedOrder === null ? (
                <div className='transition-transform duration-500 ease-in-out transform scale-100' key="order-list">

                    <OrderList
                        orders={orders}
                        onSelectOrder={(id: string) => setSelectedOrder(id)}
                    />
                </div>
            ) : (
                <div className="transition-transform duration-500 ease-in-out transform scale-100 p-5"
                    key="order-detail ">

                    <div className="text-center text-3xl mb-10">ORDERS</div>
                    <div className='p-2'>

                        <OrderDetail
                            order_number={selectedOrder}
                            onBack={() => setSelectedOrder(null)}
                        />
                    </div>
                </div>
            )}
        </div>
    );
};

export default OrdersPage;
