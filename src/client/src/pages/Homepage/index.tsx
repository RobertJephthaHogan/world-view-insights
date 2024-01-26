import react from 'react'
import './styles.css'
import Header from '../../components/Header'
import TickerBanner from '../../components/TickerBanner'
import IndexBanner from '../../components/IndexBanner'


export default function Homepage() {

    return (
        <div>
            <Header/>
            <TickerBanner/>
            <IndexBanner/>
            Homepage
        </div>
    )
}