
import React from 'react';

interface TilesProps {
    order_number: number;
    customer_name: string;
    total: string;
    onClick: () => void;
}

const Tiles: React.FC<TilesProps> = ({ order_number, customer_name, total, onClick }) => {
    return (
        <div onClick={onClick} className=" cursor-pointer p-3 m-2 rounded-lg outline outline-2 outline-green-600 grid grid-cols-3 ">
            <div className="cursor-pointer">
                <div className="text-xl text-green-500">Order No : {order_number}</div>
            </div>
            <div className="text-xl text-white">
                <div>{customer_name}</div>
            </div>
            <div className="grid grid-cols-3 p-4 gap-4">
                <div className='text-2xl text-white'>{total}</div>
            </div>
        </div>
    );
}

export default Tiles;