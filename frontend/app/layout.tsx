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
          <div className="absolute top-5 left-5 w-52 h-52 bg-red-500 opacity-30 border-2 border-red-500"></div>

          <Image
            src="/images/logo.png"
            alt="Logo"
            width={300}
            height={100}
            className="m-4"
          />
          <div></div>
        </header>
        {children}
      </body>
    </html>
  );
}
