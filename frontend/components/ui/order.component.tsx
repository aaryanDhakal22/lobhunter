import { updateStatus } from "../hooks/updateStatus"
import { Mutation, useMutation } from "@tanstack/react-query";
import { use, useState } from "react";
import queryClient from '../ui/queryclientProvider'
interface OrderViewProps {
    order_number: string;
    address: string;
    customer_name: string;
    blocked: string;
    changeClick: (id: string) => void;
}


const Order: React.FC<OrderViewProps> = ({ order_number, blocked, address, customer_name, changeClick }) => {


    const color: 'green' | 'red' = blocked ? 'red' : 'green'

    const mutation = useMutation({
        mutationFn: (status: string) => {
            return updateStatus(order_number, status)
        }
    },)
    const handleClick = (status: string) => {

        const response = mutation.mutate(status)

    }



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
            <div className="grid grid-cols-3 p-4 gap-4">
                <button onClick={() => { handleClick("accepted") }} className="bg-green-500 p-3 rounded-lg">Accept</button>
                <button onClick={() => { handleClick("rejected") }} className="bg-red-500 p-3 rounded-lg">Reject</button>
                <button onClick={() => { handleClick("dismissed") }} className="bg-slate-500 p-3 rounded-lg">Dismiss</button>
            </div>
        </div >
    );
};

export default Order;