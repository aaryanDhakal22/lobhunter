declare global {
    interface OrderProps {
        email_id: string; // Corresponds to CharField(max_length=20)
        order_number: number; // Corresponds to IntegerField(primary_key=True)
        customer_name: string; // Corresponds to CharField(max_length=255)
        date: string; // Corresponds to DateField, represented as a string in ISO format (e.g., 'YYYY-MM-DD')
        phone: number; // Corresponds to IntegerField
        total: string; // Corresponds to DecimalField(max_digits=10, decimal_places=2), handled as a string to avoid floating-point precision issues
        payment: string; // Corresponds to CharField(max_length=5)
        ticket: string; // Corresponds to CharField(max_length=1000)
        address?: string; // Corresponds to CharField(max_length=30, null=True), optional in TypeScript
        time: string; // Corresponds to TimeField(default="00:00:00"), represented as a string (e.g., 'HH:mm:ss')
        status: string; // Corresponds to CharField(max_length=10)


    }
    interface Blocktile {
        order_number: number,
        total: string,
        customer_name: string
    }

    interface ResponseApi {
        success: string,
        message: string,
        payload: Blocktile[]
    }
    interface BlockAdd {
        address: string,
        phone: string
    }
    interface ApiResponse {
        message: string; // Successful API response
    }

    interface ApiError {
        message: string; // Error message
        status?: number; // Optional status code
    }

}

export { }; // Ensures the file is treated as a module.
