'use client'
import { useQuery } from "@tanstack/react-query"
import { useState } from "react"
import Tiles from "../ui/tiles.component"
import { useFetchData } from "../hooks/dataFetch"

export default function Cfinder() {
    const [datesearch, setDateSearch] = useState(new Date(Date.now() - 86400000).toISOString().split('T')[0])
    const [priceToSearch, setPriceToSearch] = useState('')
    // const query = useQuery({
    //     queryKey: ["cfinder", datesearch],
    //     queryFn: () =>
    //         fetch(`http://10.1.10.38:8000/api/order/date/${datesearch}`, { method: "GET" })
    //             .then(res => res.json())
    // })

    const query = useFetchData<OrderProps>(datesearch, `/api/order/date/${datesearch}`, {})
    const handlePrice = (event: React.ChangeEvent<HTMLInputElement>) => {
        setPriceToSearch(event.target.value)
    }

    const handleDate = (event: React.ChangeEvent<HTMLInputElement>) => {
        setDateSearch(event.target.value)
    }

    if (query.isLoading) {
        return <p>Loading orders...</p>
    }
    if (query.isError) {
        return <p>Error: {(query.error as Error).message}</p>
    }
    if (query.isSuccess) {
        console.log(query.data)
        const orders: OrderProps[] = query.data["payload"]
        const filtered_orders: OrderProps[] = orders.filter((item) => {
            if (priceToSearch.length > 0) {
                return item["total"].startsWith(priceToSearch)
            } else {
                return true
            }
        })
        return (
            < div className="text-black" >
                <input type="date" name="date" onChange={handleDate} id="date" value={datesearch} />

                <div>
                    <input type="text" placeholder="Price" value={priceToSearch} onChange={handlePrice} />
                    <div>
                        {filtered_orders.map((item: blocktile) => {
                            return <Tiles key={item["order_number"]} order_number={item["order_number"]} customer_name={item["customer_name"]} total={item["total"]} />
                        })}
                    </div>
                </div>
            </ div>
        )
    }
    return "Error"
}
