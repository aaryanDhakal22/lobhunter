'use client'
import React, { useState, useEffect } from 'react';
import OrderList from './orderList.layout';
import OrderDetail from '../ui/orderDetail.component';
import { useFetchData } from '../hooks/dataFetch';

const OrdersPage: React.FC = () => {

    const { isLoading, isSuccess, isError, data } = useFetchData<OrderProps[]>('orders', "/api/orders")

    const [selectedOrder, setSelectedOrder] = useState<string | null>(null);

    const handleSelectedOrder = (id: string) => {
        setSelectedOrder(id);
    }

    if (isLoading) {
        return <div>Loading...</div>
    }
    if (isError) {
        return <div>Error Detected</div>
    }
    if (isSuccess) {


        return (
            <div className="container mx-auto p-4">
                {selectedOrder === null ? (
                    <div className='transition-transform duration-500 ease-in-out transform scale-100' key="order-list">

                        <OrderList
                            orders={data}
                            onSelectOrder={handleSelectedOrder}
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
    }
};

export default OrdersPage;
