import NewsSection from '@/components/NewsSection'
import React, { useEffect, useState } from 'react'
import {newsService} from '@/services/news.service'
import { paginateArray } from '@/utils/pagination'


interface BusinessNewsProps {
    page: number
    sectionTitle?: any
    moreNewsTitle?: any
}

export default function BusinessNew(props: BusinessNewsProps) {

    const [articleSet, setArticleSet] = useState<any>([])


    useEffect(() => {

        newsService.getBusinessNewsArticles(20)
            .then((resp: any) => {
                const thisSet = paginateArray(resp, props.page, 4)
                setArticleSet(thisSet)
            })
            .catch((error: any) => {
                console.error('Error Getting Business News Articles', error)
            })


    }, [props.page])

    return (
        <div>
            <NewsSection
                sectionTitle={props.sectionTitle ? props.sectionTitle : "Business News"}
                moreNewsTitle={props.moreNewsTitle ? props.moreNewsTitle : "More Business News"}
                articles={articleSet}
            />
        </div>
    )
}