'use client'
import { useState } from "react"
import Tiles from "../ui/tiles.component"
import { useFetchData } from "../hooks/dataFetch"
import { handler } from "tailwindcss-animate"
import OrderDetail from "../ui/orderDetail.component"
export default function Cfinder() {
    const [datesearch, setDateSearch] = useState(new Date(Date.now() - 86400000).toISOString().split('T')[0])
    const [priceToSearch, setPriceToSearch] = useState('')
    const [selectedOrder, setSelectedOrder] = useState(0)

    const { isLoading, isError, isSuccess, data, error } = useFetchData<ResponseApi>(datesearch, `/api/order/date/${datesearch}`, {})

    const handlePrice = (event: React.ChangeEvent<HTMLInputElement>) => {
        setPriceToSearch(event.target.value)
    }

    const handleDate = (event: React.ChangeEvent<HTMLInputElement>) => {
        setDateSearch(event.target.value)
    }
    const handleSelectedOrder = (order_number: number) => {
        setSelectedOrder(order_number)
    }

    if (isLoading) {
        return <p>Loading orders...</p>
    }
    if (isError) {
        return <p>Error: {(error as Error).message}</p>
    }
    if (isSuccess) {
        const orders: Blocktile[] = data.payload
        const filtered_orders: Blocktile[] = orders.filter((item) => {
            if (priceToSearch.length > 0) {
                return item["total"].startsWith(priceToSearch)
            } else {
                return true
            }
        })
        return (
            (selectedOrder > 0) ? (
                <div>

                    <OrderDetail order_number={selectedOrder.toString()} onBack={() => handleSelectedOrder(0)} />
                </div>
            ) : (
                < div className="text-black"  >
                    <input type="date" name="date" onChange={handleDate} id="date" value={datesearch} />

                    <div>
                        <input type="text" placeholder="Price" value={priceToSearch} onChange={handlePrice} />
                        <div>
                            {filtered_orders.map((item: Blocktile) => {
                                return <Tiles onClick={() => handleSelectedOrder(item["order_number"])} key={item["order_number"]} order_number={item["order_number"]} customer_name={item["customer_name"]} total={item["total"]} />
                            })}
                        </div>
                    </div>
                </ div>
            )

        )
    }
    return "Error"
}
