import axios from "axios";
export async function updateStatus(orderNumber: string, status: string) => {
    const response = await axios.put(`http://10.1.10.38:8000/orders/status/${orderNumber}`, status)
    return response.data
}