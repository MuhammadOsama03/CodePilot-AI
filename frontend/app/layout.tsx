import type { ReactNode } from "react";
import "./globals.css";
export const metadata = { title: "CodePilot AI | Work in Progress", description: "AI-assisted code review workspace" };
export default function RootLayout({ children }: { children: ReactNode }) { return <html lang="en"><body>{children}</body></html>; }
