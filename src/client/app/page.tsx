import Header from '../components/Header'
import TickerBanner from '../components/TickerBanner'
// import IndexBanner from '../../components/IndexBanner'
// import NotableQuotes from '../../components/NotableQuotes'
// import NewsSection from '../../components/NewsSection'
import styles from '../styles/page.module.css'



export default function Homepage() {

    return (
        <div>
            <Header/>
            <TickerBanner/>
            {/* <IndexBanner/>
            <div className={styles['homepage-body']}>
                <div className={styles['hpb-l']}>
                    <div className={styles['hpb-l-title-container']}>
                        <span className={styles['latest-news-title']}>
                            Latest News
                        </span>
                    </div>
                    <NewsSection/>
                    <NewsSection/>
                    <NewsSection/>
                </div>
                <div className={styles['hpb-r']}>z
                    <NotableQuotes/>
                </div>
            </div> */}
        </div>
    )
}