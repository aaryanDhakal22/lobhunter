'use client'
import { connectWebSocket, sendMessage } from "@/components/hooks/websocket"
import KitchenOrder from "@/components/ui/kitchenOrder";
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
            <div className="flex gap-5 items-start ">
                {orders.map((item: KitchenOrder) => {
                    return <KitchenOrder key={item.id} item={item} />
                })}
            </div>
        </div>
    )
}

export default OrderList