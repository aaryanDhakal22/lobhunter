import { useMutation } from "@tanstack/react-query"
import { updateStatus } from "../hooks/updateStatus"

export default function StatusButtons({ order_number, sendMessage }: { order_number: string, sendMessage: (order_number: string) => void }) {

    const mutation = useMutation({
        mutationFn: (status: string) => {
            return updateStatus(order_number, status)
        }
    },)

    const handleClick = (status: string) => {
        if (status == "accepted") {
            sendMessage(order_number)
        }
        const response = mutation.mutate(status)
    }
    return (
        <div className="grid grid-cols-3 p-4 gap-4">
            <button onClick={() => { handleClick("accepted") }} className="bg-green-500 p-3 rounded-lg">Accept</button>
            <button onClick={() => { handleClick("rejected") }} className="bg-red-500 p-3 rounded-lg">Reject</button>
            <button onClick={() => { handleClick("dismissed") }} className="bg-slate-500 p-3 rounded-lg">Dismiss</button>
        </div>
    )
}