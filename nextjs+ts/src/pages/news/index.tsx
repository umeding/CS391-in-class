"use client"
import {useState, useEffect, ReactNode} from 'react'
import Link from "next/link";

const MAX_ARTICLE_PAGES: number = 100;

// so that we can iterate through Articles json
interface Article {
    id: number;
    title: string;
    url: string;
    image_url: string;
    news_site: string;
    summary: string;
    published_at: string;
    updated_at: string;
    featured: boolean;
    launches: Launch[];
    events: any[]; // Assuming events can be of any type
  }

interface Launch {
    launch_id: string;
    provider: string;
  }

export default function NewsList() {
    const [articles, setArticles] = useState<[]>([])
    const [articlesOffset, setArticlesOffset] = useState<number>(0)


    /*
     * The useEffect hook allows application code to respond to user inputs.
     * In this case, we use it to query the SpaceNews API, and then store
     * the response in component state `articles`.
    * */
    useEffect( ()=> {
        async function getArticles(){

            // fetch is an async function, so we have to `await` it.
            const resp = await fetch(
                `https://api.spaceflightnewsapi.net/v4/articles/?limit=5&offset=${articlesOffset}`
                )
            if (!resp.ok) return []

            // *.json() is also async, so we have to `await` it as well.
            const data = await resp.json()

            // set state IN async function.
            setArticles(data.results);
        }

        // calls async function, doesn't get return val.
        // async functions return Promises by default,
        // even when we return something that should be a value.
        getArticles().catch(console.error)
    }, [articlesOffset])

    function handleClick(){
       setArticlesOffset(
        (curOffset) => {
            if(curOffset < MAX_ARTICLE_PAGES){
                return curOffset + 5;
            }
            else{
		// wrap around to 0
                return 0
            }
        }
       ) 
    }

    return (
        <div>
            <br />
            <button onClick={handleClick}>Next 5 Articles</button>
            <br />
            {articles.length > 0 ? <h1>Articles page: {(articlesOffset/5) + 1}</h1> : <h1>Getting data...</h1>}
            <br />
            {
                articles.map(
                    (article: Article, idx: number) => {
                        return (
                            <div key={idx}>
                                <ArticleCard key={idx} article={article}/>
                                <br />
                            </div>
                        )
                    } 
                )
            }
            <br />
            <Link href="/blog">Go to Blog</Link>
            <br />
            <Link href="/about">Go to About</Link>
        </div>
    )
  }

  // typing props nicely
  function ArticleCard({article}: {article:Article}){
    return(
        <div>
            <h2>{article.title}</h2>
            <p>{article.summary}</p>
        </div>
    )
  }
