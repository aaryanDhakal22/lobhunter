let socket: WebSocket | null = null
import primaryUrl from "@/ports/ports";
export const connectWebSocket = (
    onMessage: (kitchenTicket: KitchenTicket) => void,
    onError?: (error: Error) => void
): WebSocket | undefined => {
    const WS_URL = `wss://${primaryUrl}/ws/orders/`

    if (socket && socket.readyState === WebSocket.OPEN) {
        return;
    }

    socket = new WebSocket(WS_URL)

    socket.onmessage = (event) => {
        const data: KitchenTicket = JSON.parse(event.data)
        onMessage(data)
    }

    // Reconnect if WebSocket closes unexpectedly
    socket.onclose = () => {
        console.log("WebSocket closed. Reconnecting...");
        setTimeout(() => connectWebSocket(onMessage, onError), 3000);
    }
}
export const sendMessage = (message: string) => {
    if (socket && socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ message }));
    } else {
        console.error("WebSocket is not connected.");
    }
};
