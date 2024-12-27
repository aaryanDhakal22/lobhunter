'use client'
import axios from "axios";
import queryClient from "../ui/queryclientProvider";
export async function updateStatus(orderNumber: string, status: string) {
    const primaryUrl = "10.1.10.38"
    // const primaryUrl = "localhost"
    const payload = {
        "order_number": orderNumber.toString(),
        "status": status
    }
    // console.log(payload)
    const response = await axios.put(`http://${primaryUrl}:8000/api/order/status/`, payload).then(response => {
        // console.log(response.data)
        queryClient.invalidateQueries({ queryKey: ['orders'] })
        return response.data
    })
    return response
}