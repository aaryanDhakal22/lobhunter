'use client'

import { useQuery } from "@tanstack/react-query";
import axios from "axios";
import queryClient from "./queryclientProvider";

export default function Syncup() {
    // const primaryUrl = "10.1.10.38"
    const primaryUrl = "localhost"
    const { isLoading, error, isSuccess, data, isFetching } = useQuery({
        queryKey: ["sync"],
        queryFn: async () => {
            const response = await axios.get("http://localhost:8000/api/sync")
            return response
        }
    })
    const handleSync = () => {
        queryClient.invalidateQueries({ queryKey: ['sync'] })
    }
    if (isLoading || isFetching) {
        return <button className="bg-slate-400 rounded-md inline-block text-xl py-3 px-5 " disabled>
            <div className="box-border">
                <div className=" w-[1.4rem] h-[1.4rem] border-4 border-t-green-400 border-gray-300 rounded-full animate-spin inline-block"></div>
                <div className=" inline-block ml-2">Syncing...</div>
            </div>
        </button>
    }
    if (isSuccess) {

        return (
            <button onClick={handleSync} className="bg-green-500 rounded-md inline-block text-xl py-3 px-4">📩Sync</button>
        )
    }
    return <div>Error Occured</div>
}