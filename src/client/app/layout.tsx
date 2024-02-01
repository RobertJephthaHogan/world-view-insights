import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "../styles/globals.css";

const inter = Inter({ subsets: ["latin"] });


const keywordSearchTerms = [
  "current mortgage rates",
  "best stocks to buy",
  "home buying tips",
  "real estate market analysis",
  "is now a good time to buy a house",
  "latest business news",
  "market updates",
  "stock market news",
  "technology updates",
  "tech industry news",
  "advanced stock scanner",
  "stock value checker",
  "stock price for XYZ", // replace XYZ with specific tickers
  "stock market charts",
  "interactive stock analysis",
  "investment opportunities",
  "financial market insights",
  "economic news",
  "stock trading tips",
  "tech stocks",
  "stock market trends",
  "real estate investment advice",
  "mortgage rate trends",
  "financial planning",
  "stock portfolio management",
  "technology sector analysis",
  "business strategy news",
  "stock market analysis tools",
  "personal finance tips"
];

export const metadata: Metadata = {
  title: "WorldView Insights",
  description: "All in one source for news, market data, investing tools, overall insights",
  keywords: keywordSearchTerms
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

	return (
		<html lang="en">
			<body className={inter.className}>
				{children}
			</body>
		</html>
	);
}
