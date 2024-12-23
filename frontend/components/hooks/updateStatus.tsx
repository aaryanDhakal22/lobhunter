'use client'
import axios from "axios";

export async function updateStatus(orderNumber: string, status: string) {
    const payload = {
        "order_number": orderNumber.toString(),
        "status": status
    }
    console.log(payload)
    const response = await axios.put(`http://10.1.10.38:8000/api/order/status/`, payload).then(response => {
        console.log(response.data)
        return response.data
    })
    return response
}