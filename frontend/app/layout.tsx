import Image from "next/image";
import "./globals.css";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-background">
        <header>
          <div className="text-3xl">NylonPOS</div>
        </header>
        {children}
      </body>
    </html>
  );
}
