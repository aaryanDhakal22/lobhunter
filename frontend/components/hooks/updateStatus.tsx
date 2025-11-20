'use client'
import primaryUrl from "@/ports/ports";
import axios from "axios";
import queryClient from "../ui/queryclientProvider";
export async function updateStatus(orderNumber: string, status: string) {
    const payload = {
        "order_number": orderNumber.toString(),
        "status": status
    }
    // console.log(payload)
    const response = await axios.put(`https://${primaryUrl}/api/order/status/`, payload).then(response => {
        // console.log(response.data)
        queryClient.invalidateQueries({ queryKey: ['orders'] })
        return response.data
    })
    return response
}
