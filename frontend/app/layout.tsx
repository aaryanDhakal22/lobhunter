import Image from "next/image";
import "./globals.css";
import Syncup from "@/components/ui/sync.component";
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-background">
        <header className="">
          <div className="flex justify-around mt-5">
            <div>

              <button className="bg-green-500 rounded-md inline-block p-5">🏠Home</button>
            </div>
            <div className="mb-10 text-7xl text-center ">Nylon<span className="text-green-500">POS</span></div>
            <div>
              <Syncup />

            </div>

          </div>
        </header>
        {children}
      </body>
    </html>
  );
}
