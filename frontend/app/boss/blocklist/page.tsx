import Cfinder from "@/components/layouts/cfinder.layout"
import BlockListTemplate from "@/components/layouts/blocklist.layout"
export default function BlockPage() {
    return (
        <div className="flex flex-row ">

            <div className="basis-1/2">
                <Cfinder />
            </div>
            <div className="basis-1/2 ">
                <BlockListTemplate />
            </div>
        </div>
    )
}