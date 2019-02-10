const puppeteer = require('puppeteer');
function run () {
    return new Promise(async (resolve, reject) => {
        try {
            const browser = await puppeteer.launch();
            const page = await browser.newPage();
            await page.goto("https://www.semanticscholar.org/search?q=google&sort=relevance");
            let urls = await page.evaluate(() => {
                let results = [];
                let items = document.querySelectorAll('div#app')
                items.forEach((item) => {
                    results.push({
                        // url: item.href,
                        text: item.innerText,
                    });
                });
                return results;
            })
            browser.close();
            return resolve(urls);
        } catch (e) {
            return reject(e);
        }
    })
}
run().then(console.log).catch(console.error);