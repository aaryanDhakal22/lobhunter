'use client'
import { connectWebSocket, sendMessage } from "@/components/hooks/websocket"
import React, { useEffect, useState } from 'react'

interface KitchenOrder extends KitchenTicket {
    id: string;
}


const OrderList: React.FC = () => {
    const [orders, setOrders] = useState<KitchenOrder[]>([]);

    useEffect(() => {
        const socket = connectWebSocket((kitchenTicket) => {
            const newOrder: KitchenOrder = { id: Date.now().toString(), name: kitchenTicket.name, ticket: kitchenTicket.ticket };
            setOrders((prevOrders) => [...prevOrders, newOrder]);
        })
        return () => {
            if (socket) socket?.close
        }
    }, [])

    return (
        <div className="p-4">
            <div className="flex gap-5 ">
                {orders.map((item: KitchenOrder) => {
                    return <div className='bg-white inline text-black p-6 rounded-md' dangerouslySetInnerHTML={{ __html: item.ticket }} key={item.id}></div>
                })}
            </div>
        </div>
    )
}

export default OrderList