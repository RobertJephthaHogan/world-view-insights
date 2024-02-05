import Header from '@/components/Header';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });



const ArticlePage: NextPage<any> = ({ article }) => {
  return (
    <div className={inter.className}>
		<Header/>
		<h1>{article?.title}</h1>
		<p>{article?.content}</p>
		<p>Article Page!</p>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {

	const { id } = context.params!;
	
	// const res = await fetch(`https://examoke.com/articles/${id}`);
	// const article: any = await res.json();
	console.log('id', id)

	return {
		props: { id },
	};
};

export default ArticlePage;