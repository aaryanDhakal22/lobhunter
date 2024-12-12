'use client'
async function syncOrders() {
    const response = await fetch("http://10.1.10.38:8000/api/sync", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        }
    });
    const orders = await response.json();
    return orders;
}

export default function Syncup() {

    return (

        <button onClick={syncOrders} className="bg-green-500 rounded-md inline-block text-xl py-3 px-4">📩Sync</button>

    )
}