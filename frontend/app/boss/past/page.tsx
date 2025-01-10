'use client'
import { useFetchData } from "@/components/hooks/dataFetch"
import Order from "@/components/ui/order.component"
import OrderDetail from "@/components/ui/orderDetail.component"
import { useState } from "react"
export default function PastOrders() {



    const { isLoading, isSuccess, isError, data } = useFetchData<OrderProps[]>('orders', "api/orders")

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
        data.sort((a, b) => {
            const dateObject1 = new Date(a.date + ' ' + a.time)
            const dateObject2 = new Date(b.date + ' ' + b.time)
            return dateObject2.getTime() - dateObject1.getTime()
        })

        return (
            <div className="container mx-auto p-4">
                {selectedOrder === null ? (
                    <div className='' >

                        <div className=" p-10">
                            <div className="text-center text-3xl mb-10">PAST ORDERS</div>
                            <div className="flex h-screen flex-col">

                                {data.map((order: OrderProps) => (
                                    <Order key={order.email_id} order={order} changeClick={handleSelectedOrder} >
                                    </Order>
                                ))}
                            </div>
                        </div>
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