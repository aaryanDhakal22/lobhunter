import { useQuery, UseQueryOptions, UseQueryResult } from "@tanstack/react-query";

export function useFetchData<TData>(myqueryKey: string, url: string, options?: {
    fetchOption?: RequestInit;
    reactQueryOption?: Omit<UseQueryOptions<TData, Error>, 'queryKey' | 'queryFn'>
}
): UseQueryResult<TData, Error> {
    // const primaryUrl = "10.1.10.38"
    const primaryUrl = "localhost"
    return useQuery<TData, Error>({
        queryKey: [myqueryKey],
        queryFn: async (): Promise<TData> => {
            const response = await fetch(`http://${primaryUrl}:8000/${url}`, options?.fetchOption)
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json()
        },
        ...options?.reactQueryOption
    })
}