export async function fetchJSON(context) {
    const url = context.env.LATEST_URL;
    console.log("url", url);
    const response = await fetch(url);
    const text = await response.text();
    return new Response(JSON.parse(text));
}
