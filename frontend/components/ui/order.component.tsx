import { updateStatus } from "../hooks/updateStatus"
import { Mutation, useMutation } from "@tanstack/react-query";
import { use, useState } from "react";
import queryClient from '../ui/queryclientProvider'
import StatusButtons from "../layouts/statusButtons.layout";
interface OrderViewProps {
    order_number: string;
    address: string;
    customer_name: string;
    blocked: string;
}


export default function Order({ order, changeClick, children }: { order: OrderViewProps, changeClick: (id: string) => void, children?: any }) {
    const { blocked, order_number, customer_name, address } = { ...order }

    const color: 'green' | 'red' = blocked ? 'red' : 'green'


    return (

        <div className={`p-3 m-2 rounded-lg outline outline-2 ${color == 'green' ? 'outline-green-600' : 'outline-red-600'} grid grid-cols-3 `}>

            <div onClick={() => changeClick(order_number)} className="cursor-pointer">

                <div className={`text-xl ${color == 'green' ? 'text-green-600' : 'text-red-600'}`}>Order No : {order_number}</div>
                <div className="text-3xl">{customer_name}</div>
            </div>
            <div className="text-xl">

                {address ? (
                    <a href={`http://maps.google.com/?q=${address}`} target="blank" rel="noreferrer noopener" >
                        <div>Address:</div>
                        <div>{address}</div>
                    </a>
                ) : (
                    "PICKUP"
                )}

            </div>

            {children}
        </div >
    );
};
