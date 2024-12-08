import OrderList from "@/components/layouts/orderList.layout"
import Controls from "@/components/layouts/controls.layout"

export default function ClientPage() {
    return (
        <>
            <div className="text-center text-2xl">Client Page</div>
            <div className="flex flex-row h-screen">
                <div className="basis-1/2"><OrderList /></div>
                <div className="basis-1/2"><Controls /></div>
            </div>
        </>
    )
}