import { useQuery, UseQueryOptions, UseQueryResult } from "@tanstack/react-query";

export function useFetchData(myqueryKey: string, url: string, options?: {
    fetchOption?: RequestInit;
    reactQueryOption?: Omit<UseQueryOptions<OrderProps[], Error>, 'queryKey' | 'queryFn'>
}
): UseQueryResult<blocktile[], Error> {
    return useQuery({
        queryKey: [myqueryKey],
        queryFn: async (): Promise<OrderProps[]> => {
            const response = await fetch(`http://localhost:8000/${url}`, options?.fetchOption)
            if (!response.ok) {
                throw new Error('Network response was not ok')
            }
            return response.json()
        },
        ...options?.reactQueryOption
    })
}