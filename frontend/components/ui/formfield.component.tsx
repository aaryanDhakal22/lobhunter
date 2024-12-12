
export default function TextInput({ value, setValue }: { value: string, setValue: (value: string) => void }) {
    return (
        <input type="text" value={value} onChange={(e) => setValue(e.target.value)} />
    )
}