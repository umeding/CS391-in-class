import Link from "next/link";

export default function About(){
    return(
        <div>
            <br/>
            <h1>About me:</h1>
            <h2>{"I'm a SWE and I don't like Java that much."}</h2>
            <br/>
            <Link href="/blog">Go to Blog</Link>
            <br/>
            <Link href="/news">SpaceNews!</Link>
            <br/>
            <Link href="/">Back home</Link>
        </div>
    )
}