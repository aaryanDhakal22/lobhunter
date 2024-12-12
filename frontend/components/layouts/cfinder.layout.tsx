'use client'
import { useQuery } from "@tanstack/react-query"
import { useState } from "react"

export default function Cfinder() {
    const [datesearch, setDateSearch] = useState(new Date().toISOString().split('T')[0])

    const query = useQuery({
        queryKey: ["cfinder", datesearch],
        queryFn: () =>
            fetch(`http://10.1.10.38:8000/api/order/date/${datesearch}`, { method: "GET" })
                .then(res => res.json())
    })

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
        const orders = query.data["payload"]
        console.log(orders)
        return (
            <div className="text-black">
                <input type="date" name="date" onChange={handleDate} id="date" value={datesearch} />

                <div>
                    <input type="text" placeholder="Price" />
                    <div>
                        {orders.map((order: any) => (
                            <div key={order["email_id"]}>Hello</div>))}
                    </div>
                </div>
            </div>
        )
    }
    return "Error"
}
