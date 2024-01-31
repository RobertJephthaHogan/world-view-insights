import react from 'react'
import './styles.css'
import Header from '../../components/Header'
import TickerBanner from '../../components/TickerBanner'
import IndexBanner from '../../components/IndexBanner'
import NotableQuotes from '../../components/NotableQuotes'
import NewsSection from '../../components/NewsSection'


export default function Homepage() {

    return (
        <div>
            <Header/>
            <TickerBanner/>
            <IndexBanner/>
            <div className='homepage-body'>
                <div className='hpb-l'>
                    <div className='hpb-l-title-container'>
                        <span className='latest-news-title'>
                            Latest News
                        </span>
                    </div>
                    <NewsSection/>
                    <NewsSection/>
                    <NewsSection/>
                </div>
                <div className='hpb-r'>
                    <NotableQuotes/>
                </div>
            </div>
        </div>
    )
}