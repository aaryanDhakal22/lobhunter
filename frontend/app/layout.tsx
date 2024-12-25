import "./globals.css";
import { ReactQueryClientProvider } from "@/components/ui/queryclientProvider";
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ReactQueryClientProvider>
      <html lang="en">
        <body className="bg-background">
          {children}
        </body>
      </html>
    </ReactQueryClientProvider>

  );

}
