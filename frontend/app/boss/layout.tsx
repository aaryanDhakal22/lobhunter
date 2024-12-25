import Link from "next/link"
import Syncup from "@/components/ui/sync.component"

export default function BossLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <div className="">
            <div className="flex justify-around mt-5">
                <div>

                    <Link href="/boss" passHref>
                        <button className="bg-green-500 rounded-md inline-block p-5">🏠Home</button>
                    </Link>
                </div>
                <div className="mb-10 text-7xl text-center ">Nylon<span className="text-green-500">P0S</span></div>
                <div>
                    <Link href="/boss/blocklist">
                        <button className="bg-red-500 py-3 px-4 rounded-md text-xl mr-3">BlockList</button>
                    </Link>
                    <Syncup />

                </div>

            </div>
            {children}
        </div>
    )
}