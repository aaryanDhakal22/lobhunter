'use client'
import Link from "next/link"

async function syncOrders() {
    const response = await fetch("http://10.0.0.167:8000/api/sync", {
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

        <button onClick={syncOrders} className="bg-green-500 rounded-md inline-block p-5">📩Sync</button>

    )
}