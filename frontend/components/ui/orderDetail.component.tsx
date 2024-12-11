// components/OrderDetail.tsx
import React from 'react';

type OrderDetailProps = {
  order_number: string;
  onBack: () => void;
};

const OrderDetail: React.FC<OrderDetailProps> = ({ order_number, onBack }) => {
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
    </div>
  );
};

export default OrderDetail;
