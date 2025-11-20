import { useQuery, UseQueryOptions, UseQueryResult } from "@tanstack/react-query";
import primaryUrl from "@/ports/ports";
export function useFetchData<TData>(myqueryKey: string, url: string, options?: {
    fetchOption?: RequestInit;
    reactQueryOption?: Omit<UseQueryOptions<TData, Error>, 'queryKey' | 'queryFn'>
}
): UseQueryResult<TData, Error> {
    return useQuery<TData, Error>({
        queryKey: [myqueryKey],
        queryFn: async (): Promise<TData> => {
            const response = await fetch(`https://${primaryUrl}/${url}`, options?.fetchOption)
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json()
        },
        ...options?.reactQueryOption
    })
}
