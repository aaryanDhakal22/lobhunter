
import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { useFetchData } from '../hooks/dataFetch';
type OrderDetailProps = {
  order_number: string;
  onBack: () => void;
};


const OrderDetail: React.FC<OrderDetailProps> = ({ order_number, onBack }) => {
  // const order = useQuery({ queryKey: ['order_detail'], queryFn: () => fetch(`http://10.1.10.38:8000/api/order/detail/${order_number}`, { method: 'GET' }).then((res) => res.json()) });
  const { isLoading, isError, error, data, isSuccess } = useFetchData<OrderProps>('orderDetail', `api/order/detail/${order_number}`, {})


  if (isLoading) {
    return <p>Loading ..</p>;
  }
  if (isError) {
    return <p>Error: {(error as Error).message}</p>;
  }
  if (isSuccess) {

    return (
      <div>
        <button onClick={onBack} className="bg-green-500 px-5 py-3 rounded-lg mb-3 "> &lt;&nbsp;&nbsp;&nbsp;&nbsp;Back</button>
        <p className='bg-white text-black p-6 rounded-md' dangerouslySetInnerHTML={{ __html: data["ticket"] }}></p>

      </div>

    );
  }
};

export default OrderDetail;