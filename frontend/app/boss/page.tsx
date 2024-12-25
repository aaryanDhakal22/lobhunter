import OrderList from "@/components/layouts/orderList.layout"
import OrdersPage from "@/components/layouts/orders.layout"
export default function main() {
    return (
        <div className="flex flex-row ">
            
            <div className="basis-2/3">
                <OrdersPage />
            </div>
            <div className="basis-1/3 ">
                <div className="text-center text-2xl">

                    Controls
                </div>
            </div>
        </div>
    )
}