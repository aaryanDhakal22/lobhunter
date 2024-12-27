import { useState } from "react"

export default function KitchenOrder({ item }: { item: KitchenOrder }) {
    const [isVisible, setVisible] = useState<"hidden" | "">("")
    console.log(item)
    return (
        <div key={item.id} className={`bg-white inline-block shrink-0 text-black p-6 rounded-md ${isVisible}`}>
            <div className="flex justify-between">
                <div className="text-3xl text-red-600 mb-2">Order No : {item.kitchenNumber.toString()}</div>
                <button onClick={() => setVisible("hidden")} className="btn bg-blue-500 text-white" >DONE</button>

            </div>
            <div dangerouslySetInnerHTML={{ __html: item.ticket }} ></div>
        </div>
    )
}