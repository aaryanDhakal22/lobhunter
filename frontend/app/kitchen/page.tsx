'use client'
import { connectWebSocket, sendMessage } from "@/components/hooks/websocket"
import React, { useEffect, useState } from 'react'
interface Message {
    id: string,
    text: string
}

const MessageList: React.FC = () => {
    const [messages, setMessages] = useState<Message[]>([]);

    useEffect(() => {
        const socket = connectWebSocket((incomingMessage: string) => {
            const newMessage = { id: Date.now().toString(), text: incomingMessage };
            setMessages((prevMessages) => [...prevMessages, newMessage]);
        })
        return () => {
            if (socket) socket?.close
        }
    }, [])

    return (
        <div className="p-4">
            <div className="flex gap-5 ">
                {messages.map((item: Message) => {
                    return <div className='bg-white inline text-black p-6 rounded-md' dangerouslySetInnerHTML={{ __html: item.text }} key={item.id}></div>
                })}
            </div>
        </div>
    )
}

export default MessageList