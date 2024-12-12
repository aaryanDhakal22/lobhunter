
import React from 'react';
import { useQuery } from '@tanstack/react-query';
type OrderDetailProps = {
  order_number: string;
  onBack: () => void;
};


const OrderDetail: React.FC<OrderDetailProps> = ({ order_number, onBack }) => {
  const order = useQuery({ queryKey: ['order_detail'], queryFn: () => fetch(`http://10.1.10.38:8000/api/order/detail/${order_number}`, { method: 'GET' }).then((res) => res.json()) });
  if (order.isLoading) {
    return <p>Loading order...</p>;
  }
  if (order.isError) {
    return <p>Error: {(order.error as Error).message}</p>;
  }
  console.log(order.data);
  console.log(order.data["ticket"]);
  return (
    <div>
      <button onClick={onBack} className="bg-green-500 px-5 py-3 rounded-lg mb-3 "> &lt;&nbsp;&nbsp;&nbsp;&nbsp;Back</button>
      <p className='bg-white text-black p-6 rounded-md' dangerouslySetInnerHTML={{ __html: order.data["ticket"] }}></p>

    </div>

  );
};

export default OrderDetail;