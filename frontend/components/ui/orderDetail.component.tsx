
// components/OrderDetail.tsx

import React from 'react';

type OrderDetailProps = {
  order_number: string;
  onBack: () => void;
};

async function fetchOrderDetail(order_number: string) {
  try {
    // console.log(`http://10.0.0.167:8000/api/orders/detail/${order_number}`)
    const response = await fetch(`http://10.0.0.167:8000/api/order/detail/${order_number}`);
    if (!response.ok) {
      throw new Error('Failed to fetch order detail');
    }
    const data = await response.json();
    return data;
  } catch (err) {
    throw err;
  }
}

const OrderDetail: React.FC<OrderDetailProps> = ({ order_number, onBack }) => {
  // export default async function OrderDetail({ order_number, onBack }) => {
  const order_detail = fetchOrderDetail(order_number);
  return (
    <div className="p-4 border rounded-md">
      <button
        onClick={onBack}
        className="mb-4 px-4 py-2 text-sm text-white bg-blue-500 rounded-md hover:bg-blue-600"
      >
        Back to Orders
      </button>
      <h2 className="text-lg font-semibold">Order Detail</h2>
      <p className="mt-2">Details for order : {order_number}</p>
      <div>
        {order_detail}
      </div>
    </div>
  );
};

export default OrderDetail;