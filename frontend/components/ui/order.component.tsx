import updateStatus from "../hooks/updateStatus"

interface OrderViewProps {
    order_number: string;
    address: string;
    customer_name: string;
    changeClick: (id: string) => void;
}

const Order: React.FC<OrderViewProps> = ({ order_number, address, customer_name, changeClick }) => {

    const handleClick = (status: string) => {
        const response = updateStatus(order_number, status)
    }
    return (

        <div className="p-3 m-2 rounded-lg outline outline-2 outline-green-600 grid grid-cols-3 ">

            <div onClick={() => changeClick(order_number)} className="cursor-pointer">

                <div className="text-xl text-green-500">Order No : {order_number}</div>
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