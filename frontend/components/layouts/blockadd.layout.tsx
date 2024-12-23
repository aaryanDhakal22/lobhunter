'use client'
import { useForm, SubmitHandler } from "react-hook-form"


export default function BlockListAdd() {
    const { register, handleSubmit, watch, formState: { errors }, } = useForm<BlockAdd>()

    // console.log(watch("address")) // watch input value by passing the name of it




    const onSubmit: SubmitHandler<BlockAdd> = async (data) => {
        const response = await fetch("http://10.1.10.38:8000/api/blocklist/add", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-type": "application/json"
            }
        })


    }


    return (
        <div>
            <div className="text-center text-2xl">BlockList</div>
            <div className="">
                <div className="">
                    <form className="flex gap-4" onSubmit={handleSubmit(onSubmit)}>
                        <input type="text" {...register("address")} placeholder="Address" className="input-field" name="address" id="address" />
                        <input type="number" {...register("phone")} placeholder="Phone no." className="input-field" name="phone" id="phone" />
                        <input type="submit" className="btn" value="Add" />

                    </form>

                </div>
            </div>
            <div>
            </div>
        </div>
    )
}

