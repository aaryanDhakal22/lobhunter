let socket: WebSocket | null = null

export const connectWebSocket = (
    onMessage: (message: string) => void,
    onError?: (error: Error) => void
): WebSocket | undefined => {
    const primaryUrl = "10.1.10.38"
    // const primaryUrl = "localhost"
    const WS_URL = `ws://${primaryUrl}:8000/ws/orders/`

    if (socket && socket.readyState === WebSocket.OPEN) {
        return;
    }

    socket = new WebSocket(WS_URL)

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data)
        onMessage(data.message)
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