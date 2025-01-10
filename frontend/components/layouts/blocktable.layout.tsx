'use client'
import { useFetchData } from "../hooks/dataFetch"
export default function BlockTable() {
    const { isLoading, isSuccess, isError, data, error } = useFetchData<string[]>('blocks', 'api/blocklist/blocks')
    if (isLoading) {
        return <p>Loading...</p>
    }
    if (isError) {
        return <p>Error: {(error as Error).message}</p>
    }
    if (isSuccess) {
        return (
            <div>
                {data.map((block: string) => {
                    return <div className="p-3 border rounded-sm mt-3 border-red-600" key={block} >{block}</div>
                })}
            </div>
        )
    }
}  