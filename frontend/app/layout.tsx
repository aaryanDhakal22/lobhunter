import "./globals.css";
import Syncup from "@/components/ui/sync.component";
import { ReactQueryClientProvider } from "@/components/ui/queryclientProvider";
import Link from "next/link";
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ReactQueryClientProvider>
      <html lang="en">
        <body className="bg-background">
          <header className="">
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
          </header>
          {children}
        </body>
      </html>
    </ReactQueryClientProvider>

  );

}
