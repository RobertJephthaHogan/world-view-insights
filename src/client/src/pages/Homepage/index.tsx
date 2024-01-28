import react from 'react'
import './styles.css'
import Header from '../../components/Header'
import TickerBanner from '../../components/TickerBanner'
import IndexBanner from '../../components/IndexBanner'
import NotableQuotes from '../../components/NotableQuotes'


export default function Homepage() {

    return (
        <div>
            <Header/>
            <TickerBanner/>
            <IndexBanner/>
            <div className='homepage-body'>
                <div className='hpb-l'>
                    Homepage Left
                </div>
                <div className='hpb-r'>
                    <NotableQuotes/>
                </div>
            </div>
        </div>
    )
}