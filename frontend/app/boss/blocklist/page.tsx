import Cfinder from "@/components/layouts/cfinder.layout"
import BlockListAdd from "@/components/layouts/blockadd.layout"
import BlockTable from "@/components/layouts/blocktable.layout"
export default function BlockPage() {
    return (
        <div className="flex flex-row ">

            <div className="basis-1/2">
                <Cfinder />
            </div>
            <div className="basis-1/2 ">
                <BlockListAdd />
                <BlockTable />

            </div>
        </div>
    )
}