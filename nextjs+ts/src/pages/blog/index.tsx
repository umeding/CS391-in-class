import Link from "next/link";

export default function Blog(){
    return (
        <div>
            <br></br>
            <h1>My new blog!</h1>
            <h2>{"(There's nothing here...)"}</h2>
            <br></br>
            <Link href="/about">Go to About</Link>
            <br/>
            <Link href="/news">SpaceNews!</Link>
            <br />
            <Link href="/">Back home</Link>
        </div>
    )
}