export default function BlockListTemplate() {
    return (
        <div>
            <div className="text-center text-2xl">BlockList</div>
            <div className="">
                <div className="">
                    <form className="flex gap-4">
                        <input type="text" className="input-field" name="address" id="address" />
                        <input type="text" className="input-field" name="phone" id="phone" />
                        <input type="submit" className="btn" value="Add" />
                    </form>
                </div>
            </div>
        </div>
    )
}